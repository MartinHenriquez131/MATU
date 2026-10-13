-- =============================================================================
-- MATU · Esquema de base de datos · versión 1.0
-- PostgreSQL 16 · se ejecuta como matu_owner (primera migración de Alembic)
--
-- Convenciones
--   * Claves primarias UUID (gen_random_uuid), salvo tablas de registro con BIGINT.
--   * Dinero en BIGINT, pesos chilenos enteros. Nunca NUMERIC ni coma flotante.
--   * Porcentajes en puntos base (bp): 1500 bp = 15%. Enteros, sin decimales.
--   * Fechas con zona (timestamptz). Fechas de calendario en date.
--   * Enumerados como TEXT + CHECK, no CREATE TYPE: agregar un valor es una
--     migración trivial y reversible, lo que un ENUM de PostgreSQL no permite.
--   * Toda raíz de agregado lleva grupo_id (o comercio_id). Las hijas heredan.
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS btree_gist;   -- EXCLUDE sobre rangos (convenios, liquidaciones)

-- -----------------------------------------------------------------------------
-- Contexto de sesión. Cada petición y cada job los fija con set_config(..., true)
-- -----------------------------------------------------------------------------
CREATE FUNCTION app_usuario()  RETURNS uuid LANGUAGE sql STABLE AS
$$ SELECT nullif(current_setting('app.usuario_id', true), '')::uuid $$;
CREATE FUNCTION app_grupo()    RETURNS uuid LANGUAGE sql STABLE AS
$$ SELECT nullif(current_setting('app.grupo_id', true), '')::uuid $$;
CREATE FUNCTION app_comercio() RETURNS uuid LANGUAGE sql STABLE AS
$$ SELECT nullif(current_setting('app.comercio_id', true), '')::uuid $$;
CREATE FUNCTION app_repartidor() RETURNS uuid LANGUAGE sql STABLE AS
$$ SELECT nullif(current_setting('app.repartidor_id', true), '')::uuid $$;
CREATE FUNCTION app_acceso_relevo() RETURNS uuid LANGUAGE sql STABLE AS
$$ SELECT nullif(current_setting('app.acceso_relevo_id', true), '')::uuid $$;
CREATE FUNCTION app_rol()      RETURNS text LANGUAGE sql STABLE AS
$$ SELECT coalesce(nullif(current_setting('app.rol', true), ''), 'ninguno') $$;

