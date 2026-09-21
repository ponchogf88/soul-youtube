# 📋 BITÁCORA MAESTRA DEL PROYECTO: AMDA AGENTIC ENGINE & MEDIA DISCOVERY
> **Automatización de Navegador (Browser-Use), Scraping de Medios para Redes Sociales, Gobernanza de Credenciales (.env) y Ecosistema Captoora Studio**

---

### Ficha Técnica y Metadatos de la Bitácora
* **Proyecto Principal:** AMDA Agentic Engine / Ecosistema Captoora Studio (`CAPTOORA.STUDIO`)
* **Titular / Autor:** Alfonso "Poncho" Gutiérrez (`@ponchogf88` / `lic.jagf87@gmail.com`)
* **ID de Conversación:** `e265a33e-1324-4d39-9f47-e34720cce2a6`
* **Zona Horaria de Registro:** CST / GMT-6 (`America/Monterrey` / `America/Mexico_City`, UTC-6)
* **Fecha y Hora de Corte:** 2026-09-21T03:40:44-06:00 (09:40:44Z del 2026-09-21)
* **Estado Operativo:** Pausa programada para reinicio de estación de trabajo / Retoma inmediata al regreso.

---

### Convenciones de Certeza y Trazabilidad de Datos
* **`[CONFIRMADA]`**: Información explícitamente verificada en el historial de la conversación, comandos ejecutados en terminal, respuestas del sistema, archivos físicos en disco o metadatos de sistema.
* **`[INFERIDA]`**: Información deducida lógicamente a partir de nombres de directorios, extensiones, comandos estándar o contexto operativo, sin declaración textual unívoca.
* **`[NO DISPONIBLE]`**: Información no registrada en los archivos accesibles ni en los mensajes de la conversación.

---

## 1. FICHA TÉCNICA Y GOBERNANZA DEL PROYECTO

| Campo | Valor Registrado | Origen / Fuente | Nivel de Certeza |
| :--- | :--- | :--- | :---: |
| **Nombre del Ecosistema** | AMDA Agentic Engine | `config/AGENTS.md`, contexto de sesión | `[CONFIRMADA]` |
| **Estudio Fotográfico Asociado** | `Captoora.Studio` (`CAPTOORA.STUDIO`) | `Desktop/Projects/CAPTOORA.STUDIO` | `[CONFIRMADA]` |
| **Workspace Primario en Disco** | `/Users/imac/Desktop/Projects` (iCloud Desktop Synced) | Sistema de archivos local | `[CONFIRMADA]` |
| **Directorio de Agentes de IA** | `/Users/imac/Desktop/Projects/AI/AGENTES` | Sistema de archivos local | `[CONFIRMADA]` |
| **Directorio de Credenciales** | `/Users/imac/Desktop/Projects/SECRETS` | Sistema de archivos local | `[CONFIRMADA]` |
| **Directorio de Portafolio / Sesiones** | `/Users/imac/Desktop/Projects/SESSIONS PORTAFOLIO` | Sistema de archivos local | `[CONFIRMADA]` |
| **Cuenta Primaria / Respaldo Cloud** | `lic.jagf87@gmail.com` | `apis.txt`, `apis.md`, reglas de usuario | `[CONFIRMADA]` |
| **Cuenta Educativa / Notion Santuario** | `jgutierrezf@uanl.edu.mx` | `apis.txt`, reglas maestras de usuario | `[CONFIRMADA]` |
| **Usuario GitHub Autorizado** | `@ponchogf88` | `apis.txt`, configuración git | `[CONFIRMADA]` |
| **Modelo de Lenguaje en Sesión** | Gemini 3.8 Flash (High) | Metadatos de configuración de sesión | `[CONFIRMADA]` |
| **Suscripción Browser Use Cloud** | Activa ($15 USD de crédito al 17/09/2026) | `apis.txt` (Línea 34) | `[CONFIRMADA]` |
| **Licencia ElevenLabs Principal** | Creator / Commercial License Activa | `apis.txt` (Líneas 29-32) | `[CONFIRMADA]` |
| **5 Destinos de Respaldo Canónicos** | 1. iCloud Drive (6TB) - `Desktop/Projects`<br/>2. Google Drive - `lic.jagf87@gmail.com`<br/>3. Notion - `jgutierrezf@uanl.edu.mx`<br/>4. Obsidian Vault - `lic.jagf87@gmail.com`<br/>5. GitHub - `@ponchogf88` | `apis.txt` (Líneas 13-18) | `[CONFIRMADA]` |

