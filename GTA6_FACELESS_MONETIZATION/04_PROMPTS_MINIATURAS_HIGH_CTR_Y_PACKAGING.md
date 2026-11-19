# 🎨 PACKAGING VISUAL, PROMPTS DE MINIATURAS HIGH-CTR & PROTOCOLO YOUTUBE STUDIO 2026

> **Proyecto:** `GTA6_FACELESS_MONETIZATION` (Ecosistema AMDA)  
> **Reglas Visuales No Negociables:**
> 1. **Regla de los 3 Elementos:** Máximo 3 puntos focales por miniatura (Sujeto/Escena principal + Indicador visual/Objeto + Máximo 2–3 palabras grandes).
> 2. **Regla de los 2 Segundos:** Cualquier miniatura debe entenderse al instante en pantalla de celular (`168x94 px` en feed móvil).
> 3. **Zero Crop / Full-Frame Integrity:** Nunca amputar cabezas, manos, armas o personajes clave en los bordes; respetar zonas seguras de YouTube (esquina inferior derecha reservada para el sello de duración `11:15`).
> 4. **Prohibido Texto Basura:** Jamás llenar la miniatura con frases largas ni bloques de texto sobre fondos oscuros planos.

---

## 1. PALETA CROMÁTICA OFICIAL: *LEONIDA VICE NEON & OBSIDIAN TACTICAL*

| Rol Cromático | Nombre Técnico | Código HEX | Uso en Miniaturas, HUDs y Subtítulos |
| :--- | :--- | :--- | :--- |
| **Base Oscura / Contraste** | Obsidian Night | `#090D16` | Sombras profundas, tarjetas HUD forenses y contorno de texto `4px`. |
| **Neón Firma Vice City** | Vice Magenta | `#FF2A85` | Luces de borde (rim light), flechas de atención y resaltado emocional. |
| **Acento Técnico / IA** | Leonida Cyan | `#00F0FF` | Escáneres de IA, rutas en mapa, datos telemétricos y badges de física. |
| **Dinero / Alerta Hardware** | Vice Gold / Amber | `#F59E0B` | Indicadores de `$50,000`, `212 GB`, SSD NVMe y palabras gancho clave. |
| **Aprobado / Seguro** | Emerald Shield | `#10B981` | Verificaciones válidas, rutas sin spoilers y controles de ciberseguridad. |
| **Peligro / Malware** | Signal Crimson | `#EF4444` | Alertas de troyano *GTA 6 PC*, error de espacio y zonas bloqueadas. |

- **Tipografía Recomendada:** `Montserrat ExtraBold` / `Anton` / `Impact Modern` (para palabras de miniatura de máximo 3 palabras) + `JetBrains Mono` (para datos HUD en video como `212 GB`, `EXP #07`, `$50,000/HR`).

---

## 2. BIBLIOTECA DE 6 PROMPTS HIGH-CTR (MIDJOURNEY v6 / FLUX + COMPOSICIÓN DE CAPAS)

> **Flujo de Trabajo:** Genera la imagen base limpia `--ar 16:9` sin texto inventado por la IA (o con texto mínimo guiado) y monta las flechas vectoriales + texto de 2–3 palabras en Canva/Photoshop en la zona superior izquierda o centro limpio.

