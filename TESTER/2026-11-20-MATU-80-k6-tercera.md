# TESTER · 20-11: MATU-80, tercera corrida de k6 (después del #128)

**Revisor:** Martín Henríquez (modo Martín) · **Fecha:** 20-11-2026, de 18:27 a 18:40
**Resultado:**
- K1 y K2 corregidos.
- Con 10 usuarios, la corrida es válida y la mediana de cada paso queda bajo 800 ms, pero el p95 no cumple.
- Con 50 usuarios, la máquina se satura.
- La decisión sobre RNF-05 queda para Jorge y Martín.

## Contexto

- **El #128 (562a8c8)** hace dos cosas:
  - **K1:** el pool de conexiones se configura con `DB_POOL_SIZE`, `DB_MAX_OVERFLOW` y `DB_POOL_TIMEOUT`, por omisión 10, 20 y 10 s. Si se llena, la API responde 503 con `Retry-After`.
  - **K2:** cada conexión lleva `jit=off`.
- Se fusionó y se desplegó en staging y en la demo.
- La carga corrió **en local**, con la pasarela falsa, nunca contra Railway ni Transbank.
- **Máquina:** la misma que en la segunda corrida, una ASUS VivoBook X515JA con Windows 11, un i3-1005G1 de 2 núcleos y 4 hilos, 8 GB de RAM y el disco casi lleno. Uvicorn con un solo proceso.
- Antes de cada corrida se repuso el stock con `preparar_carga.py --cuentas 50`.

## A · 10 usuarios: la corrida es válida

`checks` 100 %, `http_req_failed` 0,00 % y **406 iteraciones** (antes eran 70).

| paso | p50 | p95 | p99 | p95 de la segunda corrida |
|---|---|---|---|---|
| entrar (no se exige) | 161 ms | 1818 ms | 1836 ms | 1570 ms |
| catalogo | 49 ms | **141 ms** ✅ | 197 ms | 183 ms |
| pedido | 300 ms | 999 ms | 1547 ms | 1657 ms |
| confirmar | 520 ms | 1580 ms | 2017 ms | 2300 ms |
| pagar | 356 ms | 1072 ms | 1465 ms | 1458 ms |
| retorno | 1289 ms | 4840 ms | 5749 ms | **26279 ms** |
| total | 382 ms | 2939 ms | 4833 ms | 23388 ms |

## B · 50 usuarios: la máquina se satura

`checks` 99,46 %, `http_req_failed` 2,38 % y 213 iteraciones (antes eran 89).

| paso | p50 | p95 | p99 |
|---|---|---|---|
| entrar (no se exige) | 951 ms | 42623 ms | 43826 ms |
| catalogo | 2199 ms | 5133 ms | 5911 ms |
| pedido | 5056 ms | 9694 ms | 11303 ms |
| confirmar | 5789 ms | 11994 ms | 13649 ms |
| pagar | 5669 ms | 8837 ms | 10794 ms |
| retorno | 13600 ms | 18595 ms | 20495 ms |
| total | 5407 ms | 18000 ms | 42436 ms |

- **Seis cuentas no lograron entrar** (carga11, 13, 20, 24, 26 y 32), a los 36 s, cuando las 50 entran a la vez. Eso explica el 2,38 % de fallos.
  - Puede ser la CPU saturada por argon2id, o el límite de intentos por IP, porque todas entran desde la misma IP.
  - No está confirmado en el log.
- Ya **no hay errores por pool agotado**. En la segunda corrida eran el 13,86 %.

## Lectura

| ID | Severidad | Hallazgo |
|---|---|---|
| K1 | Resuelto | El pool de conexiones ya no da 500 con 50 usuarios |
| K2 | Resuelto | Con 10 usuarios, el retorno bajó de un p50 de 22 s a 1,3 s, y de un p95 de 26 s a 4,8 s |
| K4 | P2 | Con 10 usuarios, la mediana de cada paso queda bajo 800 ms, pero el p95 de pedido, confirmar, pagar y retorno no cumple. Con 50, todos los pasos suben juntos. Según la guía de `infra/carga`, eso apunta a la máquina (un proceso en 2 núcleos) más que a un paso en particular |
| K5 | P3 | Con 50 usuarios que entran a la vez, 6 no logran entrar. Falta confirmar en el log si es argon2id o el límite por IP |

**Para decidir (Jorge y Martín, con la tercera persona si corresponde):** una de tres.
- Repetir en un equipo con más núcleos y con más procesos de uvicorn.
- Ajustar la meta de RNF-05 para el piloto, por ejemplo a la mediana bajo 800 ms con 10 usuarios.
- Optimizar el retorno.