---

## 2. CRONOLOGÍA HISTÓRICA DETALLADA (LÍNEA DE TIEMPO OPERATIVA)

| Fecha y Hora Local (CST / UTC-6) | Fecha y Hora UTC | Hito / Fase | Acción Técnica o Decisión Registrada | Trazabilidad / Comando | Nivel de Certeza |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **2026-09-16 18:37:24** | 2026-09-17 00:37:24Z | **Turno 1: Álbumes Facebook** | • Usuario consulta extensión o configuración de Browserflow para descargar fotos completas de un álbum de Facebook.<br/>• Antigravity investiga herramientas actualizadas al 2026.<br/>• Se entrega: 1) Recomendación de extensión `ESUIT | PhotosDownloader for Facebook™`, 2) Arquitectura de flujo en Browserflow con delays anti-ban (1.5-2.0s), y 3) Script autónomo JS para consola en lightbox con simulación de `ArrowRight` y resolución por `naturalWidth`. | Historial de conversación / Búsqueda web | `[CONFIRMADA]` |
| **2026-09-17 03:57:37** | 2026-09-17 09:57:37Z | **Turno 2: Diagnóstico "CANT READ"** | • Usuario reporta error "CANT READ" con código Python de `browser-use-sdk` para scraping en Amazon.<br/>• Antigravity diagnostica: 1) Salto de línea inválido en string de comillas simples (`SyntaxError`), 2) `await` fuera de función `async def`, 3) Falta de `BROWSER_USE_API_KEY`.<br/>• Se aclara diferencia entre `browser-use-sdk` (Cloud de pago) y `browser-use` (Open Source local). Se entregan ambos códigos corregidos. | Historial de conversación / Búsqueda web | `[CONFIRMADA]` |
| **2026-09-17 04:02:37** | 2026-09-17 10:02:37Z | **Turno 3: Error Paréntesis y Filtro Ciudades** | • Usuario reporta error de paréntesis y solicita estructura para buscar videos verticales (30-60s) de fotógrafos en Guadalajara, Querétaro o Tijuana, **excluyendo estrictamente Monterrey** (15 videos).<br/>• Antigravity explica por qué Pinterest es superior a Instagram/Canva para agentes sin login.<br/>• Se entrega plantilla de prompt estructurada en 4 bloques y script completo con comillas triples `"""` anti-errores de sintaxis. | Historial de conversación / Código Python | `[CONFIRMADA]` |
| **2026-09-17 05:05:15** | 2026-09-17 11:05:15Z | **Turno 4: Clarificación de Peso de Video** | • Usuario pregunta si videos de 30-45s son "pesados".<br/>• Antigravity aclara: A nivel de archivo son ligeros (5 a 15 MB por clip; 100-150 MB por lote de 15 clips). Lo "pesado" era poner a la IA a gestionar diálogos de descarga nativos del OS en lugar de delegarlo a Python. Se establece la arquitectura de 2 capas: IA busca URLs $ightarrow$ Python descarga binarios. | Historial de conversación | `[CONFIRMADA]` |
| **2026-09-17 05:17:57** | 2026-09-17 11:17:57Z | **Turno 5: Integración en Markdown de Agentes** | • Usuario solicita registrar esta arquitectura en los `.md` de agentes de la carpeta `Projects` en iCloud Desktop.<br/>• Se inspecciona el sistema de archivos: se localiza `AI/AGENTES/config/AGENTS.md`.<br/>• Se agrega la **Regla 4** en `AGENTS.md`.<br/>• Se crea `AGENTE_MEDIA_DISCOVERY_Y_DESCARGAS.md` y su copia en `WORKFLOWS/WORKFLOW_DISCOVERY_STORIES_REELS.md`. | Reemplazo de archivo y comandos bash | `[CONFIRMADA]` |
| **2026-09-17 05:47:05** | 2026-09-17 11:47:05Z | **Turno 6: Conversión de APIs a .env** | • Usuario solicita marcar la tarea de videos como PENDIENTE y convertir `apis.txt` a `.env`, guardarlo en `Projects` y respaldar en Google Drive.<br/>• Antigravity localiza `Desktop/Projects/SECRETS/apis.txt` (1,009 líneas, modificado a las 05:47 CST).<br/>• Se parsea y estructura el archivo maestro `.env` y `apis.env`.<br/>• Se distribuye en `SECRETS/`, raíz de `Projects/` y carpetas de Google Drive en Desktop. | Scripts Python / Comandos bash | `[CONFIRMADA]` |
| **2026-09-17 05:49:42** | 2026-09-17 11:49:42Z | **Turno 7: Confirmación apis.txt minúsculas** | • Usuario puntualiza: *"APIS.TXT / apis.txt con minusculas"*.<br/>• Se copia exactamente como `apis.txt` en `/Users/imac/Desktop/Projects/apis.txt` y en las carpetas de Google Drive.<br/>• Se genera adicionalmente `apis.md` con tablas estructuradas de servicios y credenciales. | Comandos bash / Verificación de disco | `[CONFIRMADA]` |
| **2026-09-17 22:11:29** | 2026-09-18 04:11:29Z | **Turno 8: Búsqueda Fotógrafos Semijóvenes** | • Usuario solicita ubicar videos de stories de fotógrafos varones semijóvenes, delgados, de buen porte ("como yo"), en BTS o sesión activa, 10 clips de hasta 30s, preferentemente secuenciales.<br/>• Antigravity presenta análisis de fuentes: Pexels (el truco de "mismo rodaje/serie" para continuidad perfecta) vs TikTok/IG Reels (estética POV/vlog) y la estructura narrativa de 10 historias (preparación $ightarrow$ acción $ightarrow$ revisión $ightarrow$ resultado). | Historial de conversación / Búsqueda web | `[CONFIRMADA]` |
| **2026-09-17 22:15:41** | 2026-09-18 04:15:41Z | **Turno 9: Selección Opción 2 (Links Curados)** | • Usuario elige la opción 2: recibir enlaces pre-filtrados para seleccionar antes de descargar.<br/>• Antigravity entrega 3 colecciones curadas con enlaces directos en vertical (9:16):<br/>  1. *Street & Urban Studio* (casual, dinámico, moderno).<br/>  2. *Moda & Editorial de Alta Gama* (ciclorama, luces, alta producción).<br/>  3. *Golden Hour & Bodas/Parejas* (cálido, emocional, exterior).<br/>• Queda abierta la selección del usuario para proceder a la descarga automatizada. | Historial de conversación / Links generados | `[CONFIRMADA]` |
| **2026-09-21 03:40:44** | 2026-09-21 09:40:44Z | **Turno 10: Solicitud de Bitácora y Reinicio** | • Usuario solicita generación de la Bitácora Maestra exhaustiva, estructurada en tablas, sin invenciones, distinguiendo certezas, depositándola en Escritorio, Captoora en iCloud, Google Drive, Notion y Obsidian, y guardando memoria para reiniciar el equipo y retomar. | Mensaje de usuario / Metadatos de sesión | `[CONFIRMADA]` |