### Arquetipo 1: Experimento de IA 24 Horas (Sub-Nicho Viral & Retención)
- **Título Asociado:** *Puse a Prueba la IA de GTA 6 Durante 24 Horas en Vice City*
- **Composición de 3 Elementos:** (1) Patrulla de policía iluminada con luces de neón magenta/cyan apuntando a un NPC sosteniendo un teléfono grabando en primer plano (cuerpo completo/medio sin cortes), (2) Cuadro de escaneo HUD cian sobre la cabeza del NPC (`#00F0FF`), (3) Texto corto superior izquierda: **`IA SIN LÍMITES`** o **`24 HORAS`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  Cinematic ultra-realistic game engine screenshot aesthetic of a neon-lit Vice City Miami night street after tropical rain, wet asphalt reflecting vibrant magenta #FF2A85 and cyan #00F0FF neon lights, a panicked pedestrian holding up a glowing smartphone filming a futuristic muscle car and a police cruiser with flashing blue and red sirens in the background, dramatic rim lighting, razor sharp focus, 35mm lens, rule of thirds composition with clean dark space on top left, no text, no watermark --ar 16:9 --style raw --v 6.1
  ```

### Arquetipo 2: Mapa Secreto & Ruta de Dinero Día 1 (Alto Search Value)
- **Título Asociado:** *Ruta Secreta en Port Gellhorn: Tus Primeros $50,000 en la Hora 1*
- **Composición de 3 Elementos:** (1) Toma aérea oblicua de un puerto industrial al atardecer con un coupé deportivo brillante estacionado frente a un almacén abierto, (2) Recorte circular o superposición limpia de mapa táctico brillante con una ruta marcada en verde esmeralda (`#10B981`) y flecha amarilla (`#F59E0B`), (3) Texto corto: **`+$50K HORA 1`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  High-contrast aerial drone perspective of a sun-drenched Florida industrial port dock at golden hour, turquoise ocean water, a sleek dark metallic sports coupe parked beside open shipping containers with subtle golden light spilling out, GTA VI Vice City hyper-detailed video game visual style, crisp shadows, clean negative space on the left side for map overlay, no text, no HUD --ar 16:9 --style raw --v 6.1
  ```

### Arquetipo 3: Comparativa Gráfica / Física Extrema (Mythbusters / Tech)
- **Título Asociado:** *¿Qué Pasa si Bloqueas el Puente de los Cayos? / PS5 vs PS5 Pro*
- **Composición de 3 Elementos:** (1) División diagonal limpia `50/50`: izquierda puente despejado soleado vs. derecha caos masivo con tráiler atravesado, autos bloqueados y helicóptero sobrevolando el agua turquesa, (2) Línea divisoria neón cian brillante, (3) Texto corto superior: **`¿SE ROMPIÓ?`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  Dramatic wide angle shot of a long coastal highway bridge stretching across crystal clear turquoise Florida Keys ocean water, a massive heavy semi-truck jackknifed sideways blocking all lanes causing a huge traffic jam of luxury sports cars, police helicopter hovering low over the water casting spotlights, hyper-detailed next-gen console graphics aesthetic, ultra crisp lighting, no text --ar 16:9 --style raw --v 6.1
  ```

### Arquetipo 4: Documental Noir — Misterios de los Pantanos Grassrivers (Alto Mid-Roll + Spotify)
- **Título Asociado:** *Los Misterios Ocultos de Grassrivers: La Historia Real que Inspiro a Leonida*
- **Composición de 3 Elementos:** (1) Hidrodeslizador (airboat) solitario entre neblina nocturna de los pantanos Everglades/Grassrivers con un reflector de luz cálida iluminando ojos brillantes de caimán en el agua oscura, (2) Efecto de documento/expediente desclasificado sutil en una esquina, (3) Texto corto dorado/blanco: **`NO ENTRES AQUÍ`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  Moody noir investigative documentary aesthetic in misty Florida Everglades swamp at midnight, dense cypress trees, dark reflective water, a lone rugged airboat shining a warm amber searchlight cutting through thick fog, faint glowing alligator eyes partially submerged in the foreground, subtle cyan moonlight rim lighting, atmospheric mystery, full framing without cutting boat, no text --ar 16:9 --style raw --v 6.1
  ```

### Arquetipo 5: La Crisis de los 212 GB & SSD (Afiliados Hardware Día 1)
- **Título Asociado:** *El Error de 212 GB que Bloquea Consolas Hoy (Solución SSD PS5/Xbox)*
- **Composición de 3 Elementos:** (1) Consola PS5 / Xbox oscura sobre escritorio gaming minimalista con iluminación magenta/roja, (2) SSD NVMe M.2 con disipador metálico en primer plano nítido con una flecha verde (`#10B981`) apuntando desde un ícono de advertencia rojo `212 GB FULL`, (3) Texto enorme legible en móvil: **`212 GB FIX`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  Sleek dark obsidian gaming desk studio photography, next-gen white and black gaming console in soft background blur, sharp macro focus in foreground on a black metallic M.2 NVMe heatsink SSD drive resting on matte dark slate, dramatic red #EF4444 and electric cyan #00F0FF studio rim lighting, clean composition with clear space on upper right, photorealistic commercial tech shot, no text --ar 16:9 --style raw --v 6.1
  ```

### Arquetipo 6: Alerta Ciberseguridad — Estafas "GTA 6 PC Gratis" (Puente Alto CPM)
- **Título Asociado:** *La Trampa del "GTA 6 para PC Gratis": Analicé el Troyano que Vacía Tarjetas*
- **Composición de 3 Elementos:** (1) Monitor de PC mostrando un archivo falso `GTA6_PC_CRACK.exe` envuelto en un aura roja de calavera/candado roto (`#EF4444`) con un logo de tarjeta bancaria en alerta, (2) Estética forense *Copper Titanium & Cyber Slate* coherente con `CYBERSECURITY_AI_GOVERNANCE_MTY`, (3) Texto de alto contraste: **`ES UN TROYANO`**.
- **Prompt Midjourney v6 / Flux:**
  ```text
  Cybersecurity forensic studio scene, dark slate monitor glowing in an obsidian room showing blurred red warning terminal code and a glowing crimson padlock icon, subtle Vice City pink and blue neon reflection on a dark desk keyboard, ominous high-tech threat alert atmosphere, clean dark upper left quadrant for bold typography, photorealistic, no readable gibberish text --ar 16:9 --style raw --v 6.1
  ```

