#!/usr/bin/env python3
"""PDF visual — Prompt Maestro Máquila. Companion del .md pegable."""

from pathlib import Path
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path("/Users/user/Desktop/PROMPT_MAESTRO_MAQUILA_CANALES.pdf")
W, H = landscape(letter)
IMG = Path("/Users/user/.grok/sessions/%2FUsers%2Fuser/01a07248-f00e-7263-a595-5ba3ac41673d/images")
SUNRISE = IMG / "1.jpg"
NIGHT = IMG / "2.jpg"
SPLIT = IMG / "3.jpg"

C_BG = HexColor("#0A0A0B")
C_PANEL = HexColor("#121214")
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


def bg(c):
    c.setFillColor(C_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def footer(c, n, total=9):
    c.setStrokeColor(C_LINE)
    c.setLineWidth(0.4)
    c.line(36, 22, W - 36, 22)
    c.setFillColor(C_MUTED)
    c.setFont("A", 7.5)
    c.drawString(36, 10, "PROMPT MAESTRO MÁQUILA  ·  PEGAR EL .MD AL AGENTE  ·  5 SEP 2026")
    c.drawRightString(W - 36, 10, f"{n:02d}  /  {total:02d}")


def kicker(c, t, x, y, col=C_GOLD):
    c.setFillColor(col)
    c.setFont("AB", 8)
    c.drawString(x, y, t.upper())


def h1(c, t, x, y, s=24):
    c.setFillColor(C_TEXT)
    c.setFont("AB", s)
    c.drawString(x, y, t)


def gold_rule(c, x, y, w=72):
    c.setStrokeColor(C_GOLD)
    c.setLineWidth(1.4)
    c.line(x, y, x + w, y)


def card(c, x, y, w, h, stroke=None):
    c.setFillColor(C_PANEL)
    c.setStrokeColor(stroke or C_LINE)
    c.setLineWidth(0.6)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=1)


def pill(c, x, y, w, h, text, bg, fg=None, size=8):
    c.setFillColor(bg)
    c.roundRect(x, y, w, h, h / 2, fill=1, stroke=0)
    c.setFillColor(fg or C_BG)
    c.setFont("AB", size)
    c.drawCentredString(x + w / 2, y + (h - size) / 2 + 0.5, text)


def bullet(c, x, y, text, col=C_GOLD, size=9, maxw=340):
    c.setFillColor(col)
    c.circle(x + 3, y + 3, 2.2, fill=1, stroke=0)
    c.setFillColor(C_TEXT)
    c.setFont("A", size)
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


def cover_img(c, path):
    ir = ImageReader(str(path))
    iw, ih = ir.getSize()
    scale = max(W / iw, H / ih)
    nw, nh = iw * scale, ih * scale
    c.drawImage(ir, (W - nw) / 2, (H - nh) / 2, nw, nh, preserveAspectRatio=True, mask="auto")


def page_cover(c):
    cover_img(c, SUNRISE)
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.40))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.84))
    c.rect(0, 0, W, 268, fill=1, stroke=0)
    c.setFillColor(C_GOLD)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)
    kicker(c, "PARA EL AGENTE DE MAQUILA  ·  NO ES UN INFORME  ·  ES LA ORDEN", 40, H - 36)
    h1(c, "Prompt maestro de producción.", 40, 188, 30)
    c.setFillColor(C_MUTED)
    c.setFont("A", 12)
    c.drawString(40, 160, "Corrige AS + EG. Enciende la fábrica. Clona el método a otros nichos.")
    gold_rule(c, 40, 144, 90)
    pill(c, 40, 88, 210, 22, "PEGAR EL .MD AL AGENTE", C_GOLD, C_BG, 8)
    pill(c, 260, 88, 170, 22, "FASE A PRIMERO", C_RED, white, 8)
    pill(c, 440, 88, 200, 22, "7 DÍAS EN COLA ANTES DE CLONAR", C_PANEL, C_TEXT, 7.5)
    c.setFillColor(C_MUTED)
    c.setFont("A", 8)
    c.drawString(40, 48, "Escritorio:  PROMPT_MAESTRO_MAQUILA_CANALES.md")
    c.drawString(40, 34, "Ficha de canal nuevo:  FICHA_NUEVO_CANAL.md")
    footer(c, 1)