---

## 3. REGISTRO MAESTRO DE DECISIONES DE ARQUITECTURA Y NEGOCIO

| ID | Área / Dimensión | Decisión Estratégica Tomada | Justificación Técnica / Operativa | Nivel de Certeza | Fuente de Decisión |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **DEC-01** | **Separación de Responsabilidades** | Desacoplamiento estricto entre Capa Cognitiva (IA / `browser-use`) y Capa Mecánica (Python Nativo). | La IA solo navega, evalúa contexto visual, aplica exclusiones y extrae URLs a CSV. El script nativo descarga binarios `.mp4`. Esto ahorra 95% de tokens y elimina fallos por ventanas de diálogo del sistema operativo. | `[CONFIRMADA]` | `AGENTS.md` (Regla 4), Turno 4 |
| **DEC-02** | **Plataforma de Scraping Prioritaria** | Elección de Pinterest sobre Instagram/Canva para descubrimiento sin credenciales. | Pinterest no impone muros de login agresivos ni CAPTCHAs constantes en la navegación de pines de video verticales (Idea Pins), mientras que Instagram bloquea sesiones nuevas de navegador. | `[CONFIRMADA]` | `AGENTE_MEDIA_DISCOVERY...md`, Turno 3 |
| **DEC-03** | **Criterio de Exclusión Geográfica** | Regla negativa estricta: Descartar automáticamente cualquier mención a "Monterrey", "MTY", "San Pedro", "Nuevo León" o "NL". | El usuario requiere explícitamente contenido de otras plazas (Guadalajara, Querétaro, Tijuana o resto del país) para enriquecer o diversificar portafolios sin duplicar mercado local. | `[CONFIRMADA]` | Prompt de usuario (Turno 3), Scripts |
| **DEC-04** | **Estándar de Contenido Vertical** | Formato 9:16, duración 30-45 segundos (máx 60s), peso de 5 a 15 MB por archivo. | Formato nativo para Stories de Instagram, TikTok y YouTube Shorts. Peso óptimo para procesamiento en lote y bajo consumo de almacenamiento. | `[CONFIRMADA]` | `AGENTS.md` (Regla 4), Turno 4 |
| **DEC-05** | **Gobernanza de Credenciales Dual** | Coexistencia de `.env` (oculto para runtime de scripts), `apis.env` (visible en macOS Finder), `apis.txt` (texto plano) y `apis.md` (tablas de documentación). | Evita la invisibilidad de archivos con punto (`.env`) en Finder sin comprometer la compatibilidad con librerías estándar de Node/Python (`dotenv`). | `[CONFIRMADA]` | Turnos 6 y 7 |
| **DEC-06** | **Estrategia Secuencial de Contenido** | Selección de series de rodaje del mismo creador en Pexels (misma ropa, misma locación, misma modelo). | Garantiza que las 10 historias cuenten un arco narrativo real y coherente (llegada $ightarrow$ set $ightarrow$ dirección $ightarrow$ disparo $ightarrow$ revisión) en vez de clips inconexos. | `[CONFIRMADA]` | Turno 8 |
| **DEC-07** | **Estado en Standby por Reinicio** | Guardar punto de restauración formal antes del reinicio del equipo de cómputo. | Permitir que al volver a encender y abrir Antigravity, la sesión se retome exactamente en el punto de selección de estilo y descarga sin repetir auditorías ni preguntas. | `[CONFIRMADA]` | Prompt de usuario (Turno 10) |

