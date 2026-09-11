# INFORME EXHAUSTIVO DE EXPLORACIÓN Y AUDITORÍA TÉCNICA
## Canales Espirituales de YouTube: 5 Formatos, 3 Canales, Arquitectura Devocional y Correcciones del Día
**Fecha de Auditoría:** 5 de Septiembre de 2026  
**Agente Investigador:** `explorer_survey_2`  
**Directorio Base Analizado:** `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT` (con referencias cruzadas a repositorios hermanos de canales)

---

## RESUMEN EJECUTIVO (VEREDICTO EN 60 SEGUNDOS)

1. **Estado Operativo Real:** Existe un volumen sustancial de especificaciones, guiones de alta calidad litúrgica y calendarios editoriales locales (CSV de 30 días, PDFs de especificación y auditoría visual de fecha 5 sep 2026), pero la máquina de automatización diaria está inactiva desde el 2 de septiembre (n8n apagado, `sacred_service.py` :8765 apagado, 0 LaunchAgents, 0 cron jobs activos).
2. **Los 3 Canales Identificados:**
   - **Canal 1 (ES):** *Agradecimiento Sincero* (`@agradecimientosincero` / ID: `UCABE05zuxJifGDhnuB5dGUg`). Canal público en YouTube con 3 suscriptores y 4 videos publicados.
   - **Canal 2 (EN):** *Eternally Grateful* (`@EternallyGratefulDaily` / `@EternallyGratefulDevotions`). Carpeta local en disco con guiones en inglés, pero sin videos públicos y con miniaturas que requieren rediseño urgente.
   - **Canal 3 (ES+EN):** *Oración Bilingüe / Orando con Cristina Campos*. Actualmente sin carpeta propia en el sistema de directorios (archivos dispersos en `YOUTUBE GOD CHANNELS/TEXT`), con un piloto de 11:02 min que debe estandarizarse al formato canónico de 15 minutos.
3. **Los 5 Formatos de Video:**
   - **60 Segundos (Shorts / 9:16):** Anzuelo de alta retención (95–115 palabras a 120–140 WPM), 0:00–0:06 hook + 0:07–0:48 decreto + 0:49–1:00 CTA hacia el video largo.
   - **5 Minutos (Devocional Rápido / 16:9):** 550–950 palabras a 110 WPM. Modelo: `GUION_ORACION_6_MINUTOS_3_SEGUNDOS.md` y video en vivo `AkiQT3CUgOo` (5:28). Oración condensada en 5 actos para el creyente apurado.
   - **15 Minutos (Oración Canónica / 16:9):** El pilar de retención y descubrimiento (1,250–1,450 palabras a 110–120 WPM). Regulado por gate técnico estricto de 14:00–16:00. Estilo Galeano con 5 actos inmutables.
   - **45 Minutos ("Estar con Dios" / 16:9):** Plegaria extendida matutina o nocturna (3,600–4,200 palabras de locución + 10–15 min de colchón musical sacro a 432 Hz). Diseñado para acompañamiento continuo y acumulación de Watch Time.
   - **1 Hora 10 Minutos (70 Minutos / Devocional Dominical & Vigilia / 16:9):** 4,000–4,500 palabras de liturgia + 25–30 min de piano/pads continuos en 432 Hz. Motor masivo para alcanzar las 4,000 horas de monetización. Requiere verificación telefónica de YouTube.
4. **Infracciones Críticas Detectadas Hoy (5 Sep 2026):**
   - Se subieron a YouTube videos horizontales cortos de 33s, 34s y 46s (`mbhbQLktAY4`, `iojQEROVCvM`, `90FHwQp3fN8`), lo cual está terminantemente prohibido por degradar la señal algorítmica.
   - Persiste en miniaturas y scripts la mención prohibida de "Reto de 7 Días", "Día 1", "Día 2" y el horario antiguo de "5:00 AM" (el horario ritual obligatorio es 06:00 AM y 22:00 PM).
   - En el canal en inglés, se montaron textos en inglés encima de plantillas en español rompiendo la caja tipográfica.