def page_uso(c):
    bg(c)
    kicker(c, "01  ·  CÓMO USARLO", 36, H - 48)
    h1(c, "Se lo pegas entero. No le resumas.", 36, H - 78)
    gold_rule(c, 36, H - 90)
    steps = [
        ("1", "Abre el .md del Escritorio", "PROMPT_MAESTRO_MAQUILA_CANALES.md — 7 secciones. No recortes."),
        ("2", "Pégalo al agente de maquila", "Claude / Grok / Codex / Gemini. Una sesión. Empieza Fase A."),
        ("3", "El agente no pregunta el canal", "Rutas, IDs y bugs ya van en el prompt. Hechos al 5 sep."),
        ("4", "Reporta en el bloque del final", "FASE / HECHO / BLOQUEADO / COLA YT / GATES."),
        ("5", "Canal nuevo = ficha primero", "Sin FICHA_NUEVO_CANAL.md llena, no hay carpeta nueva."),
        ("6", "PDF = mapa para humanos", "Este PDF no se pega al agente. El .md sí."),
    ]
    x, y = 36, 430
    for n, t, s in steps:
        card(c, x, y, 360, 88)
        pill(c, x + 16, y + 52, 28, 22, n, C_GOLD, C_BG, 10)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 11)
        c.drawString(x + 56, y + 56, t)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8.5)
        c.drawString(x + 56, y + 36, s)
        if x == 36:
            x = 412
        else:
            x = 36
            y -= 104
    footer(c, 2)


def page_paradas(c):
    bg(c)
    kicker(c, "02  ·  PARADAS EN SECO", 36, H - 48)
    h1(c, "Si va a hacer esto, que pare.", 36, H - 78)
    gold_rule(c, 36, H - 90)
    stops = [
        ("NO 27–47 s", "Eso no es oración ni episodio. El canal ya tiene 3. No hagas el 4."),
        ("NO «Día 1»", "Ni Reto de 7 Días. El suscriptor nuevo siente que llegó tarde."),
        ("NO 5:00 AM", "Canónico: 6:00 México / 6:00 EST. El código todavía miente."),
        ("NO 4.º formato", "11 min, 6 min, clip. Solo 60 s / 15 min / 45–60 min."),
        ("NO webhook teatro", "n8n sin proceso y sin cron no publica a las 6. Batch 21:00 + publishAt."),
        ("NO Canva Education", "Business de paga. La cuenta de maestro no es este canal."),
        ("NO Galeano en voz", "Se copia la máquina. Nunca el nombre."),
        ("NO borrar YT", "Los 3 cortos se quedan hasta que Poncho lo pida."),
    ]
    positions = [(36, 292), (228, 292), (420, 292), (612, 292), (36, 70), (228, 70), (420, 70), (612, 70)]
    for (t, s), (x, y) in zip(stops, positions):
        card(c, x, y, 180, 188, C_RED)
        c.setFillColor(C_RED)
        c.setFont("AB", 10)
        c.drawString(x + 14, y + 154, t)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        words = s.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 8) <= 152:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = y + 128
        for line in lines:
            c.drawString(x + 14, yy, line)
            yy -= 13
    footer(c, 3)


def page_arq(c):
    bg(c)
    kicker(c, "03  ·  PROGRAMACIÓN QUE SÍ VIVE EN LA NUBE", 36, H - 48)
    h1(c, "Se produce de noche. YouTube guarda la hora.", 36, H - 78, 20)
    gold_rule(c, 36, H - 90)
    steps = [
        ("21:00 MX", "Batch local", "La Mac encendida genera 1–7 piezas. Gate de duración."),
        ("QA", "Thumbs + ASS", "3–5 palabras. 6:00 AM. Sin Día N. Palabras sagradas."),
        ("API", "private + publishAt", "El horario vive en YouTube. La Mac puede apagarse."),
        ("06:00", "Estreno ritual", "ES México · EN EST. Short a las 11:00."),
    ]
    x = 36
    for n, t, s in steps:
        card(c, x, 360, 174, 150)
        c.setFillColor(C_GOLD)
        c.setFont("AB", 12)
        c.drawString(x + 16, 478, n)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 10)
        c.drawString(x + 16, 454, t)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        words = s.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if c.stringWidth(trial, "A", 8) <= 142:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        yy = 430
        for line in lines:
            c.drawString(x + 16, yy, line)
            yy -= 12
        x += 186
    card(c, 36, 70, 720, 270)
    kicker(c, "UN JOB. N CANALES. NO UN N8N POR NICHO.", 52, 312)
    items = [
        "CSV 30 días → guion master → voz → 15 min → Short 60 s + largo 45–60 (piano, no más API).",
        "Traducir el master. No reescribir 30 oraciones por idioma.",
        "n8n: o LaunchAgent KeepAlive + cron real, o fuera del camino crítico.",
        "sacred :8765: KeepAlive o llamar el composer directo desde el batch.",
        "Cero clips de 40 s «para no fallar el día». Si el gate falla, el log dice por qué.",
        "Cola mínima: 7 días scheduled antes de abrir o anunciar un canal nuevo.",
    ]
    y = 284
    for it in items:
        y -= bullet(c, 52, y, it, C_GOLD, 9.5, 680) + 8
    footer(c, 4)