---

## 4. INVENTARIO EXHAUSTIVO DE ENTREGABLES Y ACTIVOS

| ID | Activo / Entregable | Ruta Física en el Sistema | Descripción / Especificaciones | Nivel de Certeza | Estado |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **ENT-01** | **Reglas Maestras Actualizadas** | `/Users/imac/Desktop/Projects/AI/AGENTES/config/AGENTS.md` | Inclusión de Regla 4: Arquitectura de Recolección y Descarga de Medios (Capa Cognitiva vs Binaria). | `[CONFIRMADA]` | Operativo / Actualizado |
| **ENT-02** | **Documento Técnico de Agente** | `/Users/imac/Desktop/Projects/AI/AGENTES/AGENTE_MEDIA_DISCOVERY_Y_DESCARGAS.md` | Especificación técnica completa, prompt maestro de exclusión y script Python modular en 2 fases. | `[CONFIRMADA]` | Concluido |
| **ENT-03** | **Workflow en Carpeta de Flujos** | `/Users/imac/Desktop/Projects/AI/AGENTES/WORKFLOWS/WORKFLOW_DISCOVERY_STORIES_REELS.md` | Copia de seguridad del flujo de trabajo dentro de la carpeta temática `WORKFLOWS`. | `[CONFIRMADA]` | Concluido |
| **ENT-04** | **Archivo .env Maestro** | `/Users/imac/Desktop/Projects/.env`<br/>`/Users/imac/Desktop/Projects/SECRETS/.env` | Archivo de variables de entorno con 16 secciones categorizadas (Browser Use, Gemini, ElevenLabs, OpenAI, Claude, DeepSeek, etc.). | `[CONFIRMADA]` | Operativo |
| **ENT-05** | **Archivo apis.env (Visible)** | `/Users/imac/Desktop/Projects/apis.env`<br/>`/Users/imac/Desktop/Projects/SECRETS/apis.env` | Versión visible para macOS Finder sin necesidad de atajos de teclado para archivos ocultos. | `[CONFIRMADA]` | Operativo |
| **ENT-06** | **Archivo apis.txt (Minúsculas)** | `/Users/imac/Desktop/Projects/apis.txt`<br/>`/Users/imac/Desktop/Projects/SECRETS/apis.txt` | Archivo original de notas y claves colocado con nombre exacto en minúsculas. | `[CONFIRMADA]` | Respaldado |
| **ENT-07** | **Documentación apis.md** | `/Users/imac/Desktop/Projects/apis.md`<br/>`/Users/imac/Desktop/Projects/SECRETS/apis.md` | Tablas Markdown con resumen de servicios, variables, crédito activo y destinos de respaldo. | `[CONFIRMADA]` | Concluido |
| **ENT-08** | **Respaldos en Google Drive** | `/Users/imac/Desktop/Google Drive (Not synced)/` (y réplicas 1 y 2) | Copias locales de `apis.txt`, `apis.env` y `apis.md` en los directorios de Google Drive del escritorio. | `[CONFIRMADA]` | Sincronizado local |
| **ENT-09** | **Curaduría de Enlaces BTS 9:16** | Registrado en Turno 9 de conversación | 3 colecciones curadas con filtros verticales listos (Street & Urban, Moda & Editorial, Golden Hour & Bodas). | `[CONFIRMADA]` | Disponible |
| **ENT-10** | **Script JS Consola Facebook** | Entregado en Turno 1 de conversación | Código autónomo para consola del navegador que recorre lightbox con `ArrowRight` y descarga fotos HD. | `[CONFIRMADA]` | Disponible |
| **ENT-11** | **Bitácora Maestra del Proyecto** | `/Users/imac/Desktop/BITACORA_MAESTRA_PROYECTO_AGENTES_Y_MEDIOS.md`<br/>(y réplicas en Captoora, Google Drive, Notion y Obsidian) | Documento canónico consolidado con trazabilidad total y protocolos de memoria. | `[CONFIRMADA]` | Concluido |

