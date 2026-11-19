# BITÁCORA MAESTRA DE CONVERSACIÓN Y GUÍA DE CONTINUIDAD EN WINDOWS
**Proyecto:** Estrategia y Fábrica Automatizada de Monetización Faceless GTA 6  
**Repositorio GitHub:** [ponchogf88/soul-youtube](https://github.com/ponchogf88/soul-youtube)  
**Fecha de Sincronización:** 19 de Noviembre, 2026  

---

## 1. HISTORIA COMPLETA Y CONTEXTO DE LA SESIÓN

### A. Solicitud Inicial: "GTA6 - faceless monetizing strategy"
Se diseñó y construyó un ecosistema integral de monetización faceless para el lanzamiento de **Grand Theft Auto VI**, estructurado bajo las reglas maestras de AMDA:
- **Cero trabajo manual para el humano.**
- **Enfoque 100% visual:** No diapositivas aburridas de texto, sino gameplay 4K cinemático, edición con ritmo acelerado y cero saturación de texto en pantallas principales.
- **Normalización acústica estricta:** Audio masterizado a `-14 LUFS` según el estándar de YouTube.

### B. Entregables Generados en la Carpeta `GTA6_FACELESS_MONETIZATION/`:
1. `00_DASHBOARD_GTA6_WAR_ROOM.html`: Centro de comando visual interactivo (War Room) con KPIs de monetización, embudo de ingresos por CPM en USA/UK, temporizador de cuenta regresiva y selector de guiones.
2. `01_BLUEPRINT_MAESTRO_MONETIZACION_GTA6_FACELESS.md`: Plan maestro de monetización que cubre AdSense, marketing de afiliados (hardware, mandos, consolas), patrocinadores y automatización de DMs con Lead Magnets.
3. `02_PACK_GUIONES_LANZAMIENTO_Y_SHORTS_CRP.md`: Batería completa de guiones para videos largos (8-12 min) y Shorts de alto impacto (formato Hook-Retain-Payoff).
4. `03_CALENDARIO_GUERRA_30_DIAS_Y_SEO_MATRIX.csv`: Matriz de 30 días con fechas de publicación, títulos con alto CTR, tags SEO optimizados y descripciones prediseñadas.
5. `04_PROMPTS_MINIATURAS_HIGH_CTR_Y_PACKAGING.md`: Fórmulas y prompts para Midjourney / Flux orientados a miniaturas con CTR superior al 12%.
6. `gta6_faceless_pipeline.py`: Motor CLI en Python para sanitización de audio a -14 LUFS, renderizado 16:9 y recorte dinámico 9:16 (Shorts/Reels/TikTok).
7. `05_INSPECCION_REEL_VIRAL_INSTAGRAM.md`: Análisis forense en profundidad del Reel viral `@vibecoder_es` con 26.5K likes y 11.5K comentarios, detallando su fórmula de conversión por DMs aplicable a GTA 6.
8. `requirements.txt`: Dependencias del ecosistema listas para instalación rápida con `pip` o `uv`.

---

## 2. GUÍA PASO A PASO PARA CONTINUAR EN WINDOWS

Cuando abras tu computadora con **Windows**, sigue estos sencillos pasos en tu terminal (PowerShell o CMD):

### Paso 1: Clonar o Actualizar el Repositorio
Abre PowerShell o Windows Terminal y navega a tu carpeta de proyectos:

```powershell
cd C:\Users\%USERNAME%\Projects
# Si ya lo habías clonado antes:
cd soul-youtube
git pull origin main

# Si es la primera vez que lo descargas en Windows:
git clone https://github.com/ponchogf88/soul-youtube.git
cd soul-youtube
```

### Paso 2: Entrar a la Carpeta de GTA 6
```powershell
cd GTA6_FACELESS_MONETIZATION
dir
```

### Paso 3: Instalar Dependencias de Python
Asegúrate de tener Python 3.10+ instalado. Puedes crear un entorno virtual o instalar directamente:
```powershell
# Crear y activar entorno virtual (Recomendado):
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar librerías:
pip install -r requirements.txt
```

> **Nota sobre FFmpeg en Windows:**  
> Si no tienes `ffmpeg` instalado en Windows, puedes instalarlo en un solo comando usando `winget` o `choco`:
> ```powershell
> winget install Gyan.FFmpeg
> ```

### Paso 4: Abrir el Dashboard Interactivo
Puedes abrir el War Room Dashboard simplemente haciendo doble clic en el archivo o ejecutando:
```powershell
start 00_DASHBOARD_GTA6_WAR_ROOM.html
```
Esto abrirá una interfaz moderna y futurista con gráficos en tiempo real, calendario interactivo y visor de guiones.

### Paso 5: Ejecutar el Pipeline de Procesamiento de Video
Para comprobar que el entorno está al 100%:
```powershell
# Diagnóstico de herramientas del sistema:
python gta6_faceless_pipeline.py --check

# Ver menú de ayuda y comandos:
python gta6_faceless_pipeline.py --help

# Sanitizar audio a -14 LUFS estándar YouTube:
python gta6_faceless_pipeline.py --sanitize-audio tu_archivo_audio.wav

# Renderizar un Short en formato 9:16 con subtítulos automáticos:
python gta6_faceless_pipeline.py --render-crp-9x16 clip_origen.mp4 short_renderizado.mp4
```

---

## 3. RESUMEN DE ARCHIVOS SINCRONIZADOS

| Archivo | Tipo | Función Principal |
|---|---|---|
| `00_DASHBOARD_GTA6_WAR_ROOM.html` | HTML / CSS / JS | Dashboard interactivo visual para seguimiento del canal |
| `01_BLUEPRINT_MAESTRO_MONETIZACION_GTA6_FACELESS.md` | Markdown | Estrategia financiera y monetización paso a paso |
| `02_PACK_GUIONES_LANZAMIENTO_Y_SHORTS_CRP.md` | Markdown | Guiones listos para locución AI y montaje |
| `03_CALENDARIO_GUERRA_30_DIAS_Y_SEO_MATRIX.csv` | CSV | Calendario editorial y metadatos SEO para 30 días |
| `04_PROMPTS_MINIATURAS_HIGH_CTR_Y_PACKAGING.md` | Markdown | Prompts de miniaturas para Midjourney y Flux |
| `05_INSPECCION_REEL_VIRAL_INSTAGRAM.md` | Markdown | Análisis forense de reel viral y táctica de 11.5K comentarios |
| `gta6_faceless_pipeline.py` | Python CLI | Script de automatización de audio y video |
| `requirements.txt` | Texto | Lista de dependencias Python para Windows |

---
*¡Todo el trabajo está blindado, versionado y listo en GitHub para que retomes la producción en Windows sin perder ni un solo segundo!*
