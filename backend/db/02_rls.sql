-- =============================================================================
-- MATU · Aislamiento con Row Level Security · versión 1.0
-- Se ejecuta como matu_owner después de 01_esquema.sql
--
-- Ejes de acceso (sección 7.7, ampliada):
--   familia     app.grupo_id       (verificado contra membresía por la API)
--   comercio    app.comercio_id
--   repartidor  app.repartidor_id
--   relevo      app.rol = 'relevo' + app.acceso_relevo_id, y NUNCA app.grupo_id:
--               si lo fijara, heredaría todas las políticas de familia (pedidos,
--               pagos, direcciones). Sus políticas se resuelven solo por el acceso.
--   operación   app.rol = 'operacion'
--   sistema     app.rol = 'sistema' (worker y dos casos de uso públicos acotados)
--
-- REGLA APRENDIDA AL ESCRIBIR ESTE ARCHIVO
--   Una hija que hereda con EXISTS (SELECT 1 FROM padre ...) hereda TODAS las
--   políticas del padre, no solo la de familia. Si el padre es visible para el
--   relevo, el comercio o el repartidor, la hija también lo será.
--   Por eso las hijas de tablas con varios ejes (plan_cuidado, pedido) declaran
--   su condición de forma explícita en vez de heredar.
-- =============================================================================

-- ¿El usuario de la sesión puede ver el plan de cuidado del grupo en contexto?
-- admin y cuidador siempre, pagador solo con permiso explícito, observador nunca.
CREATE FUNCTION app_puede_ver_plan() RETURNS boolean LANGUAGE sql STABLE AS
$$ SELECT EXISTS (SELECT 1 FROM membresia m
                  WHERE m.grupo_id = app_grupo() AND m.usuario_id = app_usuario()
                    AND m.estado = 'activa'
                    AND (m.rol IN ('admin', 'cuidador') OR m.puede_ver_plan)) $$;

-- -----------------------------------------------------------------------------
-- Activar y FORZAR RLS en toda tabla de negocio.
-- Excepciones declaradas (sin RLS, acotadas por permiso en 03_permisos.sql):
--   evento_outbox, evento_consumido, indice_token, indice_credencial
-- -----------------------------------------------------------------------------
DO $$
DECLARE t text;
BEGIN
  FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public'
           AND tablename NOT IN ('evento_outbox', 'evento_consumido', 'indice_token', 'indice_credencial')
  LOOP
    EXECUTE format('ALTER TABLE %I ENABLE ROW LEVEL SECURITY', t);
    EXECUTE format('ALTER TABLE %I FORCE ROW LEVEL SECURITY', t);
  END LOOP;
END $$;

-- =============================================================================
-- iam
-- =============================================================================
CREATE POLICY usuario_propio     ON usuario FOR ALL    USING (id = app_usuario());
CREATE POLICY usuario_comiembro  ON usuario FOR SELECT USING (EXISTS (
    SELECT 1 FROM membresia m WHERE m.usuario_id = usuario.id AND m.grupo_id = app_grupo()));
CREATE POLICY usuario_operacion  ON usuario FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY dispositivo_propio    ON dispositivo FOR ALL    USING (usuario_id = app_usuario());
CREATE POLICY dispositivo_operacion ON dispositivo FOR SELECT USING (app_rol() = 'operacion');

CREATE POLICY sesion_propia    ON sesion_refresh FOR ALL USING (usuario_id = app_usuario());
CREATE POLICY sesion_operacion ON sesion_refresh FOR ALL USING (app_rol() = 'operacion');

-- =============================================================================
-- care_circle
-- =============================================================================
-- Las políticas de la aplicación se declaran TO matu_app: si fueran PUBLIC, el
-- scheduler evaluaría grupo_mis_grupos y fallaría por no tener permiso sobre membresia.
CREATE POLICY grupo_familia      ON grupo_familiar FOR ALL    TO matu_app USING (id = app_grupo());
CREATE POLICY grupo_mis_grupos   ON grupo_familiar FOR SELECT TO matu_app USING (EXISTS (
    SELECT 1 FROM membresia m WHERE m.grupo_id = grupo_familiar.id
      AND m.usuario_id = app_usuario() AND m.estado = 'activa'));
CREATE POLICY grupo_crear        ON grupo_familiar FOR INSERT TO matu_app WITH CHECK (creado_por = app_usuario());
CREATE POLICY grupo_creador_ver  ON grupo_familiar FOR SELECT TO matu_app USING (creado_por = app_usuario());
CREATE POLICY grupo_operacion    ON grupo_familiar FOR ALL    TO matu_app USING (app_rol() = 'operacion');
CREATE POLICY grupo_scheduler    ON grupo_familiar FOR SELECT TO matu_scheduler USING (estado = 'activo');

