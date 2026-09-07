# Biblioteca de escenas — MVP (16)

**Regla:** se conserva el ID. El clip puede cambiar.  
**Status:** SEED = hay archivo o stock asignado. VALIDATED = pasó QA en un master. RETIRED = no se reusa.

Plantilla:

```
ID / TYPE / MOOD / TIME / DURATION / MOTION / AUDIO_BED / TRANSITION / USE / SOURCE / STATUS
```

---

## MORNING

### SUNRISE_01
- TYPE: contemplative · MOOD: hope / mercy · TIME: morning
- DURATION: 02:30–04:00 · MOTION: slow push-in, haze → focus
- AUDIO_BED: distant birds + piano 432 · TRANSITION: dissolve
- USE: apertura, gratitud, cierre
- SOURCE: `MAQUILA/01_MORNING_M01/cinematica_fondo_m01.mp4` **o** `ETERNALLY GRATEFUL/CINEMATIC_STOCK/stage1_sunrise_zoom.mp4`
- STATUS: SEED

### SUNRISE_02
- TYPE: contemplative · MOOD: newness · TIME: morning
- DURATION: 02:00–03:30 · MOTION: lateral drift, light bloom
- AUDIO_BED: light wind · TRANSITION: dissolve
- USE: segundo ciclo de gratitud
- SOURCE: pendiente (variante de sunrise, no clonar 01)
- STATUS: SEED (falta clip distinto)

### CLOUDS_01
- TYPE: contemplative · MOOD: peace · TIME: morning
- DURATION: 02:00–03:00 · MOTION: slow drift
- AUDIO_BED: air · TRANSITION: dissolve
- USE: petición, espera
- SOURCE: pendiente
- STATUS: SEED

### CLOUDS_02
- TYPE: contemplative · MOOD: awe · TIME: morning
- DURATION: 02:00–03:00 · MOTION: tilt up
- AUDIO_BED: pads · TRANSITION: dissolve
- USE: esperanza, “Dios responde”
- SOURCE: pendiente
- STATUS: SEED

### FOREST_01
- TYPE: contemplative · MOOD: protection · TIME: morning
- DURATION: 02:30–04:00 · MOTION: rays through leaves, slow dolly
- AUDIO_BED: leaves + piano far
- USE: fuerza, cobertura (M02)
- SOURCE: `CINEMATIC_STOCK/stage2_green_forest.mp4`
- STATUS: SEED

### OCEAN_01
- TYPE: contemplative · MOOD: relief · TIME: morning
- DURATION: 02:30–04:00 · MOTION: gentle waves, horizon hold
- AUDIO_BED: water low
- USE: cargas, Mateo 11 (M05)
- SOURCE: `CINEMATIC_STOCK/stage4_coast_beach.mp4`
- STATUS: SEED

---

## NIGHT

### SUNSET_01
- TYPE: contemplative · MOOD: surrender · TIME: night
- DURATION: 03:00–04:00 · MOTION: gold → blue
- AUDIO_BED: low cello
- USE: entrega de cargas (N01)
- SOURCE: pendiente (no usar stage5 cristo-monumento como default)
- STATUS: SEED

### MOON_01
- TYPE: contemplative · MOOD: rest · TIME: night
- DURATION: 02:30–04:00 · MOTION: slow orbit feel, static-safe
- AUDIO_BED: night air
- USE: paz mental
- SOURCE: pendiente
- STATUS: SEED

### STARS_01
- TYPE: contemplative · MOOD: vastness · TIME: night
- DURATION: 03:00–05:00 · MOTION: very slow field
- AUDIO_BED: deep pad
- USE: protección, Salmo 91
- SOURCE: `CINEMATIC_STOCK/stage7_stars_nebula.mp4`
- STATUS: SEED

### RAIN_01
- TYPE: contemplative · MOOD: healing · TIME: night
- DURATION: 02:00–03:30 · MOTION: window rain, warm interior bokeh
- AUDIO_BED: rain -24 LUFS
- USE: sanidad emocional (N04)
- SOURCE: pendiente
- STATUS: SEED

### NIGHT_OCEAN_01
- TYPE: contemplative · MOOD: deep rest · TIME: night
- DURATION: 03:00–05:00 · MOTION: moon path on water
- AUDIO_BED: waves far
- USE: renovación, vigilia
- SOURCE: pendiente
- STATUS: SEED

---

## REFLECTION

### LAKE_01
- TYPE: contemplative · MOOD: peace home · TIME: morning
- DURATION: 02:30–03:30 · MOTION: gold reflection, almost still
- AUDIO_BED: water lap
- USE: familia, hogar (M04)
- SOURCE: pendiente
- STATUS: SEED

### MOUNTAIN_01
- TYPE: contemplative · MOOD: trust · TIME: any
- DURATION: 02:30–04:00 · MOTION: slow rise
- AUDIO_BED: thin wind
- USE: caminos, provisión
- SOURCE: `CINEMATIC_STOCK/stage3_earth_mountains.mp4`
- STATUS: SEED

### CLOUDS_03
- TYPE: contemplative · MOOD: hope · TIME: any
- DURATION: 02:00–03:00 · MOTION: break in the cloud
- AUDIO_BED: pads
- USE: “Dios responde”
- SOURCE: pendiente
- STATUS: SEED

### FOREST_03
- TYPE: contemplative · MOOD: quiet · TIME: any
- DURATION: 02:00–03:00 · MOTION: deeper woods, less sky
- AUDIO_BED: birds far
- USE: reflexión, no apertura
- SOURCE: variante de FOREST_01 (no el mismo frame)
- STATUS: SEED

### PATH_01
- TYPE: contemplative · MOOD: ache → hope · TIME: morning
- DURATION: 02:00–03:30 · MOTION: path catching light
- AUDIO_BED: steps none (no Foley humano)
- USE: hijo que se aleja, caminos (M03)
- SOURCE: pendiente
- STATUS: SEED

---

## Stock mínimo para M01 15 min (hoy)

Obligatorias para montar lunes:

1. SUNRISE_01 — **hay clip**
2. CLOUDS_01 — si no hay clip, loop suave de SUNRISE_01 recortado distinto (temporal, marcar TEMP)
3. MOUNTAIN_01 — **hay clip**
4. FOREST_01 — **hay clip**
5. OCEAN_01 — **hay clip**
6. LAKE_01 — TEMP de OCEAN_01 si falta
7. SUNRISE_02 o reprise de SUNRISE_01 al cierre

No se usa `stage5_christ_monument` en M01. Demasiado literal. El paisaje es el protagonista; no un monumento.

Cuando un clip TEMP sobreviva 1 master PASS, o se valida o se reemplaza. No se queda TEMP más de 7 días.
