# Entorno de demostración · instructivo (MATU-64)

**Responsable:** Martín (despliegue, ADR-030) · **Revisa:** Jorge · **Creado:** 09-11-2026

La demo de MATU es un proyecto aparte de staging en Railway, con su propia base, su Redis y sus secretos. **Solo datos sintéticos.** Una prueba en staging no rompe la demo, y la demo nunca usa un secreto de staging.

## 1. Qué hay

| Dato | Valor |
|---|---|
| Proyecto de Railway | `matu-demo` (`7e4bcc17-6e4b-43a8-821a-64177c1df0b3`), entorno `demo`, región `sfo` |
| Dirección | `https://matu-api-demo.up.railway.app` |
| Servicios | `matu-api` (la API y la app), `Postgres` (16, `postgres-ssl:16`, con volumen), `Redis` (8.2, con volumen) y tres cron: `matu-cron-borrados` (`10 6,7 * * *`), `matu-cron-quiebres` (`30 7 * * *`) y `matu-cron-avisos` (`*/15 * * * *`) |
| `ENTORNO` | `staging`. La configuración solo admite la KEK sintética y el envío simulado con `local`, `pruebas` o `staging`, y la demo los necesita |
| Variables que no son secretas | Las mismas de staging (`infra/railway/README.md` del repositorio MATU_PROYECTO), con `ORIGEN_WEB` de la demo, `CAPA3_HABILITADA=true`, `REDIS_URL=${{Redis.REDIS_URL}}`, y `DATABASE_URL` y `MIGRATIONS_DATABASE_URL` armadas con referencias de Railway |
| Secretos (8) | `PEPPER_EMAIL`, `JWT_CLAVE`, `PEPPER_PIN`, `PEPPER_RECUPERACION`, `PEPPER_LIMITES`, `KEK_ENTORNO`, `MATU_OWNER_PASSWORD` y `MATU_APP_PASSWORD`. Se generaron en el computador de Martín y se cargaron directo en Railway (sección 4). Respaldo en su gestor de contraseñas. Nunca en el chat ni en el repositorio |
| Cron | Usan la misma imagen, con `restartPolicyType=NEVER`, y toman `DATABASE_URL`, `POLITICA_VERSION` y `ORIGEN_WEB` como referencia a `matu-api` |

## 2. Cuentas de la demo

Las crea la semilla, con la contraseña que se define al sembrar (`SEMILLA_CONTRASENA`, la conoce el equipo y no se escribe en ningún lado):

| Familia | Persona | Rol | Correo |
|---|---|---|---|
| Soto | Carmen Fuentes | admin | `carmen@example.com` |
| Soto | Luisa Contreras | cuidador | `luisa@example.org` |
| Soto | Rodrigo Soto | pagador, ve el plan | `rodrigo@example.com` |
| Soto | Javiera Soto | observador | `javiera@example.org` |
| Riquelme | Patricia Riquelme | admin | `patricia@example.com` |
| Riquelme | Tomás Riquelme | observador | `tomas@example.org` |

El relevo de ejemplo es «Rosa», de la Familia Soto. Su enlace y su PIN se ven solo en la terminal (sección 3, paso 5). **Nunca se pegan en un chat.**

## 3. Restablecer la demo (unos 2 segundos)

Antes de cada presentación, o cuando la demo quedó desordenada. Desde Git Bash, en la carpeta de MATU_PROYECTO:

1. Enlaza la terminal a la demo (una vez por computador). En Git Bash los menús de `railway link` no responden, así que se pasan los identificadores:
   ```
   railway link --project 7e4bcc17-6e4b-43a8-821a-64177c1df0b3 --environment demo --service matu-api
   ```
   `railway status` tiene que decir `matu-demo`. Si dice `valiant-tenderness`, es staging: no sigas.
2. Entra al contenedor de la API:
   ```
   railway ssh --service matu-api
   ```
3. Dentro, define la contraseña y el PIN sin mostrarlos. Escríbelos cuando la terminal quede esperando; no se ven:
   ```
   read -rs SEMILLA_CONTRASENA
   read -rs SEMILLA_PIN
   export SEMILLA_CONTRASENA SEMILLA_PIN
   ```
4. Restablece:
   ```
   time python /app/infra/semillas/demo.py --restablecer
   ```
   Tiene que terminar con «Listo para probar los recorridos 1 a 4…». Medido el 09-11: **2,0 s**.