CREATE POLICY membresia_propia    ON membresia FOR SELECT USING (usuario_id = app_usuario());
CREATE POLICY membresia_familia   ON membresia FOR ALL    USING (grupo_id = app_grupo());
CREATE POLICY membresia_fundador  ON membresia FOR INSERT WITH CHECK (
    usuario_id = app_usuario() AND rol = 'admin' AND EXISTS (
        SELECT 1 FROM grupo_familiar g WHERE g.id = grupo_id AND g.creado_por = app_usuario()));
CREATE POLICY membresia_operacion ON membresia FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY invitacion_familia   ON invitacion FOR ALL    USING (grupo_id = app_grupo());
CREATE POLICY invitacion_operacion ON invitacion FOR SELECT USING (app_rol() = 'operacion');

CREATE POLICY direccion_familia   ON direccion FOR ALL USING (grupo_id = app_grupo());
CREATE POLICY direccion_operacion ON direccion FOR ALL USING (app_rol() = 'operacion');

CREATE POLICY persona_familia   ON persona_cuidada FOR ALL    USING (grupo_id = app_grupo());
CREATE POLICY persona_operacion ON persona_cuidada FOR SELECT USING (app_rol() = 'operacion');

CREATE POLICY consentimiento_familia   ON consentimiento FOR ALL    USING (grupo_id = app_grupo());
CREATE POLICY consentimiento_operacion ON consentimiento FOR SELECT USING (app_rol() = 'operacion');

-- =============================================================================
-- care_plan · CAPA 1 · operación NO tiene política en ninguna de estas tablas
-- =============================================================================
CREATE POLICY clave_familia ON clave_datos FOR ALL
    USING (grupo_id = app_grupo() AND (SELECT app_puede_ver_plan()));
CREATE POLICY clave_relevo  ON clave_datos FOR SELECT USING (
    app_rol() = 'relevo' AND EXISTS (
        SELECT 1 FROM acceso_relevo a JOIN plan_cuidado p ON p.id = a.plan_id
        WHERE a.id = app_acceso_relevo() AND p.persona_cuidada_id = clave_datos.persona_cuidada_id));

CREATE POLICY plan_familia ON plan_cuidado FOR ALL
    USING (grupo_id = app_grupo() AND (SELECT app_puede_ver_plan()));
CREATE POLICY plan_relevo  ON plan_cuidado FOR SELECT USING (
    app_rol() = 'relevo' AND EXISTS (
        SELECT 1 FROM acceso_relevo a WHERE a.id = app_acceso_relevo() AND a.plan_id = plan_cuidado.id));

-- Explícita, no heredada: heredar de plan_cuidado le daría al relevo TODAS las secciones
CREATE POLICY seccion_familia ON plan_seccion FOR ALL USING (EXISTS (
    SELECT 1 FROM plan_cuidado p WHERE p.id = plan_seccion.plan_id
      AND p.grupo_id = app_grupo() AND (SELECT app_puede_ver_plan())));
CREATE POLICY seccion_relevo  ON plan_seccion FOR SELECT USING (
    app_rol() = 'relevo' AND EXISTS (
        SELECT 1 FROM acceso_relevo a WHERE a.id = app_acceso_relevo()
          AND a.plan_id = plan_seccion.plan_id AND plan_seccion.tipo = ANY (a.secciones_permitidas)));

-- Explícita por la misma razón: el relevo no ve los otros accesos del plan
CREATE POLICY acceso_familia ON acceso_relevo FOR ALL
    USING (grupo_id = app_grupo() AND (SELECT app_puede_ver_plan()));
-- El relevo ve solo su propio acceso, y solo mientras está vigente.
-- Vencido o revocado = cero filas, y la API responde 410.
CREATE POLICY acceso_relevo_propio ON acceso_relevo FOR ALL USING (
    app_rol() = 'relevo' AND id = app_acceso_relevo()
    AND revocado_en IS NULL AND expira_en > now());

-- =============================================================================
-- catalog · datos de referencia legibles por todos, escritos por operación
-- =============================================================================
CREATE POLICY categoria_lectura   ON categoria_cuidado FOR SELECT USING (true);
CREATE POLICY categoria_operacion ON categoria_cuidado FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY producto_lectura   ON producto FOR SELECT USING (true);
CREATE POLICY producto_operacion ON producto FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY comercio_lectura   ON comercio FOR SELECT USING (estado = 'activo' OR id = app_comercio());
CREATE POLICY comercio_operacion ON comercio FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY usuario_comercio_propio    ON usuario_comercio FOR SELECT USING (usuario_id = app_usuario());
CREATE POLICY usuario_comercio_comercio  ON usuario_comercio FOR SELECT USING (comercio_id = app_comercio());
CREATE POLICY usuario_comercio_operacion ON usuario_comercio FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY convenio_comercio  ON convenio FOR SELECT USING (comercio_id = app_comercio());
CREATE POLICY convenio_operacion ON convenio FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY oferta_lectura   ON oferta FOR SELECT USING (true);
CREATE POLICY oferta_comercio  ON oferta FOR UPDATE USING (comercio_id = app_comercio());
CREATE POLICY oferta_operacion ON oferta FOR ALL    USING (app_rol() = 'operacion');