---

## 3. PROTOCOLO DE SUBIDA EN YOUTUBE STUDIO 2026 (ANTI-THROTTLE & YPP SAFE)

1. **Visibilidad Inicial Obligatoria = `OCULTO` (Unlisted):**
   - Sube el archivo master al menos **45 minutos antes** de la hora de publicación objetivo.
   - Jamás publiques directo en `Público` ni uses `Estreno` en canal nuevo; deja que YouTube termine el procesamiento 4K/1080p, la verificación de derechos de autor (Confirmar **0 reclamos de Content ID**) y la indexación semántica de subtítulos.
2. **Configuración de Monetización & Declaraciones:**
   - **Creado para niños:** `NO` (siempre).
   - **Contenido Alterado o Sintético:** Marcar **`NO`** si es gameplay real de consola + gráficos HUD 2D + clonación de tu propia voz / narración sin deepfakes engañosos. Marcar **`SÍ`** únicamente si el video incluye secuencias fotorrealistas sintéticas generadas por IA (Veo/Runway) de personas o noticias.
   - **Restricción de Edad:** Mantener **sin restricción +18** en lo posible evitando sangre explícita en los primeros 30 segundos y en la miniatura (garantiza anuncios estándar de anunciantes Tier 1).
3. **Pistas Multi-Idioma (Auto-Dubbing / Multi-Language Audio):**
   - En videos largos clave (`Día 1`, `Día 2`, `Día 7`, `Día 10`), sube la pista de audio en **Inglés** y **Español** sincronizadas con el mismo timecode y traduce Título + Descripción en YouTube Studio. Esto multiplica el RPM promedio al capturar subasta de EE.UU., UK y Canadá.
4. **Efecto Cadena (Watch Time x3 para Sprint 4,000 Horas):**
   - Añade **siempre** el video a una Playlist temática con descripción SEO (`Experimentos de IA en Leonida`, `Guías Sin Spoilers GTA 6`, `Ciberseguridad Gaming`).
   - Configura **Pantalla Final** (`20s` finales) enlazando exactamente al video complementario mencionado en el guion + botón de Suscripción.
   - **NO activar Test A/B de miniaturas** mientras el canal tenga pocas impresiones diarias (fragmenta la muestra inicial y ralentiza el despegue).
5. **Shorts & TikTok CRP (`>62 segundos`):**
   - En TikTok: publicar en **Cuenta Personal**, duración mínima verificada **`62–75s`**, resolución `1080x1920`, cero marcas de agua de otras apps, y describir el tema con las **keywords exactas de búsqueda** (`Search Value`) en subtítulos y pie de video.
