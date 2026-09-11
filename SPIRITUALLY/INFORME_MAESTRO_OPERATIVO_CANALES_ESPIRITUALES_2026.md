# INFORME MAESTRO OPERATIVO: REACTIVACIÓN Y EJECUCIÓN AUTÓNOMA DEL ECOSISTEMA YOUTUBE ESPIRITUAL
**Documento Técnico-Estratégico de Alta Dirección**
**Fecha de Emisión:** 11 de Septiembre de 2026  
**Entorno de Ejecución:** AMDA Agentic Engine / macOS Developer Home (`/Users/user`)  
**Proyectos Analizados:**
- Repositorio Local: [YOUTUBE CHANNEL](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/)
- Ecosistema Espiritual: [SPIRITUALLY](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/SPIRITUALLY/)
- Canal Primario: [AGRADECIMIENTO SINCERO ](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/SPIRITUALLY/AGRADECIMIENTO%20SINCERO%20/) (ID: `UCABE05zuxJifGDhnuB5dGUg` · Playlist: `PLLmrH1ayKBko`)
- Canal Espejo US: [ETERNALLY GRATEFUL](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/SPIRITUALLY/ETERNALLY%20GRATEFUL/)
- Canal Subnicho: [FINANCES WITH GOD / FINANZAS DIVINAS](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/SPIRITUALLY/FINANCES%20WITH%20GOD/)
- Archivos de Inteligencia Gemini Notebook / NotebookLM: [the-youtube-virality-playbook-20260902-1124](file:///Users/user/Desktop/Projects/YOUTUBE%20CHANNEL/SPIRITUALLY/STACK/ASSETS/the-youtube-virality-playbook-20260902-1124/)
- Motor de Renderizado Local: [agencia-core/scripts/sacred_video_composer.py](file:///Users/user/agencia-core/scripts/sacred_video_composer.py)

---

## 1. DIAGNÓSTICO FORENSE: ¿POR QUÉ SE DETUVIERON LOS CANALES?

El análisis de auditoría cruzada entre el código fuente, los registros de ejecución y los archivos locales revela que el paro de los canales **no se debió a falta de audiencia ni a falta de visión creativa**, sino a cuatro fallas estructurales operativas:

### 1.1. Dependencia de Fricción Humana (Cuello de Botella Manual)
- Se concibió inicialmente que la creación de videos dependiera de sesiones manuales en **Canva Business**, recortando clips, importando audios y exportando a mano.
- **Consecuencia:** Un creador humano no puede sostener la producción de 2 a 3 videos diarios de 15 a 60 minutos cuando requiere entre 45 y 90 minutos de edición manual por pieza. Ante la menor interrupción, la cadena se rompió y los canales quedaron inactivos.

### 1.2. El Fallo Fatal de Duración (Micro-videos de 27 a 47 Segundos)
- Las últimas pruebas de render generaron piezas de **27 a 47 segundos** en formato horizontal 16:9.
- **Consecuencia Algorítmica Devastadora:**
  1. No son Shorts (porque eran horizontales 16:9).
  2. No son videos largos (la audiencia de oración espera sumergirse en devoción, no escuchar un comercial de 30 segundos).
  3. YouTube clasifica estos videos como contenido de baja retención y nula satisfacción, cancelando el reparto de impresiones en *Browse Features* y *Suggested Videos*.

### 1.3. Desconexión de la Automatización (n8n sin Daemon Persistente)
- El webhook de n8n (`POST /webhook/auto-video-publish`) dependía de un proceso local que no tenía configurado un servicio persistente (`launchd` o daemon residente).
- Al cerrarse la terminal o suspenderse el equipo, el servicio HTTP en el puerto `:8765` (`sacred_service.py`) moría, dejando el pipeline sin pulso.

### 1.4. El Error de Empaquetado: "Reto de 7 Días / Día 1 / Día 2"
- En los primeros videos se utilizaron miniaturas y títulos serializados: *"Día 1: Oración para empezar..."*, *"Día 2..."*.
- **Consecuencia Psicológica:** La audiencia espiritual percibe los videos numerados como contenido con fecha de caducidad. Un usuario que descubre el canal en jueves no hace clic en el "Día 1" creyendo que "ya llegó tarde". Los videos deben ser **atemporales y rituales** (*Oración de la Mañana*, *Oración de Protección al Dormir*, *Salmo 91*).

---

## 2. INTELIGENCIA DE GEMINI NOTEBOOK / NOTEBOOKLM Y SU CRUCE CON EL PROYECTO

El análisis exhaustivo de los documentos extraídos del cuaderno de Gemini Notebook (`the-youtube-virality-playbook-20260902-1124`) aporta reglas operativas fundamentales que deben integrarse inmediatamente al pipeline:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│              CRUCE DE INTELIGENCIA NOTEBOOKLM vs. OPERACIÓN EN DISCO                            │
├────────────────────────────┬──────────────────────────────────┬─────────────────────────────────┤
│ Concepto Clave             │ Inteligencia Gemini Notebook     │ Aplicación en el Proyecto       │
├────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ Audiencia Diamante         │ Consumo +50 años, valoran paz,   │ Locución sosegada (110-120 WPM),│
│                            │ hábitos rituales, tiempo libre.  │ cero cortes rápidos o ruidos.   │
├────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ El Peligro de NotebookLM   │ NO usar NotebookLM Studio para   │ NotebookLM se usa para minería; │
│ para Generar Videos        │ render directo (marca de agua,   │ el render lo ejecuta FFmpeg     │
│                            │ voz sintética flaggeada slop).   │ con ElevenLabs + Pexels 4K.     │
├────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ Regla de los 3 Elementos   │ Fondo limpio, sujeto central,    │ Miniaturas 1280x720: Oro/Azul   │
│ en Miniatura (Packaging)   │ 3-5 palabras legibles en móvil.  │ con badge ritual "6:00 AM".     │
├────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ Muro de Fe (Algoritmo)     │ CTA de comentarios: "Escribe    │ Disparo masivo de engagement    │
│                            │ AMÉN por tu familia".            │ para escalar en recomendaciones.│
├────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ Arbitraje de RPM (US)      │ El nicho faceless en inglés      │ Replicar guiones litúrgicos en  │
│                            │ monetiza con CPM de $15-$30 USD. │ ETERNALLY GRATEFUL en paralelo. │
└────────────────────────────┴──────────────────────────────────┴─────────────────────────────────┘
```

### 2.1. La Audiencia Diamante (+50 Años)
- **Comportamiento:** Los consumidores de canales religiosos matutinos y nocturnos son personas maduras y adultos mayores. No buscan "edición frenética estilo MrBeast" ni transiciones cada 1.5 segundos.
- **Lo que premian:** Calidez humana, claridad en la voz, paisajes naturales sublimes (amaneceres, montañas, ríos, cielos estrellados) y un ritmo de respiración que transmita paz y esperanza.
- **Dispositivo dominante:** Smart TVs en la sala o cocina mientras preparan el café, y tablets/móviles en la mesa de noche antes de dormir.

### 2.2. Por Qué NO Exportar Videos Directos de NotebookLM
Como documenta rigurosamente la investigación interna (`stop-using-notebooklm-for-faceless-videos..-do-this-instead.md`):
- Los videos autogenerados por el nuevo estudio de NotebookLM poseen marcas de agua y una huella acústica (`AI Voice ID`) catalogada por Google como contenido sintético de baja elaboración (*AI Slop*).
- **El Método Idóneo:** NotebookLM se utiliza como **asistente de investigación y estructurador de guiones litúrgicos**. El video final debe ensamblarse mediante un pipeline propietario con voces de ultra-alta fidelidad (ElevenLabs Multilingual v2) y metraje cinematográfico real (Pexels / stock premium) libre de marcas de agua.

### 2.3. La Regla de los Tres Elementos en Miniaturas
1. **Fondo:** Cielo celestial, amanecer radiante o noche estrellada en azul oscuro (`#0A1128`).
2. **Sujeto Central:** Manos en oración, silueta en reverencia con resplandor dorado o cruz en contraluz.
3. **Texto Titular:** Máximo 3 a 5 palabras en tipografía gruesa (*Montserrat ExtraBold* o *Anton*), color **Oro Radiante (`#FFD700`)** con contorno negro de 6px y sombra dura.
4. **Badge Superior:** `6:00 AM` (o `10:00 PM`), reforzando la cita ritual diaria.

### 2.4. El "Muro de Fe" en los Comentarios
- El algoritmo de YouTube no evalúa la sofisticación gramatical de los comentarios, sino la velocidad y el volumen de interacción por impresión.
- Al incluir en el guion y en el primer comentario fijado:  
  *«Escribe "AMÉN" y deja aquí el nombre de la persona que amas para que nos unamos en oración por ella»*, se detonan cientos de comentarios orgánicos que empujan el video a la página principal de YouTube.

---

## 3. LA MATRIZ DE LOS TRES CANALES ESPIRITUALES

El ecosistema no compite entre sí; opera bajo la estrategia **"Un Máster, Tres Mercados"**:

```
                             [ GUIÓN LITÚRGICO MAESTRO ]
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
   [ CANAL 1: ESPAÑOL ]          [ CANAL 2: INGLÉS ]          [ CANAL 3: FINANZAS/FE ]
  Agradecimiento Sincero          ETERNALLY GRATEFUL             Finances With God
  ID: UCABE05zuxJifGDhnuB5dGUg   Audiencia US/UK/CA (Tier 1)    Subnicho Fe + Abundancia
  Voz: Don Mario / George        Voz: George US / Christopher   Voz: Reflexiva / Inspiradora
  Horario: 06:00 & 22:00 CST     Horario: 05:30 & 21:30 EST     Horario: 07:00 & 19:00 CST
```

### Canal 1: Agradecimiento Sincero (Canal Primario en Español)
- **Enfoque:** Devocional diario, salmos de protección y agradecimiento genuino.
- **Audiencia Objetivo:** México, Estados Unidos Hispano, Colombia, Centroamérica y España (+50 años).
- **Inspiración Algorítmica:** *Galeano Con Dios* (copiando la arquitectura y la serenidad del ritual, **jamás mencionando su nombre** ni usando sus marcas).
- **Voz:** ElevenLabs v2 con entonación pastoral profunda, cálida y sin dramatismos estridentes.

### Canal 2: ETERNALLY GRATEFUL (Canal Espejo Anglosajón)
- **Enfoque:** *Christian Morning Prayer*, *Bedtime Psalms for Sleep & Anxiety*, *Gratitude Devotionals*.
- **Arbitraje Financiero:** El RPM en Estados Unidos para el nicho de fe y relajación ronda los **$14.00 a $28.00 USD por cada 1,000 visitas**, frente a los $2.00–$3.50 USD de América Latina.
- **Ejecución:** Cada guión litúrgico probado con éxito en español se traduce y adapta culturalmente al inglés para alimentar este canal con el mismo metraje de video ya descargado.

### Canal 3: Finances With God / Finanzas Divinas (Subnicho de Prosperidad)
- **Enfoque:** Fe aplicada al trabajo, oraciones de rompimiento de deudas, sabiduría de Proverbios para los negocios y mentalidad de mayordomía bíblica.
- **Audiencia:** Emprendedores, profesionistas y jefes de familia de 35 a 60 años.

---

## 4. LOS TRES FORMATOS CANÓNICOS DEFINITIVOS

Queda terminantemente prohibido producir formatos improvisados de 30 o 45 segundos. La parrilla de producción se rige exclusivamente por tres formatos:

| Formato | Duración | Relación de Aspecto | Estructura / Ritmo | Función Algorítmica |
|---|---|---|---|---|
| **1. Short Anzuelo** | **60 seg exactos** | Vertical (9:16) 1080x1920 | Gancho de 3s + Clímax de la oración + CTA al video largo | Viralidad rápida, suscripciones y tráfico hacia los largos. |
| **2. Oración con el Señor** | **15 minutos** | Horizontal (16:9) 1920x1080 | 4 Actos litúrgicos: Apertura, Lectura Bíblica, Intercesión, Decretos | Retención alta (AVD > 60%), posicionamiento en Home y Sugeridos. |
| **3. Estar con Dios** | **45 a 60 minutos** | Horizontal (16:9) 1920x1080 | Oración profunda + Cama instrumental prolongada a 432 Hz | Acumular masivamente las 4,000 horas requeridas por YouTube. |

---

## 5. ESTÁNDARES SAGRADOS DE PRODUCCIÓN ("TATUADOS EN PIEDRA")

Toda pieza audiovisual generada por el motor debe cumplir estos cinco mandamientos inmutables:

### 5.1. Calibración Acústica Sagrada (432 Hz y -14 LUFS)
- **Afinación:** La música de piano y cuerdas ambientales debe estar afinada en **432 Hz** para inducir calma biológica y reducir la tensión del oyente.
- **Niveles de Sonoridad (LUFS):**
  - **Voz del Orador:** Normalizada a **-16.0 LUFS** integrada.
  - **Música de Fondo:** Atenuada a **-22.0 dB LUFS** en oraciones diurnas y **-24.0 dB LUFS** en oraciones para dormir.
  - **Master Final:** **-14.0 LUFS** integrada, con pico máximo (*True Peak*) de **-1.0 dBFS**.

### 5.2. Cadencia Vocal Contemplativa (110 a 125 WPM)
- Cero locución comercial o acelerada.
- Velocidad estricta de **110 a 125 palabras por minuto**.
- Pausas litúrgicas deliberadas de **1.5 a 2.0 segundos** en puntos suspensivos y cambios de sección, permitiendo respirar e interiorizar la oración.

### 5.3. Subtítulos Litúrgicos ASS (Advanced SubStation Alpha)
Renderizados por hardware vía FFmpeg con tipografía pesada (*Montserrat ExtraBold* o *Anton*):
1. **Contorno Blindado:** Trazo negro grueso de **6.5px** (`OutlineColour: &H00000000&`) para garantizar legibilidad absoluta sobre cualquier fondo brillante o nublado.
2. **Palabras Sagradas (Regla Inmutable):** Las palabras **`DIOS`**, **`JESÚS`**, **`SEÑOR`**, **`PADRE`**, **`ESPÍRITU`** deben ir siempre en **MAYÚSCULAS** y coloreadas en **Azul Rey Celestial** (`#2563EB` en web; `&H00F6823B&` en ASS).
3. **Remate de Frase:** La última palabra de cada estrofa u oración debe resaltarse en **Morado Púrpura Celestial** (`#A855F7` en web; `&H00F755A8&` en ASS).
4. **Cuerpo del Texto:** Blanco radiante puro (`#FFFFFF`).

---

## 6. ARQUITECTURA DEL MOTOR AUTÓNOMO "CERO FRICCIÓN HUMANA"

Para que los canales corran sin depender de la intervención humana, el flujo debe orquestarse de la siguiente manera:

```
[ BANCO DE GUIONES YOUTUBE ]
  (Liturgia atemporal: Mañana, Noche, Sanación, Protección)
             │
             ▼
[ AGENCIA-CORE: sacred_video_composer.py ]
  ├── 1. Sintetiza Voz ElevenLabs (115 WPM, pausas 1.8s)
  ├── 2. Consulta API Pexels (descarga clips 4K/FHD de amaneceres, ríos, cielo)
  ├── 3. Genera subtítulos ASS con colores litúrgicos (Azul Rey y Morado)
  ├── 4. Mezcla pista instrumental 432 Hz (-22 dB LUFS) + voz (-16 LUFS)
  └── 5. Renderiza Master MP4 con FFmpeg optimizado para YouTube
             │
             ▼
[ SISTEMA AUTOMÁTICO DE SUBIDA: upload_remastered_devotional.py ]
  ├── 1. Autentica con youtube_token.json (Canal Agradecimiento Sincero)
  ├── 2. Sube el video en estado OCULTO (Unlisted) 2 horas antes
  ├── 3. Adjunta Miniatura de Alto CTR (Oro/Azul + Badge 6:00 AM)
  ├── 4. Asigna metadatos, tags de cola larga y asocia a Playlist canónica PLLmrH1ayKBko
  └── 5. Programa el estreno público exacto (06:00 CST o 22:00 CST)
```

---

## 7. PLAN DE ACCIÓN Y REACTIVACIÓN EN 72 HORAS

Sin pedirle al usuario ejecutar ningún paso manual, el sistema debe autoejecutar la siguiente secuencia:

### Fase 1: Auditoría Técnica de Conectores (Inmediata)
1. **Verificar Token de YouTube:** Validar la vigencia del archivo `agencia-core/youtube_token.json` y refrescar credenciales de OAuth2 para el canal `UCABE05zuxJifGDhnuB5dGUg`.
2. **Validar Claves de API:** Confirmar saldo y conectividad en `ELEVENLABS_API_KEY` y `PEXELS_API_KEY`.

### Fase 2: Producción del Primer Lote Canónico (Día 1 y Día 2)
1. Generar **2 Oraciones Matutinas de 15 minutos** (Enfoque: Iniciar el día en victoria, bendición sobre el hogar).
2. Generar **2 Oraciones Nocturnas de 45 minutos** (Enfoque: Salmo 91 y Salmo 23 para dormir en paz, descanso y sanidad).
3. Generar los **4 Shorts correspondientes (60 segundos)** recortando el clímax de cada pieza larga con subtítulos dinámicos verticales.

### Fase 3: Programación y Orquestación Continua (Día 3)
1. Subir y programar las publicaciones en la consola de YouTube en sus dos horarios rituales:
   - **Estreno de la Mañana:** `06:00 AM (CST)`
   - **Estreno de la Noche:** `22:00 PM (CST)`
2. Configurar el demonio local en macOS (`launchd` o cronjob del sistema) para que ejecute el pipeline diario de forma autónoma sin requerir supervisión humana.

---

## 8. CONCLUSIÓN Y VEREDICTO FINAL

Los canales se detuvieron porque se intentó operarlos con un modelo de agencia tradicional (manual, dependiente de diseño y clics en navegadores). **El modelo que funciona es el de fábrica autónoma:**
- La inteligencia de **Gemini Notebook / NotebookLM** ya definió la psicología del nicho (+50 años, videos largos de alta retención, empaquetado simple de 3 elementos y comentarios como muro de fe).
- El motor en código de **`agencia-core`** ya cuenta con la capacidad de ensamblar el audio, los subtítulos litúrgicos y el metraje en Full HD a 432 Hz.
- Al desacoplar al humano de la cadena de montaje y dejar que el script produzca, empaquete y programe automáticamente, los canales recuperan su constancia ritual y comienzan a acumular el tiempo de reproducción necesario para monetizar de forma masiva.