-- =============================================================================
-- consumption · CAPA 2 · solo familia. Operación nunca (sección 7.7, hecho 2)
-- =============================================================================
CREATE POLICY perfil_familia ON perfil_consumo FOR ALL USING (grupo_id = app_grupo());
-- Hijas: el padre tiene un solo eje, así que heredar es seguro
CREATE POLICY reposicion_hereda ON reposicion     FOR ALL USING (EXISTS (
    SELECT 1 FROM perfil_consumo p WHERE p.id = reposicion.perfil_id));
CREATE POLICY alerta_hereda     ON alerta_quiebre FOR ALL USING (EXISTS (
    SELECT 1 FROM perfil_consumo p WHERE p.id = alerta_quiebre.perfil_id));

-- =============================================================================
-- ordering
-- =============================================================================
CREATE POLICY pedido_familia ON pedido FOR ALL USING (grupo_id = app_grupo());
-- El comercio ve sus pedidos recién cuando ya están autorizados y enviados
CREATE POLICY pedido_comercio_ver ON pedido FOR SELECT USING (
    comercio_id = app_comercio()
    AND estado NOT IN ('borrador', 'pendiente_recaudacion', 'autorizado', 'expirado'));
CREATE POLICY pedido_comercio_actualizar ON pedido FOR UPDATE USING (
    comercio_id = app_comercio()
    AND estado NOT IN ('borrador', 'pendiente_recaudacion', 'autorizado', 'expirado'));
CREATE POLICY pedido_repartidor ON pedido FOR SELECT USING (EXISTS (
    SELECT 1 FROM asignacion a WHERE a.pedido_id = pedido.id
      AND a.repartidor_id = app_repartidor() AND a.estado = 'activa'));
CREATE POLICY pedido_operacion ON pedido FOR ALL USING (app_rol() = 'operacion');

-- Explícita: el comercio NUNCA ve la dirección de entrega
CREATE POLICY entrega_familia ON pedido_entrega FOR ALL USING (EXISTS (
    SELECT 1 FROM pedido p WHERE p.id = pedido_entrega.pedido_id AND p.grupo_id = app_grupo()));
CREATE POLICY entrega_repartidor ON pedido_entrega FOR SELECT USING (EXISTS (
    SELECT 1 FROM asignacion a WHERE a.pedido_id = pedido_entrega.pedido_id
      AND a.repartidor_id = app_repartidor() AND a.estado = 'activa'));
CREATE POLICY entrega_operacion ON pedido_entrega FOR ALL USING (app_rol() = 'operacion');

-- Hereda del pedido EXCEPTO para el repartidor, que no ve precios unitarios (11.2)
CREATE POLICY linea_hereda ON pedido_linea FOR ALL USING (
    app_repartidor() IS NULL AND EXISTS (SELECT 1 FROM pedido p WHERE p.id = pedido_linea.pedido_id));
CREATE POLICY regla_hereda ON regla_sustitucion FOR ALL USING (
    app_repartidor() IS NULL AND EXISTS (SELECT 1 FROM pedido p WHERE p.id = regla_sustitucion.pedido_id));
CREATE POLICY transicion_hereda ON pedido_transicion FOR ALL USING (EXISTS (
    SELECT 1 FROM pedido p WHERE p.id = pedido_transicion.pedido_id));

-- =============================================================================
-- replenishment · solo familia
-- =============================================================================
CREATE POLICY plan_repo_familia ON plan_reposicion FOR ALL USING (grupo_id = app_grupo());
CREATE POLICY plan_repo_linea_hereda ON plan_reposicion_linea FOR ALL USING (EXISTS (
    SELECT 1 FROM plan_reposicion p WHERE p.id = plan_reposicion_linea.plan_reposicion_id));
CREATE POLICY ocurrencia_hereda ON ocurrencia FOR ALL USING (EXISTS (
    SELECT 1 FROM plan_reposicion p WHERE p.id = ocurrencia.plan_reposicion_id));

-- =============================================================================
-- payments · familia y operación. Ni comercio ni repartidor
-- =============================================================================
CREATE POLICY cargo_familia ON cargo FOR ALL USING (EXISTS (
    SELECT 1 FROM pedido p WHERE p.id = cargo.pedido_id AND p.grupo_id = app_grupo()));