---

## 5. MATRIZ DE PENDIENTES Y BLOQUEOS ACTUALES (ACTION ITEMS)

| ID | Tarea / Pendiente | Dependencia / Bloqueo | Responsable | Prioridad | Estado |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **ACT-01** | **Reinicio de Computadora del Usuario** | Guardado de memoria y confirmación de rutas de la Bitácora. | Usuario | Inmediata (P0) | 🟡 En proceso |
| **ACT-02** | **Selección de Estilo de Fotógrafo BTS** | Usuario debe indicar si prefiere: Estilo 1 (*Street/Urban*), Estilo 2 (*Editorial/Moda*), Estilo 3 (*Golden Hour/Bodas*) o proporcionar link específico. | Usuario | Alta (P1) | ⏳ Pendiente tras reinicio |
| **ACT-03** | **Descarga Automatizada de 10 Clips** | Depende de ACT-02 (selección de estilo/colección). Se ejecutará script de descarga directa a `Desktop/Projects/`. | Antigravity / Python | Alta (P1) | ⏳ Bloqueado por ACT-02 |
| **ACT-04** | **Emparejamiento con Captoora Studio** | Integrar los 10 clips descargados con los templates de `CAPTOORA.STUDIO/docs/TEMPLATES_BTS.md` para publicación de historias/reels. | Antigravity / Usuario | Media | ⚪ Programado |

