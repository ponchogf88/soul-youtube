# AGRADECIMIENTO SINCERO — instrucciones para agentes

Léete esto entero antes de preguntar. No preguntes “dónde está el canal”, “qué onda con YouTube” ni “es el de métricas de Chuy”. Este archivo es la fuente de verdad del proyecto.

**Dueño:** Jesús Alfonso Gutiérrez Flores (Poncho).
**Canal:** [Agradecimiento Sincero](https://www.youtube.com/channel/UCABE05zuxJifGDhnuB5dGUg) · ID `UCABE05zuxJifGDhnuB5dGUg`
**Playlist oficial:** `PLLmrH1ayKBko`
**Actualizado:** 2026-09-03

**GitHub:** no hay repo de este canal. Los videos van a YouTube. Docs y código de producción viven en esta carpeta y en `~/agencia-core` (local). No crees un repo ni subas `.mp4` ni `youtube_token.json`.

**Producción (2026-09-03):** los videos se arman en **Canva Business** (cuenta de paga, no Education). Templates + stock comercial + voz. La cuenta de maestro de Canva no se usa para este canal.

---

## Dónde está (ruta exacta)

La carpeta del canal **termina con un espacio**. No la renombres. No la muevas. No la dupliques.

```
~/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO /
```

| Qué | Ruta |
|---|---|
| Este brief | `…/AGRADECIMIENTO SINCERO /AGENTS.md` |
| README humano | `…/AGRADECIMIENTO SINCERO /README.md` |
| Investigación (Galeano + Top 10) | `…/INVESTIGACIONES/` |
| Logos y miniaturas | `…/LOGOS AND THUMBNAILS/` |
| Videos renderizados | `…/VIDEOS/` |
| Playbook de crecimiento | `~/agencia-core/docs/PLAYBOOK_AGRADECIMIENTO_SINCERO.md` |
| Pipeline (voz, render, upload) | `~/agencia-core/scripts/sacred_video_composer.py` |
| Servicio local de render | `~/agencia-core/scripts/sacred_service.py` · puerto `8765` |
| Orquestador devocionales diarios | `~/agencia-core/scripts/trigger_daily_devotional.py` |
| Blueprint n8n | `~/agencia-core/blueprints/n8n_youtube_elevenlabs_video_pipeline.json` |
| Token YouTube | `~/agencia-core/youtube_token.json` |
| n8n local | `~/.n8n/` · workflow activo = webhook `POST /webhook/auto-video-publish` |

Esto **no** es `~/Claude/Scheduled/revision-metricas-youtube`. Esa skill es el otro canal (Chuy / automatización IA para pymes). No la uses aquí.

---

## Inspiración: Galeano Con Dios

El modelo de referencia es **Galeano Con Dios** (`@GaleanoConDios`). Se escribe **Galeano**, no Galiano.

Se copia **la máquina**, no la marca:

- Paisajes lentos, amaneceres, iglesias, cruz, naturaleza.
- Voz cálida de oración, no sermón acelerado.
- Ritual diario. La gente lo pone de compañía (desayuno / dormir), no de cine.
- Miniatura: 3–5 palabras gordas, oro `#FFD700` sobre azul noche.
- Comentarios como muro de fe: “escribe AMÉN y el nombre de tu familia”.

**Prohibido en nuestro contenido:**

- Decir “Galeano”, “Galeano Con Dios” o su slogan en título, descripción, voz, miniatura o comentarios.
- Subir videos de ~30–45 segundos y llamarlos “oración”. Eso no es este canal.
- **Empaquetar como "Reto de 7 Días", "Día 1", "Día 2" o numerar días:** PROHIBIDO. Los suscriptores nuevos sienten que "llegaron tarde" o que el contenido caducó. Cada video es un refugio diario, continuo y atemporal (Oración de la Mañana, Oración de la Noche, Oración por la Familia).

Nuestra diferencia: voz más joven, eje en **gratitud sincera**, no en milagro/miedo.

---

## Tres formatos. No hay un cuarto “por ahora”.

Cada pieza de contenido de este canal es **una** de estas tres. Si vas a generar, editar o subir, dime cuál.

| # | Formato | Duración | Rol | Cuándo |
|---|---|---|---|---|
| 1 | **Short** | **60 segundos** | Anzuelo. Un momento fuerte de la oración. Vertical 9:16. | Se recorta del 15 min o del largo. No es el producto. |
| 2 | **Oración con el Señor** | **15 minutos** | Oración que se puede terminar. Retención. Descubrimiento. | Un video de oración completa, no un clip. |
| 3 | **Estar con Dios** | **45 a 60 minutos** | Compañía. Watch time. Fondo para iniciar o cerrar el día. | **Mañana y noche.** |

### Largos (formato 3) — dos intenciones

- **Mañana (~6:00 AM México):** agradecer y pedir un excelente día. Iniciar con Dios.
- **Noche (~10:00 PM México):** dar gracias por el día que termina. Paz para dormir.

No son lives. Son videos pregrabados. No inventes un live a las 11 PM con 2 suscriptores.

Horarios por defecto (México):

- Largo mañana → estreno **06:00**
- Oración 15 min → puede ir con la mañana o como pieza sola
- Largo noche → estreno **22:00**
- Short → **11:00** o **17:00**, con enlace al largo

No uses “mejor hora genérica de YouTube” (2–4 PM). Este nicho tiene hora ritual.

---

## Qué está bien / qué no está bien hoy

Hecho:

- Canal creado, OAuth YouTube listo, 3 videos públicos (intro, 1 sep, Día 2).
- Sacred service puede estar en `:8765`.
- Estudios de Galeano y Top 10 en `INVESTIGACIONES/`.

Roto o incompleto (no lo ignores):

- Los renders actuales duran **27–47 segundos**. Eso no cumple ninguno de los 3 formatos. **No publiques otro video corto “para cumplir el horario”.**
- n8n **no tiene cron**. El workflow es un webhook. n8n a menudo está apagado. No asumas que a las 5 o a las 6 “se dispara solo”.
- La cuenta debe estar **verificada por teléfono** para subir >15 min (el largo de 45–60 min lo necesita). No hace falta más suscriptores para 5 o 15 min.
- El pipeline todavía puede colar marca de Galeano en la descripción: quítalo si lo ves.

---

## Cómo deben comportarse los agentes

1. No preguntes dónde está el proyecto. Está arriba.
2. No mezcles este canal con métricas de Chuy, AMDA, Dynamic Punch o WhatsOrb.
3. No dispares n8n / upload a YouTube de un video que no sea Short 60s, oración 15 min, o largo 45–60 min.
4. Si vas a cambiar horarios, formatos o la inspiración de Galeano, es decisión estructural: anótala en `~/Projects/agent-ops-hub/ops/decisions_log.md` y actualiza **este archivo**.
5. No reorganices `~/Desktop/Projects/YOUTUBE CHANNEL/` sin permiso explícito del humano.

---

## 👑 REGLAS DE ORO DE TIPOGRAFÍA Y REVERENCIA (TATUADO EN EL PROYECTO)

1. **LÍNEAS MÁS BOLD Y CON BORDE NEGRO:**
   - Cero líneas delgadas o frágiles. Tipografía pesada, extra-bold (Anton, Montserrat ExtraBold, League Gothic).
   - Siempre con **borde negro grueso (stroke/outline: 5.5 a 7.0)** y sombra para garantizar contraste absoluto.

2. **PALABRAS SAGRADAS — SIEMPRE EN MAYÚSCULAS Y COLOR AZUL REY DIVINO:**
   Por respeto y reverencia al Creador, NUNCA van en minúsculas:
   - **`JESÚS`**
   - **`SEÑOR`**
   - **`PADRE`**
   - **`DIOS`**
   - **`ESPÍRITU`**
   - **Color obligatorio:** **Azul Rey Celestial** (`#2563EB` en web/diseño; `&H00F6823B&` en subtítulos ASS).

3. **LA ÚLTIMA PALABRA DE CADA PÁRRAFO O SUBTÍTULO — SIEMPRE COLOR MORADO:**
   - La última palabra de cada frase o línea en pantalla DEBE ser de **Color Morado Púrpura Celestial** (`#A855F7` en web/diseño; `&H00F755A8&` en subtítulos ASS).