def page_fases(c):
    bg(c)
    kicker(c, "04  ·  FASES  ·  NO SALTAR A F", 36, H - 48)
    h1(c, "A → B → C antes de clonar nichos.", 36, H - 78)
    gold_rule(c, 36, H - 90)
    fases = [
        ("A", "Frenar slop", "Hoy", "5:00 AM → 6:00 AM. Fuera Día 1 / Reto. Thumbs nuevas. Código parchado.", C_RED),
        ("B", "Una línea viva", "Hoy–mañana", "Piloto 15 min con QA. private + publishAt 06:00. Batch script.", C_AMBER),
        ("C", "Los dos canales", "48–72 h", "7 días ES en cola. EG = traducción, no fábrica nueva. Carpeta bilingüe.", C_GOLD),
        ("D", "Canva Business", "En paralelo", "Cuenta de paga. 3 templates + Bulk CSV. No publicar desde Canva.", C_BLUE),
        ("E", "Cola viva", "Semana 1", "Studio muestra 7 scheduled. El batch de anoche hizo el día 8.", C_GREEN),
        ("F", "Nicho nuevo", "Después de C", "Ficha llena → carpeta → 7 días → entonces se anuncia.", C_PURPLE),
    ]
    y = 430
    for code, name, when, note, col in fases:
        card(c, 36, y, 720, 58)
        pill(c, 48, y + 18, 36, 22, code, col, C_BG, 11)
        c.setFillColor(C_TEXT)
        c.setFont("AB", 12)
        c.drawString(100, y + 32, name)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        c.drawString(100, y + 16, when)
        c.setFillColor(C_TEXT)
        c.setFont("A", 9)
        c.drawString(250, y + 24, note)
        y -= 66
    footer(c, 5)


def page_formula(c):
    bg(c)
    c.saveState()
    p = c.beginPath()
    p.rect(0, 430, W, 182)
    c.clipPath(p, stroke=0)
    cover_img(c, SPLIT)
    c.restoreState()
    c.setFillColor(Color(0.04, 0.04, 0.05, alpha=0.55))
    c.rect(0, 430, W, 182, fill=1, stroke=0)
    kicker(c, "05  ·  1 MASTER  ·  3 MERCADOS", 36, 560)
    h1(c, "Traducir es el atajo. Tres fábricas es el pozo.", 36, 522, 20)
    cols = [
        ("ES master", C_GOLD, ["Escribe 15 min.", "Paisajes + ASS + thumb.", "Corta Short 60 s.", "Estira a 45–60 con piano."]),
        ("EN clone", C_BLUE, ["Traduce el mismo guion.", "≥ 1,600 palabras EN.", "Nueva voz. Mismo B-roll.", "6:00 AM EST."]),
        ("ES+EN overlay", C_PURPLE, ["Una oración, dos idiomas.", "Piloto Cristina = look, no formato.", "Ajustar a 15 min.", "Carpeta propia."]),
    ]
    x = 36
    for t, col, items in cols:
        card(c, x, 70, 232, 340)
        pill(c, x + 16, 378, 140, 18, t.upper(), col, C_BG, 8)
        y = 348
        for it in items:
            y -= bullet(c, x + 16, y, it, col, 10, 196) + 14
        x += 246
    footer(c, 6)


def page_nicho(c):
    bg(c)
    kicker(c, "06  ·  OTROS NICHOS  ·  MISMA MÁQUINA", 36, H - 48)
    h1(c, "Cámbiale el nombre. No le cambies las duraciones.", 36, H - 78, 20)
    gold_rule(c, 36, H - 90)
    # table header
    card(c, 36, 390, 720, 120)
    c.setFillColor(C_GOLD)
    c.setFont("AB", 9)
    c.drawString(52, 484, "PALANCA")
    c.drawString(200, 484, "FE (HOY)")
    c.drawString(430, 484, "OTRO NICHO")
    rows = [
        ("Short 60 s", "momento de la oración", "hook / tip / receta"),
        ("15 min", "oración que se termina", "episodio / workout / cuento"),
        ("45–60 min", "estar con Dios", "sleep / study / ambience"),
    ]
    yy = 458
    c.setFont("A", 10)
    for a, b, d in rows:
        c.setFillColor(C_TEXT)
        c.drawString(52, yy, a)
        c.setFillColor(C_MUTED)
        c.drawString(200, yy, b)
        c.drawString(430, yy, d)
        yy -= 22
    receta = [
        "Ficha llena (FICHA_NUEVO_CANAL.md). Sin ficha no hay carpeta.",
        "Carpeta + AGENTS.md + logos + scripts + day_01.",
        "Competidor = máquina interna. Nunca su nombre en el contenido.",
        "Idioma A primero. Luego traduce. No 30 días × N idiomas desde cero.",
        "CSV 30 días. Brand Kit 4 colores. 1 voz por idioma.",
        "Mismo batch 21:00 + publishAt. Un job, argumento channel=.",
        "7 piezas en cola ANTES de anunciar el canal.",
    ]
    y = 360
    kicker(c, "RECETA — 7 PASOS", 36, y)
    y = 336
    for r in receta:
        y -= bullet(c, 36, y, r, C_GOLD, 10, 700) + 6
    footer(c, 7)