---

## SECCIÓN 1: REQUISITOS TÉCNICOS Y ESTRUCTURALES DE LOS 5 FORMATOS DE VIDEO

A continuación se detalla la matriz de especificación paramétrica para cada una de las 5 duraciones exigidas:

| Parámetro | 1. Short Anzuelo (60s) | 2. Devocional Rápido (5m) | 3. Oración Canónica (15m) | 4. Estar con Dios (45m) | 5. Vigilia / Domingo (1h 10m) |
|---|---|---|---|---|---|
| **Relación de Aspecto** | Vertical 9:16 (1080×1920) | Horizontal 16:9 (1920×1080) | Horizontal 16:9 (1920×1080) | Horizontal 16:9 (1920×1080) | Horizontal 16:9 (1920×1080) |
| **Duración Gate** | 57s – 60s exactos | 5:00 – 6:03 min | 14:00 – 16:00 min (Obligatorio) | 45:00 – 50:00 min | 65:00 – 72:00 min (70m promedio) |
| **Presupuesto Palabras** | 95 – 115 palabras | 550 – 950 palabras | 1,250 – 1,450 palabras | 3,600 – 4,200 palabras | 4,000 – 4,500 palabras |
| **Tiempo Locución Efectiva** | 50 – 52 segundos | 4:30 – 5:15 minutos | 11:00 – 12:30 minutos | 32:00 – 38:00 minutos | 38:00 – 45:00 minutos |
| **Colchón Sonoro / Pausas** | 8 – 10 segundos | 45 – 60 segundos | 3:00 – 4:00 minutos | 10:00 – 15:00 minutos (432 Hz) | 25:00 – 30:00 minutos (432 Hz) |
| **Cadencia de Habla** | 120 – 135 WPM | 110 WPM | 110 – 118 WPM | 110 – 115 WPM | 105 – 112 WPM |
| **Horario Ritual de Estreno** | 11:00 AM / 17:00 PM | 06:00 AM (Secundario) | 06:00 AM (Días clave / Mié-Vie) | 06:00 AM (Mañana) / 22:00 PM (Noche) | 06:00 AM Domingos / Noche Vigilia |
| **Rol Estratégico en Funnel** | Tráfico frío y descubrimiento; embudo hacia video largo | Alivio inmediato para oyentes sin tiempo | Retención extrema (>70% APV) y lealtad comunitaria | Watch time masivo de fondo; compañía devocional | Generador supremo de horas para el umbral de 4,000h |
| **Requisito Técnico YT** | Sin restricción | Sin restricción | Cuenta estándar | **Requiere verificación telefónica** | **Requiere verificación telefónica** |

### Desglose Individual de Requisitos por Formato:

#### A. Formato 60 Segundos (Shorts Anzuelo)
- **Objetivo Psicológico:** Interrumpir el scroll compulsivo con un shock de paz y serenidad. No pretende ser la plegaria completa, sino un "decreto de poder" concentrado.
- **Estructura Interna:**
  1. *Hook Visual y Verbal (0:00–0:06):* Texto amarillo grueso con sombra negra: *"NO HAGAS SCROLL. DIOS TE ENVÍA ESTO HOY"* / *"Stop scrolling. Before you step into your day, take 60 seconds with God."*
  2. *Decreto Oracional de Poder (0:07–0:48):* Extraído obligatoriamente del clímax emocional del Acto 3 o 4 del video largo de 15m/45m. Clamor directo de salud, cancelación de miedos y puertas abiertas.
  3. *Llamado a la Acción y Canalización (0:49–1:00):* Petición de "Escribe AMÉN", compartir con un ser querido y superposición visual fija con flecha señalando: *"Oración completa de 15 minutos en el canal 🙏"*.
- **Configuración ASS:** Anton o Montserrat ExtraBold, 62pt, Outline 6.0, Shadow 3.0, subtítulos dinámicos palabra por palabra.

