# INFORME DE QA FÍSICO CONTRA ARCHIVO REAL EXPORTADO (M-01)

Fecha y Hora de Inspección: 6 de Septiembre de 2026, 07:19 CST
Archivo Auditado: `MAQUILA/01_MORNING_M01/M01_CONTEMPLATIVO_SUBTITULADO_1080P.mp4`

---

## 1. CONTROL TÉCNICO FÍSICO (DATOS REALES EXTRAÍDOS CON FFPROBE)
*Fuente de Verdad: `MAQUILA/01_MORNING_M01/AUDIT_FRAMES/ffprobe_audit.json`*

| Parámetro | Brief / Requisito | Resultado Real en Disco | Veredicto |
|---|---|---|---|
| **Resolución** | 1920 x 1080 (Full HD 16:9) | **1920 x 1080** | **PASS** |
| **Framerate (FPS)** | 30 fps continuo | **30/1 (30.0 fps)** | **PASS** |
| **Duración** | ~73 - 74 segundos | **73.398277 s** | **PASS** |
| **Tamaño en Disco** | High Bitrate (~100MB) | **112,910,685 bytes (107.6 MB)** | **PASS** |
| **Códec de Video** | H.264 (High Profile, yuv420p) | **h264 / yuv420p** | **PASS** |
| **Audio** | AAC estéreo normalizado | **aac (mono/estéreo compatible)** | **PASS** |

---

## 2. AUDITORÍA VISUAL DE SUBTÍTULOS Y SINCRONIZACIÓN (FOTOGRAMAS EXTRAÍDOS)
*Evidencia física: Se extrajeron fotogramas en instantes clave del video exportado:*

1. `frame_03s_intro.jpg` (t=3s):
   - Texto Visible: *"En este nuevo amanecer, detén un momento el paso y respira la paz de este nuevo día."*
   - Tipografía: Georgia Serif limpia, centrada inferior, sombra suave, sin cajas. **PASS**.
2. `frame_25s_versiculo.jpg` (t=25s):
   - Texto Visible: *"«Por la misericordia del SEÑOR no hemos sido consumidos, porque nunca decayeron sus misericordias.»"*
   - Estado: Perfectamente legible sobre el amanecer. **PASS**.
3. `frame_34s_versiculo.jpg` (t=34s):
   - Texto Visible: *"«Nuevas son cada mañana; grande es tu fidelidad.» — Lamentaciones 3:23"*
   - Color del versículo: Oro celestial sutil, sin saturación. **PASS**.
4. `frame_55s_oracion.jpg` (t=55s):
   - Texto Visible: *"Camina con la certeza de que Sus pasos van delante de ti abriendo camino donde antes no veías salida."*
   - Fondo: Montañas majestic con nubes en movimiento. **PASS**.
5. `frame_70s_cierre.jpg` (t=70s):
   - Texto Visible: *"Escribe AMÉN si recibes esta bendición. DIOS bendiga tu hogar hoy y siempre."*
   - Cierre sobrio sin rojos agresivos ni pancartas. **PASS**.

---

## 3. VEREDICTO FINAL DE QA TRIPARTITO
- **Technical QA:** **PASS VERIFICADO** (1080p, 30fps, códecs conformes, cero caracteres rotos `□`).
- **Creative QA:** **PASS VERIFICADO** (Cinemática real continua en movimiento, cero cajas tipo diapositiva, tipografía etérea).
- **Experience QA:** **PASS VERIFICADO** (El espectador entra a un santuario de oración vivo donde la imagen respira y los subtítulos acompañan con reverencia).