def page_gates(c):
    bg(c)
    kicker(c, "07  ·  QA  ·  SI FALLA, NO SUBE", 36, H - 48)
    h1(c, "El gate es la fábrica. No el gusto.", 36, H - 78)
    gold_rule(c, 36, H - 90)
    gates = [
        ("57–63 s", "Short", C_GOLD),
        ("14–16 min", "Pieza", C_BLUE),
        ("45–60 min", "Largo", C_PURPLE),
        ("3–5 palabras", "Thumb", C_AMBER),
        ("6:00 AM", "Hora", C_GREEN),
        ("publishAt", "Nube", C_RED),
    ]
    x = 36
    for t, s, col in gates:
        card(c, x, 430, 114, 80, col)
        c.setFillColor(col)
        c.setFont("AB", 9)
        c.drawCentredString(x + 57, 478, t)
        c.setFillColor(C_MUTED)
        c.setFont("A", 8)
        c.drawCentredString(x + 57, 456, s)
        x += 124
    items = [
        "as_formats.py decide. Si el número no entra, el archivo no viaja a YouTube.",
        "Título sin Día N, sin Reto, sin Galeano, sin marca ajena.",
        "Thumb: palabras enteras, paisaje, logo, hora correcta.",
        "Palabras sagradas MAYÚSCULAS azul rey. Última palabra morado.",
        "Descripción + CTA de comentario + versículo con coordenada (nicho fe).",
        "Primer comentario = muro. Playlist oficial.",
        "Master copiado a VIDEOS/ y day_XX/.",
    ]
    y = 390
    for it in items:
        y -= bullet(c, 36, y, it, C_GOLD, 10, 700) + 8
    footer(c, 8)


def page_patch(c):
    bg(c)
    kicker(c, "08  ·  ARCHIVOS QUE EL AGENTE DEBE PARCHAR", 36, H - 48)
    h1(c, "El rumbo se corrige en el origen.", 36, H - 78)
    gold_rule(c, 36, H - 90)
    rows = [
        ("n8n blueprint", "Default «DÍA 1: ABRE CAMINOS»"),
        ("trigger_daily_devotional.py", "Reto 7 Días + 5:00 AM + scripts de un párrafo"),
        ("sacred_video_composer.py", "Thumb y descripción 5:00 AM · título Día N"),
        ("build_intro_video_pipeline.py", "5:00 AM"),
        ("upload_remastered_devotional.py", "5:00 AM"),
        ("thumbs day_01–05 + oficial", "Día N · Reto · texto cortado"),
        ("AGENTS.md AS", "Actualizar estado: 4 videos, n8n muerto desde 2 sep"),
        ("EG day_01 + guiones EN", "Estirar a ≥ 1,600 palabras. Thumb nueva"),
    ]
    y = 470
    for a, b in rows:
        c.setFillColor(C_PANEL)
        c.roundRect(36, y - 6, 720, 40, 6, fill=1, stroke=0)
        c.setFillColor(C_GOLD)
        c.setFont("AB", 9)
        c.drawString(52, y + 10, a)
        c.setFillColor(C_MUTED)
        c.setFont("A", 9)
        c.drawString(300, y + 10, b)
        y -= 48
    footer(c, 9)


def main():
    c = canvas.Canvas(str(OUT), pagesize=landscape(letter))
    c.setTitle("Prompt maestro máquila de canales")
    c.setAuthor("Poncho")
    for fn in [
        page_cover, page_uso, page_paradas, page_arq, page_fases,
        page_formula, page_nicho, page_gates, page_patch,
    ]:
        fn(c)
        c.showPage()
    c.save()
    print("WROTE", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