#### B. Formato 5 Minutos (Devocional Rápido)
- **Objetivo Psicológico:** Proporcionar sosiego a profesionales y madres/padres de familia que disponen de 5 a 6 minutos antes de salir al trabajo.
- **Evidencia en Repositorio:** `GUION_ORACION_6_MINUTOS_3_SEGUNDOS.md` (363s exactos) y video público `AkiQT3CUgOo` (5:28, *"HAZ ESTA ORACIÓN AL DESPERTAR..."* con 5 vistas y 3 likes).
- **Estructura Interna (5 Actos Condensados):**
  - Acto 1 (0:00–1:12): Saludo empático + respiración profunda guiada (inhalar, retener, exhalar la pesadez).
  - Acto 2 (1:12–2:24): Anclaje bíblico con dos citas canónicas (Mateo 11:28 y Salmo 91:4).
  - Acto 3 (2:24–3:40): Rendición de cargas y entrega del cansancio al altar del Padre.
  - Acto 4 (3:40–4:55): Cerco de intercesión sobre la casa, hijos, mesa y salud física.
  - Acto 5 (4:55–6:03): Bendición de Salmo 4:8 y activación del Muro de Oración en comentarios.

#### C. Formato 15 Minutos (Oración Canónica Matutina / Nocturna)
- **Objetivo Psicológico:** Es el núcleo del canal. Plegaria pausada que el creyente escucha concentrado mientras se arregla, viaja o desayuna. Genera el mayor compromiso y vínculo afectivo.
- **Evidencia en Repositorio:** `oracion_15m_manana_piloto.md` (1,612 palabras), `GUIONES_GALEANO_CON_DIOS_FIN_DE_JULIO.md` (3 guiones de 14:00, 14:15 y 15:00 min) y `day_01_script_15min.md` en inglés.
- **Regla Gate Inviolable (`as_formats.py`):** Si el render final no dura entre **14:00 y 16:00 minutos**, el compositor rechaza el archivo y prohíbe su subida.
- **Estructura Litúrgica Canónica:**
  - Acto 1 (0:00–2:30): Saludo íntimo, validación del dolor y cansancio, pausa respiratoria sin prisa.
  - Acto 2 (2:30–7:00): Adoración, agradecimiento por el don de la vida y entrega de deudas/preocupaciones concretas.
  - Acto 3 (7:00–11:30): El Puente Profético; cambio de voz hacia el oyente: *"No estás escuchando esto por casualidad; Dios vio tus lágrimas en secreto"*. Citas bíblicas leídas y desglosadas.
  - Acto 4 (11:30–13:30): Declaraciones de victoria y ruptura de ataduras sobre la descendencia y el trabajo.
  - Acto 5 (13:30–15:00): Bendición sacerdotal (Números 6:24-26 o Salmo 4:8) + Muro de Fe (CTA AMÉN).

#### D. Formato 45 Minutos ("Estar con Dios" / Compañía y Noche)
- **Objetivo Psicológico:** Servir de manto de paz y compañía constante. Se deja sonando en altavoces o auriculares mientras se realizan tareas domésticas o al meterse en la cama para combatir el insomnio.
- **Evidencia en Repositorio:** `generate_production_spec_pdf.py` (Líneas 299–305, 345–350) y `CALENDARIO_30_DIAS_CANVA_BULK.csv` (20 de los 30 días programados bajo este formato a las 06:00 AM o 22:00 PM).
- **Composición Técnica:**
  - 32 a 38 minutos de narración espiritual continua (3,600 a 4,200 palabras) estructurada en ciclos devocionales.
  - 10 a 15 minutos de extensión sonora pura con piano acústico, pads celestiales y cuerdas afinadas a **432 Hz** a -22 dB LUFS, permitiendo un desvanecimiento suave hacia el reposo o el sueño profundo.
- **Requisito Crítico:** Requiere obligatoriamente verificación de número de teléfono en YouTube Studio; sin ella, YouTube rechaza cualquier subida superior a 15 minutos.

