-- MATU · Roles de base de datos
-- Se ejecuta una sola vez por ambiente, con un usuario administrador del servidor.
-- Ninguno de estos roles es SUPERUSER ni tiene BYPASSRLS.

-- Propietario del esquema. Solo lo usa Alembic para migrar.
CREATE ROLE matu_owner LOGIN NOSUPERUSER NOBYPASSRLS;

-- Rol de ejecución de la API y del worker. No es propietario de ninguna tabla,
-- por eso RLS lo alcanza siempre (sección 7.7, hecho 1).
CREATE ROLE matu_app LOGIN NOSUPERUSER NOBYPASSRLS;

-- Publicador del outbox. Transversal a tenants, con permiso solo sobre dos tablas.
CREATE ROLE matu_publisher LOGIN NOSUPERUSER NOBYPASSRLS;

-- Scheduler. Solo enumera grupos activos para encolar un job por grupo.
CREATE ROLE matu_scheduler LOGIN NOSUPERUSER NOBYPASSRLS;
