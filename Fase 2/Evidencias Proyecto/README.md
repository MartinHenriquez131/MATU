# Evidencias del proyecto · Fase 2

| Archivo | Qué es |
|---|---|
| `MATU_Presentacion_Fase2.pptx` | Presentación de avance del 30 de octubre de 2026 |

## La demo

La demo que se mostró en la presentación está en el repositorio del código:

**[MATU_PROYECTO / Demo](https://github.com/MartinHenriquez131/MATU_PROYECTO/tree/main/Demo)**

Es una web app que muestra las tres capas de MATU: la ficha de relevo, el consumo con su predicción, y el pedido y pago. Usa solo datos sintéticos. Carmen cuida a María, Rosa la reemplaza y Rodrigo es su hijo.

### Cómo ejecutarla

Requiere [Git](https://git-scm.com/) y [Node.js 22](https://nodejs.org/). No hace falta el backend: sin él, la demo funciona sola en modo simulado.

```bash
git clone https://github.com/MartinHenriquez131/MATU_PROYECTO.git
cd MATU_PROYECTO/Demo
npm install
npm run dev
```

Después se abre **http://localhost:5173** en el navegador. Se ve mejor en un computador, entre 1280 y 1920 px de ancho.

- **Para recorrerla:** el panel del presentador permite saltar entre escenas.
- **Para volver al inicio:** basta con recargar la página. La demo no guarda nada en el navegador.
- **Para detenerla:** `Ctrl + C` en la terminal.

### Con el backend real (opcional)

Si la API de MATU está corriendo en `http://127.0.0.1:8000`, la demo la detecta y usa el modo real en las partes que ya existen: crear la cuenta, el grupo familiar y el alta de la persona con su consentimiento. Los pasos para levantar el backend con Docker están en el [README de la demo](https://github.com/MartinHenriquez131/MATU_PROYECTO/blob/main/Demo/README.md#levantar-el-modo-real).