#### E. Formato 1 Hora 10 Minutos (70 Minutos / Devocional Dominical & Vigilia)
- **Objetivo Psicológico:** Experiencia inmersiva de recarga espiritual profunda para días festivos, domingos de reposo ("Día del Señor") o vigilias nocturnas de sanidad.
- **Evidencia en Repositorio:** Días 07, 14, 21 y 28 de `CALENDARIO_30_DIAS_CANVA_BULK.csv` ("Devocional de Domingo: Reposo, Renovación y Bendición Total", Salmo 23 verso a verso, etc.).
- **Arquitectura Sonora y Textual:**
  - 4,000 a 4,500 palabras de locución solemne dividida en meditaciones bíblicas por estrofas.
  - Entre 25 y 30 minutos de ambiente sacro instrumental en bucle continuo de 432 Hz.
  - El usuario puede dormirse o meditar sin ser despertado por cambios abruptos de volumen o avisos publicitarios estidentes.

---

## SECCIÓN 2: SCRIPTING, PACING, RETENCIÓN, HOOKS, CTAS Y ESTRUCTURAS DEVOCIONALES

### 1. Pacing y Ritmo Litúrgico (Prohibición de Velocidad Comercial)
- En el nicho devocional, la tasa convencional de YouTube (150–170 WPM) **está formalmente prohibida**, ya que destruye la intimidad y genera estrés en la audiencia de 45–75+ años.
- **Estándar Litúrgico Obligatorio:** **110 a 125 palabras por minuto (WPM)**.
- Pausas dramáticas de **1.5 a 2.5 segundos** en los puntos suspensivos (`...`) y saltos de párrafo para permitir la asimilación espiritual.
- Configuración ElevenLabs / TTS: Modelo *Multilingual v2*, Stability: 0.65, Similarity: 0.78–0.80, Style Exaggeration: 0.0, Speed: 0.95–1.02 (para español solemne) y 1.05–1.08 (para inglés cálido).

### 2. La Regla de Oro de la "Reverencia Tatuada"
- En todos los guiones, archivos de texto, prompts, descripciones de YouTube y subtítulos en pantalla, las palabras sagradas:
  $$\text{DIOS, JESÚS, SEÑOR, PADRE, ESPÍRITU, CREADOR}$$
  **DEBEN ESCRIBIRSE SIEMPRE EN MAYÚSCULAS COMPLETAS**. Escribir "Dios" o "Jesús" en minúscula sostenida se considera una falta de estilo litúrgico en el proyecto.

### 3. Estilizado Canónico de Subtítulos (Motor ASS / libass)
Los subtítulos son la guía de oración indispensable para ancianos y creyentes que ven el video en silencio en sus camas o transportes:
- **Tipografía:** *Anton* o *Montserrat ExtraBold* (48pt para horizontal 16:9; 62pt para vertical 9:16).
- **Borde y Sombra:** Borde negro grueso (`Outline: 6.0`) con sombra sólida (`Shadow: 3.0`) para garantizar legibilidad absoluta sobre amaneceres o nubes blancas.
- **Cuerpo General:** Blanco puro `#FFFFFF`.
- **Palabras Sagradas:** Resaltadas dinámicamente en **Azul Rey Celestial (`#2563EB`)**.
- **Remate Litúrgico:** La última palabra de cada frase u oración se colorea en **Morado Púrpura Celestial (`#A855F7`)**.

### 4. Psicología de los Hooks (0–5 Segundos)
Los primeros segundos no venden el canal, validan el dolor o la promesa divina:
- *Fórmula 1 (Cansancio/Alivio):* "Si tu mente amaneció cansada, no pongas un pie fuera de tu cama sin entregar las próximas 24 horas al SEÑOR."
- *Fórmula 2 (No es casualidad):* "No estás viendo esto por casualidad. DIOS no te trajo hasta este viernes para dejarte caer justo ahora."
- *Fórmula 3 (Blindaje nocturno):* "Suelta la carga del día. Ninguna pesadilla ni mal tocará tu habitación hoy. Descansa bajo Sus alas."
- *Fórmula 4 (Short Anzuelo EN):* "Stop scrolling. Take 60 seconds with GOD. Your mistakes will never be bigger than His grace."

