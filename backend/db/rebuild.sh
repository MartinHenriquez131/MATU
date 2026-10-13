#!/usr/bin/env bash
# Reconstruye la base de pruebas desde cero y aplica el esquema completo
set -euo pipefail
P="psql -h ${PGHOST:-/tmp} -p ${PGPORT:-5433} -v ON_ERROR_STOP=1 -q"
$P -U postgres -c "DROP DATABASE IF EXISTS matu" -c "DROP ROLE IF EXISTS matu_owner, matu_app, matu_publisher, matu_scheduler"
$P -U postgres -f 00_roles.sql
$P -U postgres -c "CREATE DATABASE matu OWNER matu_owner"
$P -U postgres -d matu -c "CREATE EXTENSION btree_gist; ALTER SCHEMA public OWNER TO matu_owner"
for f in 01_esquema.sql 02_rls.sql 03_permisos.sql; do $P -U matu_owner -d matu -f "$f"; done
echo "esquema aplicado"
