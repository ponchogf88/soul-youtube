#!/usr/bin/env python3
"""Auditoría visual — canales de oración. PDF landscape, image-first."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path("/Users/user/Desktop/AUDITORIA_VISUAL_CANALES_ORACION_20260905.pdf")
PAGE = landscape(letter)  # 792 x 612
W, H = PAGE

AS = Path("/Users/user/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO ")
EG = Path("/Users/user/Desktop/Projects/YOUTUBE CHANNEL/ETERNALLY GRATEFUL")
GOD = Path("/Users/user/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS")
IMG = Path("/Users/user/.grok/sessions/%2FUsers%2Fuser/01a07248-f00e-7263-a595-5ba3ac41673d/images")

SUNRISE = IMG / "1.jpg"
NIGHT = IMG / "2.jpg"
SPLIT = IMG / "3.jpg"
BANNER_AS = AS / "LOGOS AND THUMBNAILS" / "Captura de pantalla 2026-09-02 a la(s) 9.58.01 a.m..png"
# Finder may use NARROW NO-BREAK SPACE in screenshot names; glob fallback below
THUMB_OFFICIAL = AS / "LOGOS AND THUMBNAILS" / "Miniatura Oficial YouTube - ABRE CAMINOS (AGRADECIMIENTO SINCERO).png"
THUMB_D1 = AS / "day_01" / "THUMB_MASTER_1788361141.jpg"
THUMB_D2 = AS / "day_02" / "THUMB_MASTER_1788361860.jpg"
THUMB_PILOTO = AS / "VIDEOS" / "ORACION_15M_MANANA_PILOTO_THUMB.jpg"
THUMB_EG = EG / "LOGOS AND THUMBNAILS" / "Miniatura_Oficial_YouTube_Eternally_Grateful.png"
THUMB_BI = GOD / "MINIATURA_DEVOCIONAL_11MIN_CRISTINA_CAMPOS.jpg"
AVATAR_EG = EG / "LOGOS AND THUMBNAILS" / "channel_avatar.png"
BANNER_EG = EG / "LOGOS AND THUMBNAILS" / "banner_youtube_eternally_grateful.png"

C_BG = HexColor("#0A0A0B")
C_PANEL = HexColor("#121214")
C_PANEL2 = HexColor("#18181C")
C_LINE = HexColor("#2A2A2E")
C_TEXT = HexColor("#F4F2EE")
C_MUTED = HexColor("#AAA8A4")
C_GOLD = HexColor("#FFD700")
C_RED = HexColor("#FF5A4A")
C_GREEN = HexColor("#7CFF6B")
C_BLUE = HexColor("#2563EB")
C_PURPLE = HexColor("#A855F7")
C_AMBER = HexColor("#FFB020")

pdfmetrics.registerFont(TTFont("A", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("AB", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))


def find_banner():
    folder = AS / "LOGOS AND THUMBNAILS"
    for p in folder.iterdir():
        if p.suffix.lower() == ".png" and "9.58.01" in p.name:
            return p
    return BANNER_AS


def draw_bg(c):
    c.setFillColor(C_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def img(c, path, x, y, w, h, preserve=True):
    p = Path(path)
    if not p.exists():
        c.setFillColor(C_PANEL)
        c.roundRect(x, y, w, h, 8, fill=1, stroke=0)
        return
    ir = ImageReader(str(p))
    iw, ih = ir.getSize()
    if preserve:
        scale = min(w / iw, h / ih)
        nw, nh = iw * scale, ih * scale
        c.drawImage(ir, x + (w - nw) / 2, y + (h - nh) / 2, nw, nh, preserveAspectRatio=True, mask="auto")
    else:
        c.drawImage(ir, x, y, w, h, preserveAspectRatio=False, mask="auto", anchor="c")


def cover_image(c, path):
    ir = ImageReader(str(path))
    iw, ih = ir.getSize()
    scale = max(W / iw, H / ih)
    nw, nh = iw * scale, ih * scale
    c.drawImage(ir, (W - nw) / 2, (H - nh) / 2, nw, nh, preserveAspectRatio=True, mask="auto")


def footer(c, n, total=12):
    c.setStrokeColor(C_LINE)
    c.setLineWidth(0.4)
    c.line(36, 22, W - 36, 22)
    c.setFillColor(C_MUTED)
    c.setFont("A", 7.5)
    c.drawString(36, 10, "AUDITORÍA OPERATIVA  ·  5 SEP 2026  ·  FUENTE LOCAL + YOUTUBE API")
    c.drawRightString(W - 36, 10, f"{n:02d}  /  {total:02d}")


def kicker(c, text, x, y, color=C_GOLD):
    c.setFillColor(color)
    c.setFont("AB", 8)
    c.drawString(x, y, text.upper())


def h1(c, text, x, y, size=26):
    c.setFillColor(C_TEXT)
    c.setFont("AB", size)
    c.drawString(x, y, text)


def muted(c, text, x, y, size=9):
    c.setFillColor(C_MUTED)
    c.setFont("A", size)
    c.drawString(x, y, text)


def card(c, x, y, w, h, radius=10, fill=None, stroke=None, sw=0.6):
    c.setFillColor(fill or C_PANEL)
    c.setStrokeColor(stroke or C_LINE)
    c.setLineWidth(sw)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def pill(c, x, y, w, h, text, bg, fg=None, size=8):
    c.setFillColor(bg)
    c.roundRect(x, y, w, h, h / 2, fill=1, stroke=0)
    c.setFillColor(fg or C_BG)
    c.setFont("AB", size)
    c.drawCentredString(x + w / 2, y + (h - size) / 2 + 0.5, text)


def bullet(c, x, y, text, color=C_GOLD, size=9.5, maxw=340):
    c.setFillColor(color)
    c.circle(x + 3, y + 3, 2.2, fill=1, stroke=0)
    c.setFillColor(C_TEXT)
    c.setFont("A", size)
    # wrap
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, "A", size) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for i, line in enumerate(lines[:4]):
        c.drawString(x + 12, y - i * 13, line)
    return 14 + max(0, len(lines) - 1) * 13


def gold_rule(c, x, y, w=72):
    c.setStrokeColor(C_GOLD)
    c.setLineWidth(1.4)
    c.line(x, y, x + w, y)


# ---------------------------------------------------------------------------
# PAGES
# ---------------------------------------------------------------------------

def page_cover(c):
    cover_image(c, SUNRISE)
    # dark overlays
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.35))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.82))
    c.rect(0, 0, W, 250, fill=1, stroke=0)
    # top bar
    c.setFillColor(C_GOLD)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)
    kicker(c, "AUDITORÍA OPERATIVA  ·  CANALES DE ORACIÓN", 40, H - 36)
    h1(c, "La máquina no está corriendo.", 40, 168, 32)
    muted(c, "Agradecimiento Sincero  ·  Eternally Grateful  ·  Oración bilingüe", 40, 142, 12)
    gold_rule(c, 40, 128, 90)
    # pills
    pill(c, 40, 78, 150, 22, "0 DÍAS ADELANTE", C_RED, white, 8)
    pill(c, 200, 78, 150, 22, "4 VIDEOS EN YT", C_AMBER, C_BG, 8)
    pill(c, 360, 78, 170, 22, "n8n APAGADO DESDE 2 SEP", C_PANEL, C_GOLD, 8)
    pill(c, 540, 78, 210, 22, "CANVA CALENDARIO: NO ESTÁ", C_PANEL, C_TEXT, 8)
    c.setFillColor(C_MUTED)
    c.setFont("A", 8)
    c.drawString(40, 44, "Fecha de corte  5 septiembre 2026")
    c.drawString(40, 30, "YouTube API en vivo  ·  disco local  ·  n8n sqlite  ·  Canva MCP")
    c.drawRightString(W - 40, 44, "Poncho  ·  Santuario")
    footer(c, 1)


def page_veredicto(c):
    draw_bg(c)
    kicker(c, "01  ·  VEREDICTO EN 30 SEGUNDOS", 36, H - 48)
    h1(c, "Papel sí. Publicación no.", 36, H - 78, 24)
    gold_rule(c, 36, H - 90)

    # three giant metrics
    metrics = [
        ("4", "videos públicos", "3 de 4 duran 33–46 s", C_RED),
        ("3", "suscriptores", "14 vistas sumadas", C_AMBER),
        ("0", "días adelante", "hoy es 5 sep, último n8n = 2 sep", C_RED),
    ]
    x = 36
    for num, label, sub, col in metrics:
        card(c, x, 390, 232, 130)
        c.setFillColor(col)
        c.setFont("AB", 42)
        c.drawString(x + 18, 468, num)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 11)
        c.drawString(x + 18, 440, label.upper())
        c.setFillColor(C_MUTED)
        c.setFont("A", 8.5)
        c.drawString(x + 18, 418, sub)
        x += 246

    # three channels
    channels = [
        ("ES", "Agradecimiento Sincero", "Español  ·  LATAM / MX", "VIVO en YouTube", "Canal creado 2 sep  ·  @agradecimientosincero", C_GOLD, THUMB_OFFICIAL),
        ("EN", "Eternally Grateful", "Inglés  ·  US / global", "CARPETA SÍ  ·  YT NO AUDITADO", "Creado 4 sep  ·  day_01 vacío", C_BLUE, THUMB_EG),
        ("ES+EN", "Oración bilingüe", "Español a inglés", "SIN CARPETA PROPIA", "1 piloto 11 min Cristina Campos", C_PURPLE, THUMB_BI),
    ]
    x = 36
    for code, name, market, status, note, col, thumb in channels:
        card(c, x, 70, 232, 300)
        # thumb
        c.saveState()
        p = c.beginPath()
        p.roundRect(x + 10, 248, 212, 112, 8)
        c.clipPath(p, stroke=0)
        img(c, thumb, x + 10, 248, 212, 112, preserve=False)
        c.restoreState()
        pill(c, x + 16, 218, 58, 16, code, col, C_BG, 7)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 11)
        c.drawString(x + 16, 196, name)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        c.drawString(x + 16, 180, market)
        y = 154
        for b in [status, note]:
            y -= bullet(c, x + 16, y, b, col, 8.5, 190)
        x += 246
    footer(c, 2)


def page_orden(c):
    draw_bg(c)
    kicker(c, "02  ·  CÓMO ESTÁ ESCRITA LA ORDEN", 36, H - 48)
    h1(c, "La directriz es clara. El código no la obedece.", 36, H - 78, 22)
    gold_rule(c, 36, H - 90)
    muted(c, "Fuente de verdad: AGENTS.md  ·  carpeta con espacio al final  ·  no mezclar con métricas de Chuy", 36, H - 108)

    # left: commandments
    card(c, 36, 70, 360, 400)
    kicker(c, "LO QUE TÚ ORDENASTE", 52, 448)
    rules = [
        "Solo 3 formatos: Short 60 s  ·  oración 15 min  ·  largo 45–60 min.",
        "Prohibido subir clips de 27–47 s y llamarlos oración.",
        "Prohibido empaquetar como Reto de 7 Días / Día 1 / Día 2.",
        "Horario ritual México: 06:00 mañana  ·  22:00 noche  ·  Short 11:00 o 17:00.",
        "Palabras sagradas SIEMPRE en MAYÚSCULAS y azul rey #2563EB.",
        "Última palabra de cada línea en morado #A855F7.",
        "Nunca escribir Galeano en título, voz, miniatura o descripción.",
        "Canva Business (de paga), no Education. Stock comercial.",
    ]
    y = 420
    for r in rules:
        y -= bullet(c, 52, y, r, C_GOLD, 9, 318) + 6

    # right: format tiles with images
    # short
    card(c, 412, 340, 344, 130)
    c.saveState()
    p = c.beginPath()
    p.roundRect(424, 352, 110, 106, 8)
    c.clipPath(p, stroke=0)
    img(c, SUNRISE, 424, 352, 110, 106, preserve=False)
    c.restoreState()
    pill(c, 548, 430, 70, 16, "FORMATO 1", C_GOLD, C_BG, 7)
    c.setFillColor(C_TEXT)
    c.setFont("AB", 13)
    c.drawString(548, 404, "Short  60 s")
    c.setFillColor(C_MUTED)
    c.setFont("A", 8.5)
    c.drawString(548, 386, "Vertical 9:16  ·  anzuelo")
    c.drawString(548, 370, "Se recorta del 15 min o del largo")
    c.drawString(548, 354, "No es el producto")

    card(c, 412, 200, 344, 126)
    c.saveState()
    p = c.beginPath()
    p.roundRect(424, 212, 110, 102, 8)
    c.clipPath(p, stroke=0)
    img(c, find_banner(), 424, 212, 110, 102, preserve=False)
    c.restoreState()
    pill(c, 548, 288, 70, 16, "FORMATO 2", C_BLUE, white, 7)
    c.setFillColor(C_TEXT)
    c.setFont("AB", 13)
    c.drawString(548, 262, "Oración  15 min")
    c.setFillColor(C_MUTED)
    c.setFont("A", 8.5)
    c.drawString(548, 244, "Horizontal  ·  se puede terminar")
    c.drawString(548, 228, "Retención y descubrimiento")
    c.drawString(548, 212, "Gate código: 14:00–16:00")

    card(c, 412, 70, 344, 116)
    c.saveState()
    p = c.beginPath()
    p.roundRect(424, 82, 110, 92, 8)
    c.clipPath(p, stroke=0)
    img(c, NIGHT, 424, 82, 110, 92, preserve=False)
    c.restoreState()
    pill(c, 548, 158, 70, 16, "FORMATO 3", C_PURPLE, white, 7)
    c.setFillColor(C_TEXT)
    c.setFont("AB", 13)
    c.drawString(548, 132, "Estar con Dios  45–60")
    c.setFillColor(C_MUTED)
    c.setFont("A", 8.5)
    c.drawString(548, 114, "Compañía mañana / noche")
    c.drawString(548, 98, "Watch time hacia 4,000 horas")
    c.drawString(548, 82, "YouTube >15 min = teléfono verificado")
    footer(c, 3)


def page_flujo(c):
    draw_bg(c)
    kicker(c, "03  ·  FLUJO DE CREACIÓN", 36, H - 48)
    h1(c, "Así se diseñó. Así está hoy.", 36, H - 78, 24)
    gold_rule(c, 36, H - 90)

    # designed row
    kicker(c, "FLUJO DISEÑADO", 36, 500, C_GREEN)
    steps = [
        ("1", "Calendario\n30 días"),
        ("2", "Guion +\nversículo"),
        ("3", "Voz\nElevenLabs"),
        ("4", "Paisajes\nCanva / FFmpeg"),
        ("5", "Subtítulos\nASS"),
        ("6", "Miniatura\n3–5 palabras"),
        ("7", "n8n cron\n06:00 / 22:00"),
        ("8", "YouTube\n+ muro AMÉN"),
    ]
    x = 36
    for i, (n, label) in enumerate(steps):
        card(c, x, 400, 84, 86, 8)
        c.setFillColor(C_GOLD)
        c.setFont("AB", 11)
        c.drawCentredString(x + 42, 462, n)
        c.setFillColor(C_TEXT)
        c.setFont("A", 7)
        for j, line in enumerate(label.split("\n")):
            c.drawCentredString(x + 42, 444 - j * 11, line)
        if i < len(steps) - 1:
            c.setFillColor(C_GOLD)
            c.setFont("AB", 12)
            c.drawString(x + 86, 436, "›")
        x += 94

    # real row
    kicker(c, "FLUJO REAL  ·  5 SEP 2026", 36, 370, C_RED)
    real = [
        ("CSV local\nSÍ existe", C_GREEN),
        ("Guiones\nparciales", C_AMBER),
        ("Voces\nmuestras", C_AMBER),
        ("Renders\n33–46 s", C_RED),
        ("ASS sí\ntruncado", C_AMBER),
        ("Thumbs\nDÍA 1 + 5 AM", C_RED),
        ("n8n\nAPAGADO", C_RED),
        ("YT 4 videos\n1 válido 5:28", C_AMBER),
    ]
    x = 36
    for i, (label, col) in enumerate(real):
        card(c, x, 270, 84, 86, 8, stroke=col)
        c.setFillColor(col)
        c.circle(x + 42, 336, 5, fill=1, stroke=0)
        c.setFillColor(C_TEXT)
        c.setFont("A", 7)
        for j, line in enumerate(label.split("\n")):
            c.drawCentredString(x + 42, 318 - j * 11, line)
        if i < len(real) - 1:
            c.setFillColor(C_LINE)
            c.setFont("AB", 12)
            c.drawString(x + 86, 306, "›")
        x += 94

    # bottom diagnosis
    card(c, 36, 70, 720, 180)
    kicker(c, "DÓNDE SE ROMPE", 52, 224)
    breaks = [
        "n8n es un webhook, no un cron. scheduled_task = 0. El proceso n8n no está corriendo hoy.",
        "sacred_service.py (:8765) está apagado. Sin él, el webhook no renderiza.",
        "Cero LaunchAgents de oración / YouTube / sacred. Nada se dispara solo a las 6:00.",
        "trigger_daily_devotional.py sigue hablando de «Reto de 7 Días» — prohibido en AGENTS.md.",
        "Default de n8n: título «DÍA 1: ABRE CAMINOS». Eso viola la orden de no numerar días.",
        "Canva MCP de esta sesión apunta a otra cuenta (CVs, fotos). Cero carpeta «Agradecimiento Sincero».",
    ]
    y = 200
    for b in breaks:
        y -= bullet(c, 52, y, b, C_RED, 9, 680) + 2
    footer(c, 4)


def page_maquina(c):
    draw_bg(c)
    kicker(c, "04  ·  ESTADO DE LA MÁQUINA", 36, H - 48)
    h1(c, "Se encendió el 2 de septiembre. Se apagó el mismo día.", 36, H - 78, 20)
    gold_rule(c, 36, H - 90)

    items = [
        ("n8n local", "APAGADO", "Workflow «YouTube Auto-Pilot» marcado active=1 en sqlite, pero el proceso no vive.", C_RED),
        ("Webhook", "EXISTE", "POST /webhook/auto-video-publish  ·  sin daemon no recibe nada.", C_AMBER),
        ("Cron / schedule", "NO HAY", "scheduled_task = 0  ·  scheduled_job = 0  ·  AGENTS.md ya lo advertía.", C_RED),
        ("Sacred :8765", "APAGADO", "El compositor local no escucha. n8n no tiene a quién pegarle.", C_RED),
        ("LaunchAgent", "NO HAY", "Cero plists de oración / YouTube / sacred / n8n en ~/Library/LaunchAgents.", C_RED),
        ("Última corrida", "2 SEP 04:11", "7 ejecuciones totales: 4 error + 3 success. Luego silencio 3 días.", C_RED),
        ("YouTube OAuth", "VIVE", "Token se refrescó hoy. El canal responde. El cuello no es login.", C_GREEN),
        ("Gate de duración", "EN CÓDIGO", "as_formats.py exige 57–63 s / 14–16 min / 45–60 min. Los day_01–05 no pasan.", C_AMBER),
    ]
    positions = [(36, 292), (228, 292), (420, 292), (612, 292), (36, 70), (228, 70), (420, 70), (612, 70)]
    for (title, status, note, col), (x, y) in zip(items, positions):
        card(c, x, y, 180, 188)
        c.setFillColor(col)
        c.circle(x + 22, y + 162, 6, fill=1, stroke=0)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 9)
        c.drawString(x + 36, y + 158, title.upper())
        pill(c, x + 14, y + 122, 152, 22, status, col, C_BG, 8)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        words = note.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 8) <= 150:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y + 100
        for line in lines[:5]:
            c.drawString(x + 14, yy, line)
            yy -= 13
    footer(c, 5)


def page_youtube(c):
    draw_bg(c)
    kicker(c, "05  ·  YOUTUBE EN VIVO  ·  5 SEP 2026", 36, H - 48)
    h1(c, "@agradecimientosincero  ·  3 suscriptores  ·  4 videos", 36, H - 78, 18)
    gold_rule(c, 36, H - 90)

    videos = [
        ("5:28", "HAZ ESTA ORACIÓN AL DESPERTAR…", "4 sep  ·  público", "5 vistas  ·  3 likes  ·  3 comments", "ÚNICO que se acerca a oración", C_GREEN, "AkiQT3CUgOo", THUMB_PILOTO if False else THUMB_OFFICIAL),
        ("0:33", "SANA TU MENTE HOY", "2 sep  ·  público", "2 vistas  ·  1 like  ·  1 comment", "HORIZONTAL CORTO  ·  no es formato", C_RED, "mbhbQLktAY4", THUMB_D2),
        ("0:46", "BIENVENIDO A AGRADECIMIENTO SINCERO", "2 sep  ·  público", "3 vistas  ·  2 likes  ·  2 comments", "INTRO  ·  no es los 3 formatos", C_AMBER, "90FHwQp3fN8", find_banner()),
        ("0:34", "ORACIÓN DEL 1 DE SEPTIEMBRE", "2 sep  ·  público", "4 vistas  ·  2 likes  ·  1 comment", "HORIZONTAL CORTO  ·  no publiques más así", C_RED, "iojQEROVCvM", THUMB_D1),
    ]
    x = 36
    for dur, title, when, stats, flag, col, vid, thumb in videos:
        card(c, x, 90, 174, 400)
        c.saveState()
        p = c.beginPath()
        p.roundRect(x + 8, 330, 158, 148, 8)
        c.clipPath(p, stroke=0)
        img(c, thumb, x + 8, 330, 158, 148, preserve=False)
        c.restoreState()
        pill(c, x + 12, 300, 70, 18, dur, col, C_BG, 8)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 8.5)
        # wrap title
        words = title.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "AB", 8.5) <= 150:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = 278
        for line in lines[:3]:
            c.drawString(x + 12, yy, line)
            yy -= 12
        c.setFillColor(C_MUTED)
        c.setFont("A", 7.5)
        c.drawString(x + 12, 228, when)
        c.drawString(x + 12, 214, stats)
        c.setFillColor(col)
        c.setFont("A", 7.5)
        words = flag.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 7.5) <= 150:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = 190
        for line in lines:
            c.drawString(x + 12, yy, line)
            yy -= 11
        c.setFillColor(C_MUTED)
        c.setFont("A", 6.5)
        c.drawString(x + 12, 110, vid)
        x += 186

    card(c, 36, 28, 720, 52)
    c.setFillColor(C_GOLD)
    c.setFont("AB", 9)
    c.drawString(52, 58, "FALTA EN EL CANAL")
    c.setFillColor(C_TEXT)
    c.setFont("A", 9)
    c.drawString(52, 40, "Cero Shorts de 60 s   ·   Cero oraciones de 15 min   ·   Cero largos 45–60 min   ·   El piloto 15 min sigue local, marcado «NO subir aún».")
    footer(c, 6)


def page_thumbs(c):
    draw_bg(c)
    kicker(c, "06  ·  MINIATURAS  ·  LO QUE SÍ ENTREGARON", 36, H - 48)
    h1(c, "El pulido no llegó. Las thumbs rompen la orden.", 36, H - 78, 20)
    gold_rule(c, 36, H - 90)

    samples = [
        (THUMB_OFFICIAL, "Oficial «ABRE CAMINOS»", "Dice RETO DE 7 DÍAS y 5:00 AM. Ambos prohibidos."),
        (THUMB_D1, "Pipeline day_01", "«DÍA 1» + texto cortado + 5:00 AM. Cero paisaje."),
        (THUMB_D2, "Pipeline day_02", "Misma plantilla. «DÍA 2». Misma hora vieja."),
        (THUMB_PILOTO, "Piloto 15 min", "Ya no dice Día, pero sigue 5:00 AM y se corta el título."),
        (THUMB_EG, "Eternally Grateful", "Inglés pegado encima de español. Layout roto."),
        (THUMB_BI, "Bilingüe Cristina", "Única que se ve canal: paisaje + 3–5 palabras gordas."),
    ]
    positions = [
        (36, 278), (290, 278), (544, 278),
        (36, 36), (290, 36), (544, 36),
    ]
    for (path, title, note), (x, y) in zip(samples, positions):
        card(c, x, y, 244, 228)
        c.saveState()
        p = c.beginPath()
        p.roundRect(x + 10, y + 78, 224, 138, 8)
        c.clipPath(p, stroke=0)
        img(c, path, x + 10, y + 78, 224, 138, preserve=False)
        c.restoreState()
        c.setFillColor(C_TEXT)
        c.setFont("AB", 8)
        c.drawString(x + 12, y + 58, title.upper())
        c.setFillColor(C_MUTED)
        c.setFont("A", 7.5)
        words = note.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 7.5) <= 220:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y + 42
        for line in lines[:3]:
            c.drawString(x + 12, yy, line)
            yy -= 11
    footer(c, 7)


def page_calendario(c):
    draw_bg(c)
    kicker(c, "07  ·  CALENDARIO Y ADELANTO", 36, H - 48)
    h1(c, "Hay un mes escrito. No hay un mes producido.", 36, H - 78, 20)
    gold_rule(c, 36, H - 90)

    # left status
    cards = [
        ("Canva Business", "NO ESTÁ", "Pediste calendario de publicaciones en Canva. En la cuenta conectada a esta sesión no hay carpeta ni diseños de Agradecimiento Sincero. Lo que hay: CVs, fotos, posts de IA.", C_RED),
        ("CSV 30 días", "SÍ, LOCAL", "CALENDARIO_30_DIAS_CANVA_BULK.csv — 30 filas ES + EN, versículo, hook, miniatura. Sirve para Bulk Create. Nadie lo subió a Canva.", C_GREEN),
        ("PDF calendario", "SÍ, LOCAL", "PROYECTO_CALENDARIO_CANVA_ORACIONES_MES1.pdf generado el 4 sep. Papel. No programa YouTube.", C_AMBER),
        ("Carpetas day_XX", "5 DE 30", "day_01 a day_05, todas fechadas 2 sep 09:49. Mismo lote. day_06…day_30 no existen. EG day_01 está vacío.", C_RED),
    ]
    y = 430
    for title, st, note, col in cards:
        card(c, 36, y, 360, 88)
        pill(c, 48, y + 58, 110, 18, st, col, C_BG, 7)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 10)
        c.drawString(170, y + 62, title)
        c.setFillColor(C_MUTED)
        c.setFont("A", 7.5)
        words = note.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 7.5) <= 328:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y + 42
        for line in lines[:3]:
            c.drawString(48, yy, line)
            yy -= 11
        y -= 96

    # right: week 1 calendar visual
    card(c, 412, 70, 344, 448)
    kicker(c, "SEMANA 1 DEL CSV  ·  ESTADO REAL", 428, 492)
    week = [
        ("01  Lun", "Largo 45m + Short", "ABRE CAMINOS", "NO"),
        ("02  Mar", "Largo 45m + Short", "DIOS SANA TU CASA", "NO"),
        ("03  Mié", "Oración 15m + Short", "MULTIPLICA TU SUSTENTO", "NO"),
        ("04  Jue", "Largo noche 45m", "PAZ PARA DORMIR", "NO"),
        ("05  Vie", "Largo 45m + Short", "PROTEGE A MIS HIJOS", "NO"),
        ("06  Sáb", "Oración 15m + Short", "GRACIAS SEÑOR", "NO"),
        ("07  Dom", "Largo 60m + Short", "DOMINGO CON DIOS", "NO"),
    ]
    yy = 460
    for day, fmt, thumb, st in week:
        c.setFillColor(C_PANEL2)
        c.roundRect(428, yy - 18, 312, 36, 6, fill=1, stroke=0)
        c.setFillColor(C_GOLD)
        c.setFont("AB", 8)
        c.drawString(438, yy - 2, day)
        c.setFillColor(C_TEXT)
        c.setFont("A", 7.5)
        c.drawString(500, yy - 2, thumb)
        c.setFillColor(C_MUTED)
        c.setFont("A", 6.5)
        c.drawString(500, yy - 14, fmt)
        pill(c, 690, yy - 10, 40, 14, st, C_RED, white, 6)
        yy -= 44

    c.setFillColor(C_TEXT)
    c.setFont("AB", 9)
    c.drawString(428, 96, "ADELANTO REAL")
    c.setFillColor(C_MUTED)
    c.setFont("A", 8)
    c.drawString(428, 80, "0 piezas válidas programadas. 0 en cola de YouTube Studio.")
    footer(c, 8)


def page_guiones(c):
    draw_bg(c)
    kicker(c, "08  ·  GUIONES, VOZ, PULIDO", 36, H - 48)
    h1(c, "Hay texto. Falta el producto diario.", 36, H - 78, 22)
    gold_rule(c, 36, H - 90)

    rows = [
        ("ES  piloto 15 min", "1,612 palabras", "~13–15 min a 120 wpm", "LISTO, NO SUBIDO", C_GREEN),
        ("ES  metadata piloto", "pack título / desc / tags", "marcado «NO subir aún»", "LISTO", C_GREEN),
        ("ES  guion 6 min", "943 palabras", "no es ninguno de los 3 formatos", "HUÉRFANO", C_AMBER),
        ("ES  plantillas core", "15m mañana / noche / short / salmos", "agencia-core/content/…", "SÍ", C_GREEN),
        ("ES  day_01–05", "lote 2 sep 09:49", "thumbs «Día N» + videos cortos", "NO PUBLICABLE", C_RED),
        ("EN  day_01 15 min", "999 palabras", "~8 min. Corto para el formato.", "INCOMPLETO", C_AMBER),
        ("EN  viernes 15 min", "1,179 palabras", "~10 min. Aún corto.", "INCOMPLETO", C_AMBER),
        ("EN  shorts", "2 archivos 60 s", "existen en markdown", "SÍ, SIN RENDER", C_AMBER),
        ("Bilingüe 11 min", "Cristina Campos", "fuera de los 3 formatos (11 ≠ 15)", "PILOTO SUELTO", C_AMBER),
        ("Largo 45–60", "plantilla largo_salmos.txt", "ningún master 45 min en disco", "NO EXISTE", C_RED),
    ]
    # table header
    c.setFillColor(C_PANEL2)
    c.roundRect(36, 478, 720, 28, 6, fill=1, stroke=0)
    c.setFillColor(C_MUTED)
    c.setFont("AB", 8)
    c.drawString(48, 488, "ENTREGABLE")
    c.drawString(250, 488, "QUÉ HAY")
    c.drawString(430, 488, "NOTA")
    c.drawString(640, 488, "ESTADO")
    y = 444
    for name, what, note, st, col in rows:
        c.setFillColor(C_PANEL if (y // 2) % 2 == 0 else C_PANEL2)
        c.roundRect(36, y - 8, 720, 32, 4, fill=1, stroke=0)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 8)
        c.drawString(48, y + 4, name)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        c.drawString(250, y + 4, what)
        c.drawString(430, y + 4, note)
        pill(c, 630, y - 2, 110, 16, st, col, C_BG, 6.5)
        y -= 36

    card(c, 36, 28, 720, 52)
    c.setFillColor(C_GOLD)
    c.setFont("AB", 8)
    c.drawString(52, 58, "LECTURA")
    c.setFillColor(C_TEXT)
    c.setFont("A", 8.5)
    c.drawString(52, 40, "No es que «no hayan entregado nada». Entregaron docs, un piloto 15 min local, 5 días de slop y thumbs rotas. Lo que no entregaron es la máquina diaria viva.")
    footer(c, 9)


def page_replicar(c):
    draw_bg(c)
    # hero
    c.saveState()
    p = c.beginPath()
    p.rect(0, 420, W, 192)
    c.clipPath(p, stroke=0)
    cover_image(c, SPLIT)
    c.restoreState()
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.55))
    c.rect(0, 420, W, 192, fill=1, stroke=0)
    kicker(c, "09  ·  CÓMO REPLICAR SIN TRIPLICAR EL CAOS", 36, 548)
    h1(c, "Un master. Tres mercados. No tres fábricas.", 36, 500, 22)
    muted(c, "Traducir el video ya hecho es el atajo. Volver a producir 30 días × 3 canales es el pozo.", 36, 476)

    cols = [
        ("ES  master", C_GOLD, [
            "Escribe / recita 15 min en español.",
            "Paisajes + ASS + miniatura oro.",
            "Corta el Short 60 s del mismo audio.",
            "Extiende a 45–60 con piano sacro (sin más API de voz).",
        ]),
        ("EN  clone", C_BLUE, [
            "Traduce el mismo guion (no improvises otro).",
            "Misma coreografía visual. Nueva voz EN.",
            "Cambia Brand Kit: Eternally Grateful.",
            "Horario 6:00 AM EST / 10:00 PM EST.",
        ]),
        ("ES+EN  overlay", C_PURPLE, [
            "Misma oración, dos pistas o subtítulos duales.",
            "El piloto Cristina 11 min ya prueba el formato.",
            "Ajustar a 15 min (no 11) para no inventar un 4.º formato.",
            "Carpeta propia. Hoy vive suelto en YOUTUBE GOD CHANNELS.",
        ]),
    ]
    x = 36
    for title, col, items in cols:
        card(c, x, 70, 232, 330)
        pill(c, x + 16, 368, 140, 18, title.upper(), col, C_BG, 8)
        y = 340
        for it in items:
            y -= bullet(c, x + 16, y, it, col, 9, 196) + 10
        x += 246
    footer(c, 10)


def page_accion(c):
    draw_bg(c)
    kicker(c, "10  ·  PLAN DE ACCIÓN  ·  7 DÍAS", 36, H - 48)
    h1(c, "Primero enciende una línea. Luego clónala.", 36, H - 78, 22)
    gold_rule(c, 36, H - 90)

    actions = [
        ("HOY", "No publiques otro video de 30–46 s.", "El canal ya tiene 3 piezas que entrenan mal al algoritmo.", C_RED),
        ("HOY", "Sube el piloto 15 min ES cuando pases QA visual.", "Es el único master que cumple el formato 2. Metadata ya está.", C_GOLD),
        ("HOY", "Corrige thumbs: quita Día N, 5:00 AM y Reto 7 Días.", "Usa 6:00 AM y 3–5 palabras. Referencia: bilingüe Cristina.", C_GOLD),
        ("DÍA 2", "Enciende sacred :8765 + n8n, o matalos y usa cron launchd.", "Webhook sin proceso = teatro. Elige un disparador de verdad.", C_AMBER),
        ("DÍA 2", "Limpia trigger_daily_devotional.py y el default de n8n.", "Fuera «Reto de 7 Días» y «DÍA 1» del payload.", C_AMBER),
        ("DÍA 3", "Sube el CSV a Canva Business (la cuenta de paga del canal).", "Bulk Create de miniaturas 30 días. Esta sesión no ve esa cuenta.", C_BLUE),
        ("DÍA 3", "Verifica teléfono en YouTube Studio.", "Sin eso no hay 45–60 min. El largo es el motor de watch time.", C_BLUE),
        ("DÍA 4–5", "Traduce el piloto 15 min → Eternally Grateful.", "Misma imagen, voz EN, Brand Kit EN. No reinventes el guion.", C_GREEN),
        ("DÍA 6", "Crea carpeta del canal bilingüe. Ajusta el 11 min a 15.", "Hoy no tiene AGENTS.md propio. No se puede replicar lo que no está.", C_GREEN),
        ("DÍA 7", "Programa 7 días reales en YouTube Studio (no n8n teatro).", "06:00 y 22:00 México. Short del mismo master a las 11:00.", C_GOLD),
    ]
    y = 470
    for when, title, note, col in actions:
        c.setFillColor(C_PANEL)
        c.roundRect(36, y - 6, 720, 38, 6, fill=1, stroke=0)
        pill(c, 46, y + 4, 70, 16, when, col, C_BG, 7)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 9)
        c.drawString(128, y + 8, title)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        c.drawString(128, y - 4, note)
        y -= 42
    footer(c, 11)


def page_fuentes(c):
    draw_bg(c)
    kicker(c, "11  ·  FUENTES Y LÍMITES", 36, H - 48)
    h1(c, "Qué se verificó. Qué no.", 36, H - 78, 24)
    gold_rule(c, 36, H - 90)

    card(c, 36, 280, 360, 230)
    kicker(c, "VERIFICADO HOY", 52, 486, C_GREEN)
    src = [
        "YouTube Data API v3 (token refrescado 5 sep): 4 videos, 3 subs.",
        "n8n sqlite: 7 ejecuciones, última 2 sep 04:11, 0 crons.",
        "Procesos: n8n no corre. :8765 no escucha.",
        "Disco: day_01–05, piloto 15 min, CSV 30 días, thumbs.",
        "Canva MCP: cuenta distinta (CVs / foto). Cero assets del canal.",
        "AGENTS.md ES (3 sep) + AGENTS.md EN (4 sep).",
    ]
    y = 462
    for s in src:
        y -= bullet(c, 52, y, s, C_GREEN, 8.5, 318) + 4

    card(c, 412, 280, 344, 230)
    kicker(c, "NO VERIFICADO / LÍMITE", 428, 486, C_AMBER)
    lim = [
        "Cuenta Canva Business de paga del canal: no está conectada a este MCP.",
        "Canal EN en YouTube: no hay OAuth separado auditado hoy.",
        "Duración exacta de MP4 locales: iCloud no indexó kMDItemDurationSeconds.",
        "Verificación telefónica de YouTube Studio: no se pudo abrir Studio.",
        "Notion Santuario: search básico no devolvió el dossier del canal.",
    ]
    y = 462
    for s in lim:
        y -= bullet(c, 428, y, s, C_AMBER, 8.5, 300) + 4

    # paths
    card(c, 36, 70, 720, 210)
    kicker(c, "RUTAS", 52, 256)
    paths = [
        "~/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO /   ← espacio al final. No mover.",
        "~/Desktop/Projects/YOUTUBE CHANNEL/ETERNALLY GRATEFUL/",
        "~/Desktop/Projects/YOUTUBE CHANNEL/YOUTUBE GOD CHANNELS/   ← piloto bilingüe suelto",
        "~/agencia-core/scripts/sacred_video_composer.py  ·  sacred_service.py  ·  trigger_daily_devotional.py",
        "~/agencia-core/docs/PLAYBOOK_AGRADECIMIENTO_SINCERO.md",
        "YouTube: https://www.youtube.com/channel/UCABE05zuxJifGDhnuB5dGUg",
    ]
    y = 232
    for pth in paths:
        y -= bullet(c, 52, y, pth, C_GOLD, 8.5, 670) + 4
    footer(c, 12)


def main():
    c = canvas.Canvas(str(OUT), pagesize=PAGE)
    c.setTitle("Auditoría visual — canales de oración — 5 sep 2026")
    c.setAuthor("Grok  ·  Poncho")
    pages = [
        page_cover, page_veredicto, page_orden, page_flujo, page_maquina,
        page_youtube, page_thumbs, page_calendario, page_guiones,
        page_replicar, page_accion, page_fuentes,
    ]
    for i, fn in enumerate(pages):
        fn(c)
        c.showPage()
    c.save()
    print("WROTE", OUT, "bytes", OUT.stat().st_size)


if __name__ == "__main__":
    main()
