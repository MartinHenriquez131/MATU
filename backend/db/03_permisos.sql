-- =============================================================================
-- MATU · Permisos por rol · versión 1.0
-- Se ejecuta como matu_owner. RLS decide QUÉ FILAS. Estos permisos deciden
-- QUÉ OPERACIONES y sobre QUÉ TABLAS. Las dos capas se complementan.
-- =============================================================================

REVOKE ALL ON ALL TABLES    IN SCHEMA public FROM PUBLIC;
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO matu_app, matu_publisher, matu_scheduler;

-- -----------------------------------------------------------------------------
-- matu_app · API y worker
-- -----------------------------------------------------------------------------
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO matu_app;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO matu_app;

-- Registros de solo inserción
REVOKE UPDATE, DELETE ON auditoria, pedido_transicion FROM matu_app;
-- El registro contable de la pasarela no se borra
REVOKE DELETE ON transaccion_pasarela FROM matu_app;
-- El outbox lo escribe la API y lo lee solo el publicador
REVOKE SELECT, UPDATE, DELETE ON evento_outbox FROM matu_app;
REVOKE UPDATE, DELETE ON evento_consumido FROM matu_app;

-- -----------------------------------------------------------------------------
-- matu_publisher · SOLO outbox (sección 7.7, excepción a)
-- -----------------------------------------------------------------------------
GRANT SELECT, UPDATE ON evento_outbox    TO matu_publisher;
GRANT SELECT, INSERT ON evento_consumido TO matu_publisher;

-- -----------------------------------------------------------------------------
-- matu_scheduler · solo los identificadores de los grupos activos
-- -----------------------------------------------------------------------------
GRANT SELECT (id, estado) ON grupo_familiar TO matu_scheduler;

-- Tablas futuras: mismo criterio por defecto
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO matu_app;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE ON SEQUENCES TO matu_app;