-- El outbox es transversal a tenants: su payload no puede llevar datos, solo UUID
CREATE FUNCTION payload_solo_identificadores(p jsonb) RETURNS boolean LANGUAGE sql IMMUTABLE AS
$$ SELECT jsonb_typeof(p) = 'object' AND NOT EXISTS (
       SELECT 1 FROM jsonb_each(p) e
       WHERE jsonb_typeof(e.value) <> 'string'
          OR e.value #>> '{}' !~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$') $$;

CREATE FUNCTION fijar_actualizado_en() RETURNS trigger LANGUAGE plpgsql AS
$$ BEGIN NEW.actualizado_en := now(); RETURN NEW; END $$;

CREATE FUNCTION rechazar_modificacion() RETURNS trigger LANGUAGE plpgsql AS
$$ BEGIN RAISE EXCEPTION 'la tabla % es de solo inserción', TG_TABLE_NAME
     USING ERRCODE = 'insufficient_privilege'; END $$;

-- =============================================================================
-- iam · identidad, sesiones y dispositivos
-- =============================================================================
CREATE TABLE usuario (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    email              text NOT NULL,
    telefono           text,
    nombre             text NOT NULL,
    password_hash      text NOT NULL,                       -- Argon2id
    mfa_secreto_cifrado bytea,                              -- obligatorio para operación
    es_operacion       boolean NOT NULL DEFAULT false,
    estado             text NOT NULL DEFAULT 'activo'
                       CHECK (estado IN ('activo', 'bloqueado', 'eliminado')),
    email_verificado_en timestamptz,
    creado_en          timestamptz NOT NULL DEFAULT now(),
    actualizado_en     timestamptz NOT NULL DEFAULT now(),
    eliminado_en       timestamptz,
    CONSTRAINT usuario_operacion_mfa CHECK (NOT es_operacion OR mfa_secreto_cifrado IS NOT NULL)
);
CREATE UNIQUE INDEX usuario_email_uq ON usuario (lower(email)) WHERE eliminado_en IS NULL;

-- Índice de credenciales. Resuelve email -> usuario ANTES de existir contexto.
-- Sin RLS, sin dato personal en claro: guarda HMAC-SHA256(pepper, email normalizado).
-- El pepper vive en la custodia de secretos, fuera de la base: sin él, el hash no se
-- puede revertir con un diccionario de emails.
CREATE TABLE indice_credencial (
    email_hash  bytea PRIMARY KEY CHECK (octet_length(email_hash) = 32),
    usuario_id  uuid NOT NULL UNIQUE REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE dispositivo (
    id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id    uuid NOT NULL REFERENCES usuario(id),
    plataforma    text NOT NULL CHECK (plataforma IN ('android', 'ios', 'web')),
    nombre        text,
    push_token    text,
    creado_en     timestamptz NOT NULL DEFAULT now(),
    ultimo_uso_en timestamptz,
    revocado_en   timestamptz
);
CREATE INDEX dispositivo_usuario_ix ON dispositivo (usuario_id) WHERE revocado_en IS NULL;

-- Refresh token rotativo con detección de reutilización (sección 11.6).
-- Todos los tokens de una misma cadena comparten familia_id: si se presenta uno
-- ya usado, se revoca la familia completa.
CREATE TABLE sesion_refresh (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id        uuid NOT NULL REFERENCES usuario(id),
    dispositivo_id    uuid NOT NULL REFERENCES dispositivo(id),
    familia_id        uuid NOT NULL,
    token_hash        bytea NOT NULL UNIQUE CHECK (octet_length(token_hash) = 32),
    emitido_en        timestamptz NOT NULL DEFAULT now(),
    expira_en         timestamptz NOT NULL,
    usado_en          timestamptz,
    revocado_en       timestamptz,
    motivo_revocacion text CHECK (motivo_revocacion IN ('logout', 'reutilizacion', 'cambio_clave', 'operacion')),
    CONSTRAINT sesion_refresh_vigencia CHECK (expira_en > emitido_en AND expira_en <= emitido_en + interval '30 days')
);
CREATE INDEX sesion_refresh_familia_ix ON sesion_refresh (familia_id);

-- Índice de tokens. Traduce token_hash -> tenant para los endpoints públicos
-- (vista de relevo, invitaciones, retorno de pasarela, refresh). Sin RLS, sin dato sensible.
CREATE TABLE indice_token (
    token_hash    bytea PRIMARY KEY CHECK (octet_length(token_hash) = 32),
    tipo          text NOT NULL CHECK (tipo IN ('relevo', 'invitacion', 'pago_retorno', 'refresh')),
    grupo_id      uuid,
    usuario_id    uuid,
    referencia_id uuid NOT NULL,           -- acceso_relevo.id, invitacion.id, transaccion.id o sesion.id
    expira_en     timestamptz NOT NULL,
    creado_en     timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT indice_token_tenant CHECK (grupo_id IS NOT NULL OR usuario_id IS NOT NULL)
);
CREATE INDEX indice_token_expira_ix ON indice_token (expira_en);

-- =============================================================================
-- care_circle · grupo familiar, membresías, persona cuidada, direcciones
-- =============================================================================
CREATE TABLE grupo_familiar (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre         text NOT NULL,
    estado         text NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo', 'archivado')),
    creado_por     uuid NOT NULL REFERENCES usuario(id),
    creado_en      timestamptz NOT NULL DEFAULT now(),
    actualizado_en timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE membresia (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id       uuid NOT NULL REFERENCES grupo_familiar(id),
    usuario_id     uuid NOT NULL REFERENCES usuario(id),
    rol            text NOT NULL CHECK (rol IN ('admin', 'cuidador', 'pagador', 'observador')),
    puede_ver_plan boolean NOT NULL DEFAULT false,   -- permiso explícito para 'pagador'
    estado         text NOT NULL DEFAULT 'activa' CHECK (estado IN ('activa', 'suspendida', 'retirada')),
    invitado_por   uuid REFERENCES usuario(id),
    unido_en       timestamptz NOT NULL DEFAULT now(),
    retirado_en    timestamptz,
    CONSTRAINT membresia_uq UNIQUE (grupo_id, usuario_id),
    CONSTRAINT membresia_permiso_plan CHECK (NOT puede_ver_plan OR rol = 'pagador')
);
CREATE INDEX membresia_usuario_ix ON membresia (usuario_id) WHERE estado = 'activa';

CREATE TABLE invitacion (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id       uuid NOT NULL REFERENCES grupo_familiar(id),
    destino_email  text,
    destino_telefono text,
    rol            text NOT NULL CHECK (rol IN ('admin', 'cuidador', 'pagador', 'observador')),
    token_hash     bytea NOT NULL UNIQUE,
    invitado_por   uuid NOT NULL REFERENCES usuario(id),
    creada_en      timestamptz NOT NULL DEFAULT now(),
    expira_en      timestamptz NOT NULL,
    aceptada_en    timestamptz,
    aceptada_por   uuid REFERENCES usuario(id),
    revocada_en    timestamptz,
    CONSTRAINT invitacion_destino CHECK (destino_email IS NOT NULL OR destino_telefono IS NOT NULL),
    CONSTRAINT invitacion_vigencia CHECK (expira_en <= creada_en + interval '7 days')
);

CREATE TABLE direccion (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id    uuid NOT NULL REFERENCES grupo_familiar(id),
    etiqueta    text NOT NULL DEFAULT 'Casa',
    calle       text NOT NULL,
    numero      text NOT NULL,
    depto       text,
    comuna      text NOT NULL,
    region      text NOT NULL DEFAULT 'Metropolitana',
    referencia  text,
    lat         numeric(9,6) CHECK (lat BETWEEN -90 AND 90),
    lng         numeric(9,6) CHECK (lng BETWEEN -180 AND 180),
    creado_en   timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX direccion_grupo_ix ON direccion (grupo_id);

-- La persona cuidada NO tiene diagnóstico (sección 11.3). nivel_apoyo es operacional.
CREATE TABLE persona_cuidada (
    id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id             uuid NOT NULL REFERENCES grupo_familiar(id),
    nombre               text NOT NULL,
    nombre_pila          text NOT NULL,
    nivel_apoyo          text NOT NULL CHECK (nivel_apoyo IN
                         ('autovalente_con_supervision', 'apoyo_parcial', 'apoyo_total')),
    direccion_entrega_id uuid REFERENCES direccion(id),
    activa               boolean NOT NULL DEFAULT true,
    creado_en            timestamptz NOT NULL DEFAULT now(),
    actualizado_en       timestamptz NOT NULL DEFAULT now(),
    eliminado_en         timestamptz
);
CREATE INDEX persona_cuidada_grupo_ix ON persona_cuidada (grupo_id);

-- =============================================================================
-- Consentimiento · Ley 21.719 (sección 11.5)
-- =============================================================================
CREATE TABLE consentimiento (
    id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id             uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id   uuid NOT NULL REFERENCES persona_cuidada(id),
    usuario_id           uuid NOT NULL REFERENCES usuario(id),
    calidad_otorgante    text NOT NULL CHECK (calidad_otorgante IN
                         ('titular', 'representante_legal', 'cuidador_de_hecho')),
    finalidad            text NOT NULL CHECK (finalidad IN
                         ('plan_cuidado', 'consumo', 'despacho', 'comunicaciones')),
    version_politica     text NOT NULL,
    evidencia            jsonb NOT NULL,      -- texto aceptado, ip, agente, momento
    referencia_documento text,                -- solo la referencia, nunca el documento
    otorgado_en          timestamptz NOT NULL DEFAULT now(),
    revision_vence_en    timestamptz,         -- recordatorio anual del cuidador de hecho
    revocado_en          timestamptz,
    CONSTRAINT consentimiento_representante CHECK
        (calidad_otorgante <> 'representante_legal' OR referencia_documento IS NOT NULL),
    CONSTRAINT consentimiento_revision CHECK
        (calidad_otorgante <> 'cuidador_de_hecho' OR revision_vence_en IS NOT NULL)
);
-- Un solo consentimiento vigente por persona y finalidad
CREATE UNIQUE INDEX consentimiento_vigente_uq ON consentimiento (persona_cuidada_id, finalidad)
    WHERE revocado_en IS NULL;

-- =============================================================================
-- care_plan · CAPA 1 · plan de cuidado, cifrado y relevo
-- =============================================================================

-- Clave de datos por persona cuidada, cifrada con la KEK (ADR-014 y ADR-016).
-- Lleva grupo_id propio y SOLO la política de familia: operación nunca la alcanza
-- (defecto 2 de la sección 12.8).
CREATE TABLE clave_datos (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id            uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id  uuid NOT NULL UNIQUE REFERENCES persona_cuidada(id),
    dek_cifrada_con_kek bytea,
    kek_version         integer NOT NULL CHECK (kek_version > 0),
    creada_en           timestamptz NOT NULL DEFAULT now(),
    rotada_en           timestamptz,
    destruida_en        timestamptz,
    -- Borrado criptográfico: sin clave no hay lectura, y no se regenera en silencio
    -- (defecto 5 de la sección 12.8).
    CONSTRAINT clave_datos_destruccion CHECK ((dek_cifrada_con_kek IS NULL) = (destruida_en IS NOT NULL))
);

-- modo: 'ficha_relevo' es el modo del MVP tras el cierre del ADR-023.
-- 'completo' queda disponible sin migración.
CREATE TABLE plan_cuidado (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id           uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id uuid NOT NULL UNIQUE REFERENCES persona_cuidada(id),
    modo               text NOT NULL DEFAULT 'ficha_relevo' CHECK (modo IN ('ficha_relevo', 'completo')),
    completitud_pct    smallint NOT NULL DEFAULT 0 CHECK (completitud_pct BETWEEN 0 AND 100),
    actualizado_por    uuid REFERENCES usuario(id),
    creado_en          timestamptz NOT NULL DEFAULT now(),
    actualizado_en     timestamptz NOT NULL DEFAULT now()
);

-- Cifrado por sección con AES-256-GCM. Nonce aleatorio de 96 bits por escritura.
-- AAD = plan_id || tipo: mover un texto cifrado a otra sección o a otro plan falla al descifrar.
-- La ficha de relevo usa tres tipos: rutina, manejo_situaciones y red_apoyo.
CREATE TABLE plan_seccion (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    plan_id           uuid NOT NULL REFERENCES plan_cuidado(id) ON DELETE CASCADE,
    tipo              text NOT NULL CHECK (tipo IN ('rutina', 'horarios', 'manejo_situaciones',
                      'preferencias', 'actividades', 'red_apoyo', 'alimentacion', 'movilidad')),
    contenido_cifrado bytea NOT NULL,
    nonce             bytea NOT NULL CHECK (octet_length(nonce) = 12),
    tag_auth          bytea NOT NULL CHECK (octet_length(tag_auth) = 16),
    kek_version       integer NOT NULL,
    version           integer NOT NULL DEFAULT 1 CHECK (version > 0),   -- ETag, bloqueo optimista
    actualizado_por   uuid REFERENCES usuario(id),
    actualizado_en    timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT plan_seccion_uq UNIQUE (plan_id, tipo)
);
-- Un nonce nunca se repite: repetirlo en AES-GCM rompe la autenticación.
CREATE UNIQUE INDEX plan_seccion_nonce_uq ON plan_seccion (nonce);

-- Lleva grupo_id propio aunque es hija de plan_cuidado: heredar crearía un ciclo
-- de políticas (plan_cuidado -> acceso_relevo -> plan_cuidado) que PostgreSQL rechaza.
CREATE TABLE acceso_relevo (
    id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id             uuid NOT NULL REFERENCES grupo_familiar(id),
    plan_id              uuid NOT NULL REFERENCES plan_cuidado(id) ON DELETE CASCADE,
    otorgado_por         uuid NOT NULL REFERENCES usuario(id),
    otorgado_a_nombre    text NOT NULL,
    otorgado_a_telefono  text NOT NULL,
    nombre_pila_persona  text NOT NULL,   -- lo único de la persona cuidada que ve el relevo
    secciones_permitidas text[] NOT NULL CHECK (
        cardinality(secciones_permitidas) > 0 AND
        secciones_permitidas <@ ARRAY['rutina','horarios','manejo_situaciones','preferencias',
                                      'actividades','red_apoyo','alimentacion','movilidad']),
    motivo               text NOT NULL,
    token_hash           bytea NOT NULL UNIQUE CHECK (octet_length(token_hash) = 32),
    pin_hash             text NOT NULL,
    pin_intentos_fallidos smallint NOT NULL DEFAULT 0 CHECK (pin_intentos_fallidos BETWEEN 0 AND 5),
    creado_en            timestamptz NOT NULL DEFAULT now(),
    expira_en            timestamptz NOT NULL,
    revocado_en          timestamptz,
    usos                 integer NOT NULL DEFAULT 0,
    ultimo_uso_en        timestamptz,
    CONSTRAINT acceso_relevo_vigencia CHECK
        (expira_en > creado_en AND expira_en <= creado_en + interval '30 days')
);
CREATE INDEX acceso_relevo_plan_ix ON acceso_relevo (plan_id) WHERE revocado_en IS NULL;

-- =============================================================================
-- catalog · categorías, productos, comercios, convenios y ofertas
-- =============================================================================
CREATE TABLE categoria_cuidado (
    id      uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    nombre  text NOT NULL UNIQUE,
    orden   smallint NOT NULL DEFAULT 0,
    activa  boolean NOT NULL DEFAULT true
);

CREATE TABLE producto (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    categoria_id        uuid NOT NULL REFERENCES categoria_cuidado(id),
    nombre              text NOT NULL,
    marca               text,
    presentacion        text NOT NULL,                    -- "Pañal adulto talla M x30"
    unidad              text NOT NULL CHECK (unidad IN ('unidad', 'sobre', 'ml', 'g')),
    unidades_por_envase integer NOT NULL CHECK (unidades_por_envase > 0),
    requiere_receta     boolean NOT NULL DEFAULT false,
    activo              boolean NOT NULL DEFAULT true,
    creado_en           timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX producto_categoria_ix ON producto (categoria_id) WHERE activo;

CREATE TABLE comercio (
    id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    razon_social    text NOT NULL,
    nombre_fantasia text NOT NULL,
    rut             text NOT NULL UNIQUE,
    direccion       text NOT NULL,
    comuna          text NOT NULL,
    telefono        text,
    estado          text NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo', 'suspendido', 'baja')),
    creado_en       timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE usuario_comercio (
    usuario_id  uuid NOT NULL REFERENCES usuario(id),
    comercio_id uuid NOT NULL REFERENCES comercio(id),
    rol         text NOT NULL DEFAULT 'encargado' CHECK (rol IN ('encargado', 'administrador')),
    activo      boolean NOT NULL DEFAULT true,
    PRIMARY KEY (usuario_id, comercio_id)
);

CREATE TABLE convenio (
    id                   uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    comercio_id          uuid NOT NULL REFERENCES comercio(id),
    vigencia             daterange NOT NULL,
    comision_bp          integer NOT NULL CHECK (comision_bp BETWEEN 0 AND 5000),
    tarifa_despacho      bigint NOT NULL CHECK (tarifa_despacho >= 0),
    prepara_pedidos      boolean NOT NULL DEFAULT true,
    cuenta_corriente     boolean NOT NULL DEFAULT true,
    periodo_liquidacion  text NOT NULL DEFAULT 'quincenal'
                         CHECK (periodo_liquidacion IN ('semanal', 'quincenal', 'mensual')),
    estado               text NOT NULL DEFAULT 'vigente' CHECK (estado IN ('borrador', 'vigente', 'terminado')),
    creado_en            timestamptz NOT NULL DEFAULT now(),
    -- Un comercio no tiene dos convenios vigentes que se traslapen
    CONSTRAINT convenio_sin_traslape EXCLUDE USING gist
        (comercio_id WITH =, vigencia WITH &&) WHERE (estado = 'vigente')
);

CREATE TABLE oferta (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    producto_id       uuid NOT NULL REFERENCES producto(id),
    comercio_id       uuid NOT NULL REFERENCES comercio(id),
    precio_referencia bigint NOT NULL CHECK (precio_referencia > 0),   -- referencial, ADR-011
    disponible        boolean NOT NULL DEFAULT true,
    actualizado_en    timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT oferta_uq UNIQUE (producto_id, comercio_id)
);

-- =============================================================================
-- consumption · CAPA 2 · perfil de consumo, reposiciones y alertas
-- =============================================================================

-- La tasa se guarda como fracción entera: tasa_unidades cada tasa_dias.
-- "4 al día" = 4/1, "1 cada 5 días" = 1/5. Sin coma flotante, igual que el dinero.
-- dias_cobertura = floor(stock_unidades * tasa_dias / tasa_unidades)
CREATE TABLE perfil_consumo (
    id                     uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id               uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id     uuid NOT NULL REFERENCES persona_cuidada(id),
    producto_id            uuid REFERENCES producto(id),
    nombre_libre           text,               -- producto fuera del catálogo (ADR-002)
    unidad                 text NOT NULL DEFAULT 'unidad' CHECK (unidad IN ('unidad', 'sobre', 'ml', 'g')),
    tasa_unidades          integer NOT NULL CHECK (tasa_unidades > 0),
    tasa_dias              integer NOT NULL DEFAULT 1 CHECK (tasa_dias BETWEEN 1 AND 90),
    stock_unidades         integer NOT NULL CHECK (stock_unidades >= 0),
    stock_medido_en        date NOT NULL,      -- ancla del cálculo, no la última reposición
    fecha_quiebre_estimada date NOT NULL,      -- materializada (decisión 7.6 e)
    dias_aviso             smallint NOT NULL DEFAULT 7 CHECK (dias_aviso BETWEEN 0 AND 60),
    activo                 boolean NOT NULL DEFAULT true,
    creado_en              timestamptz NOT NULL DEFAULT now(),
    actualizado_en         timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT perfil_consumo_producto CHECK (producto_id IS NOT NULL OR nombre_libre IS NOT NULL),
    CONSTRAINT perfil_consumo_quiebre CHECK (fecha_quiebre_estimada >= stock_medido_en)
);
CREATE UNIQUE INDEX perfil_consumo_producto_uq ON perfil_consumo (persona_cuidada_id, producto_id)
    WHERE producto_id IS NOT NULL AND activo;
-- La consulta más frecuente de la aplicación: qué se está por acabar
CREATE INDEX perfil_consumo_quiebre_ix ON perfil_consumo (grupo_id, fecha_quiebre_estimada) WHERE activo;

CREATE TABLE reposicion (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    perfil_id         uuid NOT NULL REFERENCES perfil_consumo(id) ON DELETE CASCADE,
    cantidad_unidades integer NOT NULL CHECK (cantidad_unidades > 0),
    origen            text NOT NULL CHECK (origen IN ('pedido_matu', 'declarada')),
    pedido_ref        uuid,      -- referencia opaca SIN clave foránea: la capa 2 no depende de la 3
    ocurrida_en       date NOT NULL,
    registrada_por    uuid REFERENCES usuario(id),
    registrada_en     timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT reposicion_origen CHECK ((origen = 'pedido_matu') = (pedido_ref IS NOT NULL))
);
CREATE INDEX reposicion_perfil_ix ON reposicion (perfil_id, ocurrida_en DESC);

CREATE TABLE alerta_quiebre (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    perfil_id      uuid NOT NULL REFERENCES perfil_consumo(id) ON DELETE CASCADE,
    fecha_prevista date NOT NULL,
    estado         text NOT NULL DEFAULT 'pendiente'
                   CHECK (estado IN ('pendiente', 'notificada', 'resuelta', 'descartada')),
    creada_en      timestamptz NOT NULL DEFAULT now(),
    notificada_en  timestamptz,
    cerrada_en     timestamptz,
    CONSTRAINT alerta_quiebre_uq UNIQUE (perfil_id, fecha_prevista)   -- idempotencia del job
);
CREATE INDEX alerta_quiebre_pendiente_ix ON alerta_quiebre (perfil_id) WHERE estado IN ('pendiente', 'notificada');

-- =============================================================================
-- ordering · pedido, líneas, sustitución e historial de estados
-- =============================================================================
CREATE TABLE pedido (
    id                      uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id                uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id      uuid NOT NULL REFERENCES persona_cuidada(id),
    comercio_id             uuid NOT NULL REFERENCES comercio(id),
    estado                  text NOT NULL DEFAULT 'borrador' CHECK (estado IN (
        'borrador', 'pendiente_recaudacion', 'autorizado', 'expirado', 'enviado_a_comercio',
        'preparando', 'requiere_decision', 'listo_retiro', 'asignado', 'sin_repartidor',
        'retirado', 'en_ruta', 'entregado', 'no_entregado', 'reprogramado',
        'captura_pendiente', 'incobrable', 'cerrado', 'cancelado', 'cancelado_con_devolucion')),
    modo_cumplimiento       text NOT NULL DEFAULT 'preparado' CHECK (modo_cumplimiento IN ('preparado', 'picking')),
    origen                  text NOT NULL DEFAULT 'manual' CHECK (origen IN ('manual', 'reposicion', 'alerta_quiebre')),
    ventana_entrega         tstzrange,
    total_estimado          bigint NOT NULL DEFAULT 0 CHECK (total_estimado >= 0),
    total_autorizado        bigint CHECK (total_autorizado >= 0),
    total_real              bigint CHECK (total_real >= 0),
    destinatario_nombre_pila text NOT NULL,     -- lo único de la persona que ve el comercio
    codigo_retiro_hash      text,
    codigo_retiro_expira_en timestamptz,
    codigo_retiro_usado_en  timestamptz,
    editable_hasta          timestamptz,        -- ventana de 24 h de la reposición (RF-19)
    creado_por              uuid NOT NULL REFERENCES usuario(id),
    creado_en               timestamptz NOT NULL DEFAULT now(),
    actualizado_en          timestamptz NOT NULL DEFAULT now(),
    version                 integer NOT NULL DEFAULT 1
);
CREATE INDEX pedido_grupo_ix ON pedido (grupo_id, creado_en DESC);
CREATE INDEX pedido_comercio_dia_ix ON pedido (comercio_id, estado, creado_en)
    WHERE estado NOT IN ('borrador', 'cerrado', 'cancelado', 'expirado');

-- Dirección de entrega congelada. Tabla aparte porque el comercio ve el pedido
-- pero NUNCA la dirección (sección 11.2), y RLS filtra filas, no columnas.
CREATE TABLE pedido_entrega (
    pedido_id         uuid PRIMARY KEY REFERENCES pedido(id) ON DELETE CASCADE,
    calle             text NOT NULL,
    numero            text NOT NULL,
    depto             text,
    comuna            text NOT NULL,
    referencia        text,
    lat               numeric(9,6),
    lng               numeric(9,6),
    telefono_contacto text NOT NULL
);

CREATE TABLE pedido_linea (
    id                    uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id             uuid NOT NULL REFERENCES pedido(id) ON DELETE CASCADE,
    oferta_id             uuid NOT NULL REFERENCES oferta(id),
    producto_id           uuid NOT NULL REFERENCES producto(id),
    cantidad              integer NOT NULL CHECK (cantidad > 0),
    precio_snapshot       bigint NOT NULL CHECK (precio_snapshot > 0),   -- al confirmar
    precio_real           bigint CHECK (precio_real >= 0),              -- al preparar
    estado_linea          text NOT NULL DEFAULT 'pendiente' CHECK (estado_linea IN
                          ('pendiente', 'preparada', 'faltante', 'requiere_decision', 'sustituida', 'eliminada')),
    sustituto_de_linea_id uuid REFERENCES pedido_linea(id),   -- la sustitución es una línea nueva
    creado_en             timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pedido_linea_no_autosustituye CHECK (sustituto_de_linea_id IS DISTINCT FROM id)
);
CREATE INDEX pedido_linea_pedido_ix ON pedido_linea (pedido_id);

CREATE TABLE regla_sustitucion (
    id                    uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id             uuid NOT NULL REFERENCES pedido(id) ON DELETE CASCADE,
    producto_id           uuid NOT NULL REFERENCES producto(id),
    accion                text NOT NULL CHECK (accion IN
                          ('equivalente', 'producto_especifico', 'no_sustituir', 'consultar')),
    producto_sustituto_id uuid REFERENCES producto(id),
    precio_maximo         bigint CHECK (precio_maximo > 0),
    CONSTRAINT regla_sustitucion_uq UNIQUE (pedido_id, producto_id),
    CONSTRAINT regla_sustitucion_especifico CHECK
        ((accion = 'producto_especifico') = (producto_sustituto_id IS NOT NULL))
);

-- Línea de tiempo del pedido (atributo de calidad 6: observabilidad). Solo inserción.
CREATE TABLE pedido_transicion (
    id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pedido_id   uuid NOT NULL REFERENCES pedido(id),
    desde       text,
    hacia       text NOT NULL,
    actor_tipo  text NOT NULL CHECK (actor_tipo IN ('usuario', 'comercio', 'repartidor', 'operacion', 'sistema')),
    actor_ref   uuid,
    motivo      text,
    ocurrido_en timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX pedido_transicion_pedido_ix ON pedido_transicion (pedido_id, ocurrido_en);

-- =============================================================================
-- replenishment · planes de reposición y ocurrencias materializadas
-- =============================================================================
CREATE TABLE plan_reposicion (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id           uuid NOT NULL REFERENCES grupo_familiar(id),
    persona_cuidada_id uuid NOT NULL REFERENCES persona_cuidada(id),
    comercio_id        uuid NOT NULL REFERENCES comercio(id),
    frecuencia_dias    smallint NOT NULL CHECK (frecuencia_dias IN (7, 14, 21, 28, 30)),
    proxima_fecha      date NOT NULL,
    estado             text NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo', 'pausado', 'cancelado')),
    creado_por         uuid NOT NULL REFERENCES usuario(id),
    creado_en          timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE plan_reposicion_linea (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    plan_reposicion_id uuid NOT NULL REFERENCES plan_reposicion(id) ON DELETE CASCADE,
    producto_id        uuid NOT NULL REFERENCES producto(id),
    perfil_consumo_id  uuid REFERENCES perfil_consumo(id),   -- propuesta desde el consumo (8.9)
    cantidad_envases   integer NOT NULL CHECK (cantidad_envases > 0),
    CONSTRAINT plan_reposicion_linea_uq UNIQUE (plan_reposicion_id, producto_id)
);

CREATE TABLE ocurrencia (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    plan_reposicion_id uuid NOT NULL REFERENCES plan_reposicion(id) ON DELETE CASCADE,
    fecha_programada   date NOT NULL,
    estado             text NOT NULL DEFAULT 'programada' CHECK (estado IN
                       ('programada', 'generada', 'saltada', 'cancelada', 'fallida')),
    pedido_id          uuid REFERENCES pedido(id),
    creada_en          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT ocurrencia_uq UNIQUE (plan_reposicion_id, fecha_programada),   -- ADR-012
    CONSTRAINT ocurrencia_generada CHECK ((estado = 'generada') = (pedido_id IS NOT NULL))
);

-- =============================================================================
-- payments · cargo, participaciones, transacciones y medios inscritos
-- =============================================================================
CREATE TABLE cargo (
    id                    uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id             uuid NOT NULL UNIQUE REFERENCES pedido(id),
    monto_objetivo        bigint NOT NULL CHECK (monto_objetivo > 0),
    margen_bp             integer NOT NULL DEFAULT 1500 CHECK (margen_bp BETWEEN 0 AND 5000),
    monto_autorizado      bigint NOT NULL DEFAULT 0 CHECK (monto_autorizado >= 0),
    monto_capturado       bigint NOT NULL DEFAULT 0 CHECK (monto_capturado >= 0),
    estado                text NOT NULL DEFAULT 'creado' CHECK (estado IN ('creado', 'recaudando',
                          'redistribuyendo', 'completo', 'fallido', 'capturado', 'revertido', 'reembolsado_parcial')),
    recaudacion_expira_en timestamptz NOT NULL,
    respaldo_usuario_id   uuid REFERENCES usuario(id),
    creado_en             timestamptz NOT NULL DEFAULT now(),
    actualizado_en        timestamptz NOT NULL DEFAULT now(),
    version               integer NOT NULL DEFAULT 1,
    CONSTRAINT cargo_captura_tope CHECK (monto_capturado <= monto_autorizado)
);

CREATE TABLE participacion (
    id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    cargo_id           uuid NOT NULL REFERENCES cargo(id),
    usuario_id         uuid NOT NULL REFERENCES usuario(id),
    porcentaje_bp      integer NOT NULL CHECK (porcentaje_bp BETWEEN 1 AND 10000),
    monto_comprometido bigint NOT NULL CHECK (monto_comprometido > 0),
    monto_autorizado   bigint NOT NULL DEFAULT 0 CHECK (monto_autorizado >= 0),
    monto_capturado    bigint NOT NULL DEFAULT 0 CHECK (monto_capturado >= 0),
    estado             text NOT NULL DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'autorizando',
                       'autorizada', 'rechazada', 'vencida', 'capturada', 'revertida')),
    es_respaldo        boolean NOT NULL DEFAULT false,
    CONSTRAINT participacion_uq UNIQUE (cargo_id, usuario_id),
    CONSTRAINT participacion_captura_tope CHECK (monto_capturado <= monto_autorizado)
);
CREATE UNIQUE INDEX participacion_un_respaldo_uq ON participacion (cargo_id) WHERE es_respaldo;

-- Registro contable. Nunca se borra. Cada operación es una fila nueva.
CREATE TABLE transaccion_pasarela (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    participacion_id    uuid NOT NULL REFERENCES participacion(id),
    proveedor           text NOT NULL CHECK (proveedor IN ('webpay_plus', 'oneclick')),
    tipo                text NOT NULL CHECK (tipo IN ('autorizacion', 'ampliacion', 'captura', 'reversa')),
    buy_order           text NOT NULL UNIQUE CHECK (length(buy_order) <= 26),   -- límite de Transbank
    token               text,
    monto               bigint NOT NULL CHECK (monto > 0),
    estado              text NOT NULL DEFAULT 'iniciada' CHECK (estado IN
                        ('iniciada', 'autorizando', 'aprobada', 'rechazada', 'error')),
    codigo_autorizacion text,
    tipo_tarjeta        text CHECK (tipo_tarjeta IN ('credito', 'debito', 'prepago')),
    ultimos4            char(4),
    payload_respuesta   jsonb,
    idempotency_key     text NOT NULL UNIQUE,
    creado_en           timestamptz NOT NULL DEFAULT now(),
    actualizado_en      timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX transaccion_participacion_ix ON transaccion_pasarela (participacion_id, creado_en);
-- Job de conciliación: transacciones colgadas en 'autorizando' (sección 8.4)
CREATE INDEX transaccion_colgada_ix ON transaccion_pasarela (creado_en) WHERE estado = 'autorizando';

-- Tarjeta inscrita con OneClick (ADR-007: entra al MVP por el respaldo)
CREATE TABLE medio_pago_inscrito (
    id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id       uuid NOT NULL REFERENCES usuario(id),
    proveedor        text NOT NULL DEFAULT 'oneclick' CHECK (proveedor = 'oneclick'),
    tbk_user_cifrado bytea NOT NULL,
    tipo_tarjeta     text NOT NULL CHECK (tipo_tarjeta IN ('credito', 'debito', 'prepago')),
    ultimos4         char(4) NOT NULL,
    inscrito_en      timestamptz NOT NULL DEFAULT now(),
    eliminado_en     timestamptz
);
CREATE INDEX medio_pago_usuario_ix ON medio_pago_inscrito (usuario_id) WHERE eliminado_en IS NULL;

-- =============================================================================
-- fulfillment · repartidores, ofertas en cascada, asignación y evidencia
-- (tablas de repartidor diseñadas y condicionadas: RF-27 a RF-30 son "Debería")
-- =============================================================================
CREATE TABLE repartidor (
    id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id        uuid NOT NULL UNIQUE REFERENCES usuario(id),
    vehiculo          text NOT NULL CHECK (vehiculo IN ('auto', 'moto', 'bicicleta')),
    comuna_base       text NOT NULL,
    tasa_aceptacion_bp integer NOT NULL DEFAULT 10000 CHECK (tasa_aceptacion_bp BETWEEN 0 AND 10000),
    estado            text NOT NULL DEFAULT 'activo' CHECK (estado IN ('activo', 'suspendido', 'baja')),
    creado_en         timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE oferta_asignacion (
    id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id     uuid NOT NULL REFERENCES pedido(id),
    repartidor_id uuid NOT NULL REFERENCES repartidor(id),
    orden_cascada smallint NOT NULL CHECK (orden_cascada > 0),
    ofrecido_en   timestamptz NOT NULL DEFAULT now(),
    expira_en     timestamptz NOT NULL,
    resultado     text NOT NULL DEFAULT 'pendiente' CHECK (resultado IN ('pendiente', 'aceptada', 'rechazada', 'vencida')),
    respondido_en timestamptz,
    CONSTRAINT oferta_asignacion_uq UNIQUE (pedido_id, orden_cascada)
);

-- Lleva grupo_id por la misma razón que acceso_relevo: pedido -> asignacion -> pedido
CREATE TABLE asignacion (
    id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    grupo_id      uuid NOT NULL REFERENCES grupo_familiar(id),
    pedido_id     uuid NOT NULL REFERENCES pedido(id),
    repartidor_id uuid NOT NULL REFERENCES repartidor(id),
    estado        text NOT NULL DEFAULT 'activa' CHECK (estado IN ('activa', 'completada', 'abandonada')),
    aceptada_en   timestamptz NOT NULL DEFAULT now(),
    retirado_en   timestamptz,
    entregado_en  timestamptz,
    abandonada_en timestamptz
);
CREATE UNIQUE INDEX asignacion_activa_uq ON asignacion (pedido_id) WHERE estado = 'activa';

-- Evidencia de boleta y de entrega. Se ata al pedido y no a la asignación, porque
-- en el MVP la registra el comercio desde su vista (recorte de la sección 15.3).
CREATE TABLE evidencia (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id           uuid NOT NULL REFERENCES pedido(id),
    tipo                text NOT NULL CHECK (tipo IN ('boleta', 'entrega')),
    objeto_clave        text NOT NULL,          -- ruta en el bucket privado
    sha256              bytea NOT NULL CHECK (octet_length(sha256) = 32),
    lat                 numeric(9,6),
    lng                 numeric(9,6),
    registrada_por_tipo text NOT NULL CHECK (registrada_por_tipo IN ('comercio', 'repartidor', 'operacion')),
    registrada_por      uuid NOT NULL,
    registrada_en       timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX evidencia_pedido_ix ON evidencia (pedido_id);

-- =============================================================================
-- settlement · lo que MATU debe al comercio
-- =============================================================================
CREATE TABLE liquidacion (
    id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    comercio_id    uuid NOT NULL REFERENCES comercio(id),
    periodo        daterange NOT NULL,
    monto_bruto    bigint NOT NULL DEFAULT 0 CHECK (monto_bruto >= 0),
    monto_comision bigint NOT NULL DEFAULT 0 CHECK (monto_comision >= 0),
    monto_neto     bigint NOT NULL DEFAULT 0,
    estado         text NOT NULL DEFAULT 'abierta' CHECK (estado IN ('abierta', 'cerrada', 'facturada', 'pagada')),
    factura_ref    text,
    cerrada_en     timestamptz,
    pagada_en      timestamptz,
    CONSTRAINT liquidacion_neto CHECK (monto_neto = monto_bruto - monto_comision),
    CONSTRAINT liquidacion_sin_traslape EXCLUDE USING gist (comercio_id WITH =, periodo WITH &&)
);

CREATE TABLE consumo_comercio (
    id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    comercio_id      uuid NOT NULL REFERENCES comercio(id),
    pedido_id        uuid NOT NULL UNIQUE REFERENCES pedido(id),
    monto_autorizado bigint NOT NULL CHECK (monto_autorizado >= 0),   -- el tope que vio el comercio
    monto_boleta     bigint NOT NULL CHECK (monto_boleta >= 0),
    folio_boleta     text NOT NULL,
    evidencia_id     uuid REFERENCES evidencia(id),
    estado           text NOT NULL DEFAULT 'pendiente' CHECK (estado IN
                     ('pendiente', 'conciliado', 'con_desviacion', 'disputado', 'liquidado')),
    desviacion_bp    integer NOT NULL DEFAULT 0,
    liquidacion_id   uuid REFERENCES liquidacion(id),
    creado_en        timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT consumo_liquidado CHECK ((estado = 'liquidado') = (liquidacion_id IS NOT NULL))
);
CREATE INDEX consumo_comercio_pendiente_ix ON consumo_comercio (comercio_id, estado) WHERE estado <> 'liquidado';

-- =============================================================================
-- notifications · preferencias y registro de envíos
-- (las plantillas viven en el código, versionadas con él)
-- =============================================================================
CREATE TABLE preferencia_notificacion (
    usuario_id     uuid NOT NULL REFERENCES usuario(id),
    tipo_evento    text NOT NULL,                 -- 'quiebre_proximo', 'pago_pendiente', ...
    canal          text NOT NULL CHECK (canal IN ('push', 'correo', 'sms')),
    activo         boolean NOT NULL DEFAULT true,
    silencio_desde time,
    silencio_hasta time,
    PRIMARY KEY (usuario_id, tipo_evento, canal)
);

-- Registro de envíos. Sin contenido: el mensaje se arma al enviar y no se guarda.
CREATE TABLE notificacion (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id  uuid NOT NULL REFERENCES usuario(id),
    grupo_id    uuid REFERENCES grupo_familiar(id),
    evento_id   bigint NOT NULL,                  -- evento_outbox.id que la originó
    canal       text NOT NULL CHECK (canal IN ('push', 'correo', 'sms')),
    plantilla   text NOT NULL,
    estado      text NOT NULL DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'enviada', 'fallida', 'omitida')),
    creada_en   timestamptz NOT NULL DEFAULT now(),
    enviada_en  timestamptz,
    error       text,
    CONSTRAINT notificacion_uq UNIQUE (evento_id, usuario_id, canal)   -- idempotencia del consumidor
);

-- =============================================================================
-- backoffice · incidencias
-- =============================================================================
CREATE TABLE incidencia (
    id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id   uuid NOT NULL REFERENCES pedido(id),
    tipo        text NOT NULL CHECK (tipo IN ('desviacion_monto', 'faltante', 'entrega_fallida',
                'captura_rechazada', 'reclamo_familia', 'otro')),
    descripcion text NOT NULL,
    estado      text NOT NULL DEFAULT 'abierta' CHECK (estado IN ('abierta', 'en_gestion', 'resuelta')),
    creada_por  uuid NOT NULL REFERENCES usuario(id),
    asignada_a  uuid REFERENCES usuario(id),
    resolucion  text,
    creada_en   timestamptz NOT NULL DEFAULT now(),
    resuelta_en timestamptz,
    CONSTRAINT incidencia_resuelta CHECK ((estado = 'resuelta') = (resuelta_en IS NOT NULL))
);
CREATE INDEX incidencia_abierta_ix ON incidencia (estado, creada_en) WHERE estado <> 'resuelta';

-- =============================================================================
-- shared · auditoría, outbox, idempotencia
-- =============================================================================

-- Solo inserción: sin UPDATE ni DELETE por permiso y por trigger.
CREATE TABLE auditoria (
    id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    grupo_id    uuid,
    actor_tipo  text NOT NULL CHECK (actor_tipo IN
                ('usuario', 'relevo', 'comercio', 'repartidor', 'operacion', 'sistema')),
    actor_ref   uuid,                      -- polimórfico: el relevo no es usuario
    accion      text NOT NULL,             -- 'plan.leer', 'plan.editar', 'relevo.abrir', ...
    entidad     text NOT NULL,
    entidad_id  uuid,
    motivo      text,
    ip          inet,
    request_id  text,
    ocurrido_en timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX auditoria_entidad_ix ON auditoria (entidad, entidad_id, ocurrido_en DESC);
CREATE INDEX auditoria_grupo_ix ON auditoria (grupo_id, ocurrido_en DESC);

-- Tabla de infraestructura SIN RLS. El payload lleva solo identificadores.
CREATE TABLE evento_outbox (
    id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    grupo_id     uuid,
    tipo         text NOT NULL,              -- 'QuiebreProximo', 'PedidoEntregado', ...
    agregado_tipo text NOT NULL,
    agregado_id  uuid NOT NULL,
    payload      jsonb NOT NULL DEFAULT '{}'::jsonb,
    creado_en    timestamptz NOT NULL DEFAULT now(),
    disponible_en timestamptz NOT NULL DEFAULT now(),
    intentos     smallint NOT NULL DEFAULT 0 CHECK (intentos BETWEEN 0 AND 8),
    publicado_en timestamptz,
    fallido_en   timestamptz,
    -- El payload solo admite identificadores: todo valor debe ser un UUID en texto
    CONSTRAINT evento_outbox_solo_ids CHECK (payload_solo_identificadores(payload))
);
CREATE INDEX evento_outbox_pendiente_ix ON evento_outbox (disponible_en)
    WHERE publicado_en IS NULL AND fallido_en IS NULL;

CREATE TABLE evento_consumido (
    evento_id    bigint NOT NULL,
    consumidor   text NOT NULL,
    consumido_en timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (evento_id, consumidor)
);

-- Guarda cuerpos de respuesta de pedidos y pagos: lleva grupo_id y RLS (defecto 4, sección 12.8)
CREATE TABLE idempotencia (
    grupo_id     uuid NOT NULL REFERENCES grupo_familiar(id),
    endpoint     text NOT NULL,
    clave        text NOT NULL,
    usuario_id   uuid NOT NULL REFERENCES usuario(id),
    hash_peticion bytea NOT NULL,           -- misma clave con otro cuerpo = 422
    estado_http  smallint,
    respuesta    jsonb,
    creada_en    timestamptz NOT NULL DEFAULT now(),
    expira_en    timestamptz NOT NULL DEFAULT now() + interval '24 hours',
    PRIMARY KEY (grupo_id, endpoint, clave)
);
CREATE INDEX idempotencia_expira_ix ON idempotencia (expira_en);

-- =============================================================================
-- Triggers
-- =============================================================================
CREATE TRIGGER usuario_actualizado        BEFORE UPDATE ON usuario        FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER grupo_actualizado          BEFORE UPDATE ON grupo_familiar FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER persona_actualizada        BEFORE UPDATE ON persona_cuidada FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER plan_actualizado           BEFORE UPDATE ON plan_cuidado   FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER perfil_actualizado         BEFORE UPDATE ON perfil_consumo FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER pedido_actualizado         BEFORE UPDATE ON pedido         FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER cargo_actualizado          BEFORE UPDATE ON cargo          FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();
CREATE TRIGGER transaccion_actualizada    BEFORE UPDATE ON transaccion_pasarela FOR EACH ROW EXECUTE FUNCTION fijar_actualizado_en();

CREATE TRIGGER auditoria_solo_insercion   BEFORE UPDATE OR DELETE ON auditoria            FOR EACH ROW EXECUTE FUNCTION rechazar_modificacion();
CREATE TRIGGER transicion_solo_insercion  BEFORE UPDATE OR DELETE ON pedido_transicion    FOR EACH ROW EXECUTE FUNCTION rechazar_modificacion();
CREATE TRIGGER transaccion_sin_borrado    BEFORE DELETE           ON transaccion_pasarela FOR EACH ROW EXECUTE FUNCTION rechazar_modificacion();
