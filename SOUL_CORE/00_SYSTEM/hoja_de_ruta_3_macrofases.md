# HOJA DE RUTA OPERATIVA — 3 MACROFASES DE SOUL

Estado del Sistema:
- FASE 1: COMPLETADA (Auditoría física realizada + Primer piloto M-01 de 73s renderizado con ElevenLabs y QA PASS).
- FASE 2: EN EJECUCIÓN (Escalamiento de duraciones y derivación Content Mother).
- FASE 3: POR ACTIVAR (Orquestación autónoma programada).

---

## 🟢 FASE 1 — HACER QUE FUNCIONE (Auditoría + Piloto + QA)
**Objetivo:** Antigravity toma un brief y entrega un video real terminado y validado físicamente en disco, sin copy-paste y corrigiéndose solo ante fallas.
- **Flujo:** AUDITAR → PRODUCIR → VALIDAR → CORREGIR → ENTREGAR
- **Condición de Salida (Criterio de Victoria):**
  - [x] Auditoría física de hardware, APIs y assets (`hardware_and_tools_audit.md`).
  - [x] Síntesis de voz real vía ElevenLabs sin intervención humana.
  - [x] Renderizado de video MP4 completo con audio balanceado y stock sacro.
  - [x] QA físico verificado en ffprobe (`VIDEO_M01_OFICIAL_73S.mp4`).

---

## 🔵 FASE 2 — HACER QUE ESCALA (Escalamiento + Derivación)
**Objetivo:** Tomar el molde probado en Fase 1 y expandirlo a las duraciones canónicas y piezas derivadas bajo la regla Content Mother.
- **Escalamiento Temporal:** 5m / 15m → 30m → 45m → 70m/90m.
- **Derivación Content Mother:**
  - MASTER (16:9) → SHORT (9:16 vertical con hook) → CLIPS DEVOCIONALES → POSTS DE COMUNIDAD → THUMBNAILS.
- **Condición de Salida (Criterio de Victoria):**
  - [ ] Un video Master extendido (5-15 min) renderizado y validado.
  - [ ] Un Short derivado (9:16) renderizado y validado a partir del mismo concepto sin clonar assets prohibidos.
  - [ ] Generación del paquete de metadatos (Título, Descripción, Tags, Cita Bíblica) para publicación.

---

## 🟣 FASE 3 — HACER QUE OPERE SOLO (Maquila Autónoma)
**Objetivo:** SOUL se convierte en un sistema de producción continuo y desacoplado del operador humano.
- **Flujo:** IDEA / BRIEF → ORQUESTADOR → PRODUCCIÓN → QA → REWORK INTERNO → DERIVACIÓN → ENTREGA / PROGRAMACIÓN.
- **El Rol Humano:** Dirección, decisiones, visión editorial y supervisión estratégica.
- **Condición de Salida (Criterio de Victoria):**
  - [ ] Pipeline disparable mediante un solo trigger (launchd / cron / n8n local).
  - [ ] Ejecución desatendida matutina (06:00 AM) y nocturna (10:00 PM).
  - [ ] Reporte automático a dashboard/monitor vertical de observabilidad.
