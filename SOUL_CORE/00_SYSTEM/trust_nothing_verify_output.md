# PROTOCOLO ABSOLUTO — TRUST NOTHING. VERIFY THE OUTPUT.

Fecha de Institución: 6 de Septiembre de 2026
Causa: Invalidación de QA de M-01. Confusión entre archivo antiguo (`VIDEO_M01_OFICIAL_73S.mp4` a 720p 1fps) y el archivo nuevo (`M01_CONTEMPLATIVO_MASTER_73S.mp4`), más la ausencia inadmisible de subtítulos dinámicos de locución completa.

---

## 1. LA REGLA INQUEBRANTABLE
- **PROHIBIDO REPORTAR POR INTENCIÓN O MEMORIA:** Nunca se reporta lo que se pretendía hacer, ni el comando que se ejecutó, ni lo que dice un script.
- **SOLO SE REPORTA LO QUE FFPROBE Y CAPTURAS REALES DEMUESTRAN DEL ARCHIVO FINAL:**
  1. `ffprobe` debe inspeccionar físicamente el archivo exportado y su JSON crudo debe incluirse en la evidencia.
  2. Debe verificarse la presencia de subtítulos quemados en video mediante extracción física de fotogramas (`ffmpeg -ss XX -vframes 1 frame_XX.png`).
  3. Si no hay subtítulos legibles sobre los fotogramas extraídos del archivo final → **FAIL AUTOMÁTICO**.

---

## 2. REQUISITOS FÍSICOS OBLIGATORIOS DE M-01
1. **Resolución:** Estrictamente 1920x1080 (16:9).
2. **Framerate:** 30 fps continuos (no 1 fps de stillimage).
3. **Subtítulos Dinámicos Completos:** Toda la locución transcrita y sincronizada sobre el video (no solo 1 o 2 versículos).
4. **Cinemática de Fondo:** Video continuo de amanecer y naturaleza en movimiento.
5. **Audio:** Master sacro balanceado (Voz cálida de Antonio + BGM sacra atenuada).