### 5. Estructura de Llamados a la Acción (CTAs Orgánicos de Fe)
El proyecto prohíbe los CTAs genéricos de marketing ("Suscríbete para más videos"). Se transforman en actos de comunión y fe:
- **Comentarios (El Muro de Oración):** *"Escribe AMÉN en los comentarios y anota los nombres de tus hijos, padres o enfermos para que oremos por ellos en comunidad como una sola familia en Cristo."* (Detona cientos de comentarios reales que el algoritmo de YouTube indexa como retención y satisfacción extrema).
- **Like:** Enmarcado como una *"ofrenda de gratitud"* o señal de honra al Creador por el día vivido.
- **Compartir:** Enmarcado como *"sé un mensajero de paz para alguien que sabes que hoy está cargando una pena en silencio"*.
- **Suscripción:** Enmarcado como *"unirse a nuestro altar de encuentro diario cada mañana a las 06:00 AM"*.

---

## SECCIÓN 3: DIFERENCIAS DE ENFOQUE ENTRE LOS 3 CANALES ESPIRITUALES

El ecosistema está concebido como una red de 3 canales complementarios que abarcan distintos mercados lingüísticos y formatos de consumo:

```
                          [ MASTER ÚNICO DE PRODUCCIÓN ]
                          (Guion 15m + Paisajes 4K + ASS)
                                         │
        ┌────────────────────────────────┼────────────────────────────────┐
        ▼                                ▼                                ▼
[ CANAL 1: ESPAÑOL ]             [ CANAL 2: INGLÉS ]            [ CANAL 3: BILINGÜE ]
Agradecimiento Sincero           Eternally Grateful             Orando con Cristina Campos
• Audiencia: LATAM & US Hispano  • Audiencia: US, UK, Global    • Audiencia: Comunidad Dual
• Tono: Íntimo, pastoral, cálido • Tono: Solemn, resonant, reverent • Tono: Pedagógico-Espiritual
• Estilo: Azul noche & Oro       • Estilo: Cinematic clean      • Estilo: Subtítulos Caja Roja
• Estado: EN VIVO (4 videos YT)  • Estado: Guiones listos / YT 0 • Estado: Huérfano en repo
```

### Tabla Comparativa de Canales:

| Dimensión | 1. Agradecimiento Sincero | 2. Eternally Grateful | 3. Oración Bilingüe (Cristina Campos) |
|---|---|---|---|
| **Idioma Principal** | Español neutro latinoamericano | Inglés estadounidense / global | Español guiado + Repetición en Inglés |
| **Audiencia Objetivo** | Hombres y mujeres 45–75+ años (México, Colombia, EE.UU. hispano) | Adultos y familias cristianas anglosajonas (EE.UU., Reino Unido, Canadá) | Creyentes hispanohablantes que desean aprender inglés orando |
| **Identificador / Handle** | `@agradecimientosincero` | `@EternallyGratefulDaily` / `@EternallyGratefulDevotions` | Por definir (actualmente sin handle propio) |
| **Horario Ritual** | 06:00 AM y 22:00 PM (Hora CDMX) | 06:00 AM EST y 10:00 PM EST | 07:00 AM o mediodía (Intercalado) |
| **Identidad Visual & Miniaturas** | Fondo azul noche (`#0B192C`), letras doradas (`#FFD700`), 3–5 palabras mayúsculas. | Paisajes sacros nítidos, texto blanco sans bold con contorno negro, logo watermark inglés. | Fondo paisajístico con "Caja Roja Devocional" de alto contraste con texto bilingüe. |
| **Locución / Voz** | Masculina joven-adulta cálida o voz solemne pastoral (ElevenLabs). | Voz cálida, profunda y reverente en inglés nativo (ElevenLabs / Edge). | Cristina Campos (ElevenLabs en español) + voz nativa en inglés. |
| **Estado Físico en Repo** | Carpeta `/AGRADECIMIENTO SINCERO /` (con espacio al final), 5 carpetas `day_XX`. | Carpeta `/ETERNALLY GRATEFUL/`, carpeta `SCRIPTS_EN` con 7 archivos. | **Sin carpeta propia**; archivos sueltos en `/YOUTUBE GOD CHANNELS/TEXT/`. |
| **Estado en YouTube** | Canal público activo (4 videos subidos entre 2 y 4 de septiembre). | Canal sin auditar / sin videos subidos formalmente en la sesión actual. | Piloto local de 11:02 minutos sin publicar. |