5. Si necesitas el enlace del relevo de ejemplo, míralo y cópialo solo a tu gestor:
   ```
   cat /app/infra/semillas/salida/relevo-demo.txt
   ```
6. Borra las variables y sal:
   ```
   unset SEMILLA_CONTRASENA SEMILLA_PIN
   exit
   ```

**Por qué con `railway ssh` y no con `railway run`:** `railway run` corre la semilla con el Python del computador, que no tiene las dependencias del backend. Además la base de la demo está solo en la red privada de Railway. Dentro del contenedor están las dos cosas. Una sesión `ssh` no queda en los logs del servicio: lo que imprime la semilla solo aparece en la terminal de quien la corre.

**Mientras no se corrija el `Dockerfile`** (hallazgo H1 del informe de MATU-64), la imagen no trae `infra/semillas/catalogo_demo.py` y la semilla falla con `FileNotFoundError`. Antes del paso 4, dentro del contenedor, se baja el archivo del mismo commit que está desplegado (cambia `<commit>` por el que muestra Railway en el despliegue de `matu-api`):
```
python -c "import urllib.request as u; u.urlretrieve('https://raw.githubusercontent.com/MartinHenriquez131/MATU_PROYECTO/<commit>/infra/semillas/catalogo_demo.py', '/app/infra/semillas/catalogo_demo.py')"
```
Se pierde en el próximo despliegue.

## 4. Crear la demo desde cero (si hubiera que rehacerla)

Lo que se hizo el 09-11, en orden:

1. **Proyecto** `matu-demo`, con Postgres 16 (`ghcr.io/railwayapp-templates/postgres-ssl:16`, con volumen en `/var/lib/postgresql/data`), Redis (plantilla `redis`) y un servicio vacío `matu-api` con el `Dockerfile`, el pre-deploy, el start y el healthcheck de staging. Revisa que la plantilla no deje Postgres 18 y que Redis exista **antes** de cargar `REDIS_URL`: una referencia a un servicio que todavía no existe queda vacía, y crear la cuenta responde 500.
2. **Las variables que no son secretas** (sección 1) y el dominio.
3. **Los 8 secretos**, desde el computador, sin que se vean:
   ```
   g() { python -c "import secrets; print(secrets.token_hex(32))"; }
   railway variables --service matu-api --skip-deploys \
     --set "PEPPER_EMAIL=$(g)" --set "JWT_CLAVE=$(g)" --set "PEPPER_PIN=$(g)" \
     --set "PEPPER_RECUPERACION=$(g)" --set "PEPPER_LIMITES=$(g)" \
     --set "MATU_OWNER_PASSWORD=$(g)" --set "MATU_APP_PASSWORD=$(g)" \
     --set "KEK_ENTORNO=$(python -c "import secrets,base64; print(base64.b64encode(secrets.token_bytes(32)).decode())")" > /dev/null && echo "8 secretos cargados"
   ```
4. **Preparar la base**, con el TCP Proxy de Postgres encendido solo para este paso (necesita `psql` 16 en el computador):
   ```
   ADMIN_DATABASE_URL="$(railway variables --service Postgres --kv | grep '^DATABASE_PUBLIC_URL=' | cut -d= -f2- | tr -d '\r')"
   export ADMIN_DATABASE_URL
   railway run --service matu-api sh infra/railway/preparar_base.sh
   unset ADMIN_DATABASE_URL
   ```
   Después se apaga el TCP Proxy.
5. **Desplegar** `matu-api` desde `main`. El log tiene que mostrar todas las migraciones antes de Uvicorn, `entorno=staging`, `diagnostico_proxy=apagado` y `/v1/salud` 200.
6. **Sembrar** (sección 3, sin `--restablecer`).
7. **Los tres cron**, después de sembrar (las fechas de la semilla se calculan con el `Reloj`, así que la primera corrida no las borra).

## 5. Reglas

- Solo datos sintéticos: correos `@example.com` y `@example.org`, celulares `+569000000xx`.
- Nunca `FORWARDED_ALLOW_IPS=*` ni `0.0.0.0/0`. `DIAGNOSTICO_PROXY` siempre apagado.
- Ningún secreto, enlace de relevo ni PIN en un chat, un documento o un commit. Si se pega uno por error, se rota: para el relevo de ejemplo basta con `--restablecer`.
- Para las sesiones con usuarios se usa la demo, no staging: así un despliegue de staging no corta una sesión.