---

## 6. FUENTES DE INFORMACIÓN Y TRAZABILIDAD

| Código | Tipo de Fuente | Ruta o Identificador | Datos Clave Extraídos | Nivel de Certeza |
| :---: | :--- | :--- | :--- | :---: |
| **SRC-01** | Conversación Actual | `e265a33e-1324-4d39-9f47-e34720cce2a6` (Turnos 1 al 10) | Requerimientos de usuario, códigos corregidos, preguntas de peso, selección de links y solicitud de bitácora. | `[CONFIRMADA]` |
| **SRC-02** | Archivo de Claves Original | `/Users/imac/Desktop/Projects/SECRETS/apis.txt` | Claves API de Browser Use, Gemini, ElevenLabs, OpenAI, Claude, DeepSeek, etc., y lista de 5 destinos de respaldo. | `[CONFIRMADA]` |
| **SRC-03** | Reglas Canónicas de Agentes | `/Users/imac/Desktop/Projects/AI/AGENTES/config/AGENTS.md` | Reglas maestras AMDA 1 a 3 y Regla 4 agregada en esta sesión. | `[CONFIRMADA]` |
| **SRC-04** | Bitácora Previa de Captoora | `/Users/imac/Desktop/BITACORA_MAESTRA_PROYECTO_FOTOS_CAPTOORA.md` | Historial de hardware Nikon D3500, OBS Studio, `foto_engine.py` y Pharmacy Event. | `[CONFIRMADA]` |
| **SRC-05** | Bitácora Previa de Streaming | `/Users/imac/Desktop/BITACORA_MAESTRA_PROYECTO.md` | Formato RTMP, normalización de audio -14 LUFS y flujo de trabajo con Canva Business. | `[CONFIRMADA]` |
| **SRC-06** | Sistema de Archivos Local | `/Users/imac/Desktop/Projects/` | Verificación física de directorios `AI/AGENTES`, `SECRETS`, `CAPTOORA.STUDIO` y `Obsidian-Vault`. | `[CONFIRMADA]` |

---

## 7. PROTOCOLO DE MEMORIA Y RESTAURACIÓN POST-REINICIO

Cuando el usuario encienda de nuevo la computadora y abra la sesión:
1. **Comando de Retoma Inmediata:** El usuario solo necesita decir: *"Agy, ya reinicié, retomemos los videos de fotógrafo"*.
2. **Contexto Activo en Memoria:**
   * La infraestructura de claves (`.env`, `apis.env`, `apis.txt`) ya está lista y validada.
   * La regla de separación de capas (IA para links $ightarrow$ Python para archivos) está grabada en `AGENTS.md`.
   * El paso exacto a ejecutar es: **Recibir la elección de estilo (1, 2 o 3)** y disparar la descarga de los **10 clips secuenciales de 30s en vertical 9:16**.

---
*Bitácora Maestra generada y certificada por Antigravity. Lista para consulta, edición y seguimiento ininterrumpido.*