### Estrategia de Producción Multi-Mercado ("Un Master, Tres Salidas"):
Para evitar triplicar el trabajo y los costos de API, la directriz técnica de los documentos establece:
1. **Paso 1:** Producir el guion maestro de 15 minutos en español (Agradecimiento Sincero) con sus fondos 4K y subtítulos `.ass`.
2. **Paso 2:** Cortar el Short de 60 segundos del Acto 3 de ese mismo master.
3. **Paso 3:** Extender el audio con 30 minutos de piano sacro en 432 Hz para generar el video largo de 45m sin consumir tokens adicionales de locución.
4. **Paso 4:** Traducir fielmente el guion maestro al inglés, sincronizar la locución en inglés sobre el mismo montaje visual y aplicar el Brand Kit de *Eternally Grateful*.
5. **Paso 5:** Ensamblar la pista dual o alternada con subtítulos bilingües para el canal de Cristina Campos.

---

## SECCIÓN 4: CORRECCIONES Y SUGERENCIAS IDENTIFICADAS HOY (5 SEP 2026)

A partir del análisis exhaustivo del código de auditoría visual (`generate_audit_visual_pdf.py`), del generador de especificaciones (`generate_production_spec_pdf.py`) y del prompt unificado v3 (`Prompt_Maestro_Orquestador_AgradecimientoSincero.md`), se extrae el siguiente inventario forense:

### A. Correcciones Inmediatas (Infracciones a Eliminar Hoy Mismo)

1. **PROHIBICIÓN ABSOLUTA DE VIDEOS HORIZONTALES CORTOS (30–46 SEGUNDOS):**
   - *Hallazgo:* En el canal de YouTube `@agradecimientosincero` existen actualmente tres videos públicos que violan las reglas: `mbhbQLktAY4` (0:33, *"SANA TU MENTE HOY"*), `iojQEROVCvM` (0:34, *"ORACIÓN DEL 1 DE SEPTIEMBRE"*) y `90FHwQp3fN8` (0:46, *"BIENVENIDO A AGRADECIMIENTO SINCERO"*).
   - *Corrección:* No volver a subir jamás un video horizontal de menos de 14 minutos. Los videos de 30–60 segundos son estrictamente verticales (Shorts 9:16). Subir horizontales cortos entrena negativamente al algoritmo de YouTube.
2. **ERRADICAR DEFINITIVAMENTE "RETO DE 7 DÍAS", "DÍA 1", "DÍA 2":**
   - *Hallazgo:* El script `trigger_daily_devotional.py`, los defaults de n8n y las miniaturas oficiales (`Miniatura Oficial YouTube - ABRE CAMINOS`) continúan rotulando "RETO DE 7 DÍAS" y "DÍA 1".
   - *Corrección:* Eliminar toda numeración secuencial. Cada video debe ser 100% autosuficiente, descubrible e independiente en búsquedas orgánicas sin requerir contexto de serie previa.
3. **CORREGIR EL HORARIO DE 5:00 AM A 6:00 AM EN MINIATURAS:**
   - *Hallazgo:* Las miniaturas piloto y de `day_01` a `day_05` muestran el badge "5:00 AM".
   - *Corrección:* El horario ritual establecido y aprobado para la audiencia es **06:00 AM** para la oración de la mañana y **22:00 PM** para la oración de la noche (Hora México).