CREATE POLICY cargo_operacion ON cargo FOR ALL USING (app_rol() = 'operacion');
-- Hijas de cargo, que solo tiene familia y operación: heredar es seguro
CREATE POLICY participacion_hereda ON participacion FOR ALL USING (EXISTS (
    SELECT 1 FROM cargo c WHERE c.id = participacion.cargo_id));
CREATE POLICY transaccion_hereda ON transaccion_pasarela FOR ALL USING (EXISTS (
    SELECT 1 FROM participacion p WHERE p.id = transaccion_pasarela.participacion_id));

CREATE POLICY medio_pago_propio ON medio_pago_inscrito FOR ALL USING (usuario_id = app_usuario());

-- =============================================================================
-- fulfillment
-- =============================================================================
CREATE POLICY repartidor_propio    ON repartidor FOR SELECT USING (usuario_id = app_usuario() OR id = app_repartidor());
CREATE POLICY repartidor_operacion ON repartidor FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY oferta_asig_repartidor ON oferta_asignacion FOR ALL USING (repartidor_id = app_repartidor());
CREATE POLICY oferta_asig_operacion  ON oferta_asignacion FOR ALL USING (app_rol() = 'operacion');
CREATE POLICY oferta_asig_sistema    ON oferta_asignacion FOR ALL USING (app_rol() = 'sistema');

CREATE POLICY asignacion_repartidor ON asignacion FOR ALL    USING (repartidor_id = app_repartidor());
CREATE POLICY asignacion_familia    ON asignacion FOR SELECT USING (grupo_id = app_grupo());
CREATE POLICY asignacion_operacion  ON asignacion FOR ALL    USING (app_rol() = 'operacion');

CREATE POLICY evidencia_hereda ON evidencia FOR ALL USING (EXISTS (
    SELECT 1 FROM pedido p WHERE p.id = evidencia.pedido_id));

-- =============================================================================
-- settlement · comercio y operación
-- =============================================================================
CREATE POLICY consumo_comercio_propio    ON consumo_comercio FOR ALL USING (comercio_id = app_comercio());
CREATE POLICY consumo_comercio_operacion ON consumo_comercio FOR ALL USING (app_rol() = 'operacion');

CREATE POLICY liquidacion_comercio  ON liquidacion FOR SELECT USING (comercio_id = app_comercio());
CREATE POLICY liquidacion_operacion ON liquidacion FOR ALL    USING (app_rol() = 'operacion');

-- =============================================================================
-- notifications
-- =============================================================================
CREATE POLICY preferencia_propia ON preferencia_notificacion FOR ALL USING (usuario_id = app_usuario());
-- Si no hay preferencia propia, el consumidor de notificaciones (sistema) la lee por grupo
CREATE POLICY preferencia_sistema ON preferencia_notificacion FOR SELECT USING (
    app_rol() = 'sistema' AND EXISTS (SELECT 1 FROM membresia m
        WHERE m.usuario_id = preferencia_notificacion.usuario_id AND m.grupo_id = app_grupo()));

CREATE POLICY notificacion_propia    ON notificacion FOR SELECT USING (usuario_id = app_usuario());
CREATE POLICY notificacion_sistema   ON notificacion FOR ALL    USING (app_rol() = 'sistema' AND grupo_id = app_grupo());
CREATE POLICY notificacion_operacion ON notificacion FOR SELECT USING (app_rol() = 'operacion');

-- =============================================================================
-- backoffice
-- =============================================================================
CREATE POLICY incidencia_operacion ON incidencia FOR ALL    USING (app_rol() = 'operacion');
CREATE POLICY incidencia_familia   ON incidencia FOR SELECT USING (EXISTS (
    SELECT 1 FROM pedido p WHERE p.id = incidencia.pedido_id AND p.grupo_id = app_grupo()));

-- =============================================================================
-- shared
-- =============================================================================
-- Auditoría: la familia ve la de su grupo (pantalla "quién ha visto el plan").
-- Cualquiera inserta, pero solo en su propio grupo o sin grupo.
CREATE POLICY auditoria_familia   ON auditoria FOR SELECT USING (grupo_id = app_grupo());
CREATE POLICY auditoria_operacion ON auditoria FOR SELECT USING (app_rol() = 'operacion');
CREATE POLICY auditoria_insertar  ON auditoria FOR INSERT WITH CHECK (
    grupo_id IS NULL OR grupo_id = app_grupo() OR app_rol() = 'operacion');
-- El relevo no fija app.grupo_id: registra su apertura en el grupo de su acceso
CREATE POLICY auditoria_relevo    ON auditoria FOR INSERT WITH CHECK (
    app_rol() = 'relevo' AND actor_tipo = 'relevo' AND EXISTS (
        SELECT 1 FROM acceso_relevo a WHERE a.id = app_acceso_relevo() AND a.grupo_id = auditoria.grupo_id));

CREATE POLICY idempotencia_familia ON idempotencia FOR ALL USING (grupo_id = app_grupo());