4. **REPARAR EL BRANDING Y LAYOUT DE ETERNALLY GRATEFUL:**
   - *Hallazgo:* La miniatura de prueba `Miniatura_Oficial_YouTube_Eternally_Grateful.png` fue generada pegando texto en inglés directamente sobre la plantilla en español, provocando textos encimados y cajas rotas.
   - *Corrección:* Crear una plantilla nativa en inglés en Canva con tipografía limpia y el logotipo `logo_watermark_eternally_grateful.png`.
5. **CERO MENCIÓN DE LA PALABRA "GALEANO":**
   - *Hallazgo:* Aunque el canal de referencia es "Galeano con Dios", se detectó la tentación de usar el término en metadatos.
   - *Corrección:* Regla de oro número 2 del expediente: Está terminantemente prohibido incluir la palabra "Galeano" en títulos, descripciones, tags, audio o miniaturas para evitar problemas de derechos de autor o suplantación.
6. **NORMALIZAR EL FORMATO BILINGÜE DE 11 MINUTOS A 15 MINUTOS:**
   - *Hallazgo:* El entregable `PACK_YOUTUBE_ORACION_11MIN_CRISTINA_CAMPOS.md` fija una duración arbitraria de 11:02 minutos (`FORMATO_VIDEO_DEVOCIONAL_BILINGUE_11MIN_CRISTINA_CAMPOS.mp4`), la cual no encaja en ninguno de los formatos aprobados.
   - *Corrección:* Extender las estrofas y pausas para que alcance los 14:00–16:00 minutos canónicos del Formato 3.

### B. Sugerencias Operativas y Arquitectura del Sistema

1. **Subida Inmediata del Piloto Español de 15 Minutos:**
   - El archivo `oracion_15m_manana_piloto.md` (1,612 palabras) cuenta con metadatos completos y aprobados en `oracion_15m_manana_piloto_METADATA.md`. Tras una revisión visual rápida del render, debe publicarse para establecer el primer video largo canónico del canal.
2. **Ejecución de la Verificación Telefónica en YouTube Studio:**
   - Acción obligatoria para el titular: Verificar la cuenta mediante SMS para habilitar de inmediato la subida de videos mayores a 15 minutos (indispensable para los formatos de 45m y 1h 10m).
3. **Cargar `CALENDARIO_30_DIAS_CANVA_BULK.csv` en Canva Business:**
   - El archivo CSV de 30 días está completamente listo en disco con títulos duales, versículos, hooks y miniaturas. Debe importarse mediante la herramienta *Bulk Create* de Canva Business para generar las 120 piezas gráficas en un solo lote.
4. **Resolver la Desconexión de n8n y Servicios Locales:**
   - n8n estuvo activo únicamente el 2 de septiembre con 7 ejecuciones (4 errores, 3 éxitos). Actualmente no hay ningún daemon ni LaunchAgent corriendo. Se debe decidir entre levantar un servicio permanente vía `launchd` en macOS o ejecutar la programación manual directamente en YouTube Studio.
5. **Crear el Espacio Propio para el Canal Bilingüe:**
   - Crear el directorio formal `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/ORACION BILINGUE CRISTINA CAMPOS/` con su propio `AGENTS.md`, Brand Kit y carpeta de scripts para evitar que siga disperso en carpetas temporales.

---

## SECCIÓN 5: INVENTARIO COMPLETO DE ARCHIVOS ANALIZADOS

A continuación se indexan todos los archivos de texto examinados durante la presente exploración con sus rutas absolutas, pesos y propósitos dentro del proyecto:

1. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/COMMUNITY_MANAGER_PACK_ETERNALLY_GRATEFUL.md` (3,415 bytes)  
   *Contenido:* Copywriting multi-plataforma para Shorts, TikTok, IG Reels y FB Reels para *Eternally Grateful*, reglas de oro para responder comentarios en los primeros 30 minutos y pin de oración.
2. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/GUION_ORACION_6_MINUTOS_3_SEGUNDOS.md` (5,646 bytes)  
   *Contenido:* Guion devocional exacto de 06:03 min (363s), 110 WPM, estructura de 5 actos para *Agradecimiento Sincero / Eternally Grateful*.
3. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/PACK_YOUTUBE_ORACION_11MIN_CRISTINA_CAMPOS.md` (2,800 bytes)  
   *Contenido:* Pack de lanzamiento para el video devocional bilingüe de Cristina Campos, 11:02 min, títulos SEO, subtítulos de caja roja y metadatos.
4. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/GUIONES_GALEANO_CON_DIOS_FIN_DE_JULIO.md` (14,935 bytes)  
   *Contenido:* Tres guiones completos de 14:00 a 15:00 min estilo Galeano (29, 30 y 31 de julio) para *Agradecimiento Sincero*, 110–115 WPM, 4-5 actos litúrgicos.
5. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/TEXTO_LIMPIO_SUBTITULOS_6MIN.txt` (4,152 bytes)  
   *Contenido:* Transcripción limpia en español sin etiquetas técnicas del devocional de 6 minutos para sincronización ASS.
6. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/CLEAN_SUBTITLE_TEXT_6MIN_ENGLISH.txt` (4,279 bytes)  
   *Contenido:* Transcripción en inglés correspondiente a la oración de 6 minutos para la versión anglosajona / subtitulado bilingüe.
7. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/CALENDARIO_30_DIAS_CANVA_BULK.csv` (16,209 bytes)  
   *Contenido:* Matriz completa de 30 días para Bulk Create en Canva con títulos ES/EN, textos de miniatura, versículos, hooks de 5s, intención litúrgica y colores de subtítulos.
8. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/generate_production_spec_pdf.py` (46,191 bytes)  
   *Contenido:* Script ReportLab que define el Expediente Técnico de Producción de 120 videos mensuales (47 horas de video, 181,950 palabras, stack de herramientas y reglas no-negociables).
9. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/generate_audit_visual_pdf.py` (33,784 bytes)  
   *Contenido:* Script de auditoría operativa de fecha 5 de septiembre de 2026, diagnóstico forense de YouTube Data API, n8n, estado de miniaturas y plan de acción de 7 días.
10. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/TEXT/generate_calendar_pdf.py` (52,547 bytes)  
    *Contenido:* Script ReportLab que compila el dossier visual del Calendario Canva de 30 días, reglas de oro de tipografía y matriz de miniaturas.
11. `files.zip` -> `Guion_Video2_Oracion_Viernes_Gratitud.md` (15,311 bytes)  
    *Contenido:* Guion post-corrección de 30 minutos (~4,200 palabras), estructura de 4 actos, prompt de miniatura y short derivado de 60s.
12. `files.zip` -> `Prompt_Maestro_Orquestador_AgradecimientoSincero.md` (7,665 bytes)  
    *Contenido:* Prompt maestro v3 para orquestación editorial con Gemini/Claude, payload canónico en JSON, reglas inviolables de originalidad y modo de aprobación manual.
13. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO /SCRIPTS/oracion_15m_manana_piloto.md` (9,322 bytes)  
    *Contenido:* Guion maestro del piloto de 15 minutos en español listo para publicación.
14. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO /SCRIPTS/oracion_15m_manana_piloto_METADATA.md` (2,507 bytes)  
    *Contenido:* Paquete de metadatos aprobado para el piloto de 15 minutos.
15. `/Users/imac/Desktop/Projects/YOUTUBE CHANNEL/ETERNALLY GRATEFUL/SCRIPTS_EN/day_01_script_15min.md` (5,628 bytes) y `day_01_short_60s.md` (978 bytes)  
    *Contenido:* Guion en inglés de 15 minutos y Short derivado de 60s para *Eternally Grateful*.
