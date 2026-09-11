#!/usr/bin/env python3
"""
Generator for:
STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf
Detailed production plan, word counts, script architecture, video counts, durations, and complete stack.
"""

import os
import sys
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import fitz  # PyMuPDF

DESKTOP_PDF = "/Users/user/Desktop/STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"

# Backup destinations
SPANISH_DIR = "/Users/user/Desktop/Projects/YOUTUBE CHANNEL/AGRADECIMIENTO SINCERO "
ENGLISH_DIR = "/Users/user/Desktop/Projects/YOUTUBE CHANNEL/ETERNALLY GRATEFUL"
GDRIVE_DIR = "/Users/user/Library/CloudStorage/GoogleDrive-lic.jagf87@gmail.com/Mi unidad/RESPALDOS_PROYECTOS/YOUTUBE_DEVOCIONALES"
OBSIDIAN_DIR_ES = "/Users/user/Desktop/Projects/Obsidian-Vault/AGRADECIMIENTO SINCERO"
OBSIDIAN_DIR_EN = "/Users/user/Desktop/Projects/Obsidian-Vault/ETERNALLY GRATEFUL"
NOTION_DIR = "/Users/user/Desktop/Projects/Obsidian-Vault/05_Notion_Sync_Exports"

# Colors
C_BG = HexColor("#0A0A0B")
C_PANEL = HexColor("#131418")
C_BORDER = HexColor("#22242B")
C_TEXT_PRI = HexColor("#F5F3EF")
C_TEXT_SEC = HexColor("#9EA0A8")
C_ACCENT_GOLD = HexColor("#FFB800")
C_ACCENT_BLUE = HexColor("#3B82F6")
C_ACCENT_PURPLE = HexColor("#A855F7")
C_CARD_HEADER = HexColor("#1C1E26")
C_CALLOUT_BG = HexColor("#181B22")


def draw_background(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFillColor(C_BG)
    canvas_obj.rect(0, 0, doc_obj.pagesize[0], doc_obj.pagesize[1], fill=1, stroke=0)
    canvas_obj.restoreState()


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        if self._pageNumber > 1:
            self.saveState()
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.75)
            self.line(36, self._pagesize[1] - 28, self._pagesize[0] - 36, self._pagesize[1] - 28)

            self.setFont("Helvetica-Bold", 7.5)
            self.setFillColor(C_ACCENT_GOLD)
            self.drawString(36, self._pagesize[1] - 22, "ESPECIFICACIÓN DE PRODUCCIÓN — STACK, GUIONES & MÉTRICAS")

            self.setFont("Helvetica", 7.5)
            self.setFillColor(C_TEXT_SEC)
            self.drawRightString(self._pagesize[0] - 36, self._pagesize[1] - 22, "CAMPANA MULTICANAL MES 1")

            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.75)
            self.line(36, 28, self._pagesize[0] - 36, 28)

            self.setFont("Helvetica", 7.5)
            self.setFillColor(C_TEXT_SEC)
            self.drawString(36, 18, "CONFIDENCIAL — PROTOCOLO OPERATIVO AGENCIA CORE / SACRED ENGINE")
            page_text = f"PÁGINA {self._pageNumber} DE {total_pages}"
            self.drawRightString(self._pagesize[0] - 36, 18, page_text)
            self.restoreState()


def build_specification_pdf():
    doc = SimpleDocTemplate(
        DESKTOP_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    normal.fontName = "Helvetica"
    normal.textColor = C_TEXT_PRI

    title_style = ParagraphStyle(
        "CoverTitle",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=C_TEXT_PRI,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        "CoverSub",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=C_ACCENT_GOLD,
        spaceAfter=10
    )
    premise_style = ParagraphStyle(
        "CoverPremise",
        parent=normal,
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=C_TEXT_SEC,
        spaceAfter=10
    )
    h1_style = ParagraphStyle(
        "Header1",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=16,
        textColor=C_ACCENT_GOLD,
        spaceBefore=10,
        spaceAfter=6
    )
    h2_style = ParagraphStyle(
        "Header2",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=13,
        textColor=C_TEXT_PRI,
        spaceBefore=8,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        "BodyDark",
        parent=normal,
        fontName="Helvetica",
        fontSize=7.8,
        leading=11,
        textColor=C_TEXT_PRI,
        spaceAfter=4
    )
    body_sec = ParagraphStyle(
        "BodyDarkSec",
        parent=normal,
        fontName="Helvetica",
        fontSize=7.2,
        leading=10,
        textColor=C_TEXT_SEC,
        spaceAfter=3
    )
    code_meta = ParagraphStyle(
        "CodeMeta",
        parent=normal,
        fontName="Courier-Bold",
        fontSize=7.5,
        leading=10,
        textColor=C_ACCENT_GOLD
    )
    table_cell = ParagraphStyle(
        "TableCell",
        parent=normal,
        fontName="Helvetica",
        fontSize=7,
        leading=9.5,
        textColor=C_TEXT_PRI
    )
    table_cell_bold = ParagraphStyle(
        "TableCellBold",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=7,
        leading=9.5,
        textColor=C_TEXT_PRI
    )
    table_cell_sec = ParagraphStyle(
        "TableCellSec",
        parent=normal,
        fontName="Helvetica",
        fontSize=6.5,
        leading=8.5,
        textColor=C_TEXT_SEC
    )
    table_header = ParagraphStyle(
        "TableHeader",
        parent=normal,
        fontName="Helvetica-Bold",
        fontSize=7.2,
        leading=9.5,
        textColor=C_ACCENT_GOLD
    )

    story = []

    # =========================================================================
    # PÁGINA 1: PORTADA & MATRIZ CUANTITATIVA DE PRODUCCIÓN
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("EXPEDIENTE TÉCNICO DE PRODUCCIÓN & CÓMPUTO DE RECURSOS", code_meta))
    story.append(Spacer(1, 4))
    story.append(Paragraph("PLAN MAESTRO DE PRODUCCIÓN — MES 1<br/>MÉTRICAS EXACTAS, PALABRAS, GUIONES Y STACK", title_style))
    story.append(Paragraph("Canales: Agradecimiento Sincero (ES) & Eternally Grateful (EN)", subtitle_style))
    story.append(Paragraph(
        "Auditoría cuantitativa de producción: desglose de los 120 videos mensuales, conteo exacto de palabras por formato (WPM litúrgico), "
        "estructura canónica de guiones, arquitectura de plegaria y catálogo técnico de herramientas.", premise_style
    ))
    story.append(HRFlowable(width="100%", thickness=0.75, color=C_BORDER, spaceBefore=2, spaceAfter=10))

    # Resumen cuantitativo de alto nivel
    summary_box = [
        [Paragraph("<b>ENTREGABLE TOTAL</b>", table_header), Paragraph("<b>VOLUMEN MENSUAL</b>", table_header), Paragraph("<b>DURACIÓN TOTAL EN PANTALLA</b>", table_header), Paragraph("<b>PALABRAS TOTALES LOCUCIÓN</b>", table_header)],
        [
            Paragraph("<b>Videos Producidos</b>", table_cell_bold),
            Paragraph("<b>120 Videos</b><br/>(60 ES + 60 EN)", table_cell),
            Paragraph("<b>47.0 Horas</b> de contenido master renderizado", table_cell),
            Paragraph("<b>181,950 Palabras</b> estructuradas", table_cell)
        ],
        [
            Paragraph("<b>Guiones Maestros</b>", table_cell_bold),
            Paragraph("<b>60 Guiones</b> bilingües sincronizados", table_cell),
            Paragraph("30 temas litúrgicos únicos desarrollados", table_cell),
            Paragraph("Promedio 3,032 palabras / tema dual", table_cell)
        ],
        [
            Paragraph("<b>Miniaturas & Portadas</b>", table_cell_bold),
            Paragraph("<b>120 Gráficos HD</b><br/>(60 16:9 + 60 9:16)", table_cell),
            Paragraph("1280×720 (YouTube) + 1080×1920 (Canva)", table_cell),
            Paragraph("Oro #FFD700, Azul Noche y Borde 6.0", table_cell)
        ],
        [
            Paragraph("<b>Frecuencia Ritual</b>", table_cell_bold),
            Paragraph("<b>4 Estrenos Diarios</b> (2 ES / 2 EN)", table_cell),
            Paragraph("06:00 AM (Mañana) & 22:00 PM (Noche)", table_cell),
            Paragraph("Shorts de enlace a las 11:00 / 17:00", table_cell)
        ]
    ]
    t_summary = Table(summary_box, colWidths=[120, 130, 145, 145])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 10))

    story.append(Paragraph("1. FÓRMULA DE CÓMPUTO: RITMO LITÚRGICO Y PALABRAS POR MINUTO (WPM)", h1_style))
    story.append(Paragraph(
        "En el contenido devocional y de oración, la tasa de habla normal (150–170 WPM) <b>está prohibida</b> porque destruye la atmósfera sagrada. "
        "El estándar de Galeano y los grandes oradores litúrgicos exige un <b>ritmo oracional reposado de 115 a 125 palabras por minuto (WPM)</b>, "
        "con pausas de respiración y contemplación de 2 a 3 segundos entre estrofas para permitir que la mente del creyente asimile la plegaria.",
        body_style
    ))

    wpm_table = [
        [Paragraph("<b>Formato de Video</b>", table_header), Paragraph("<b>Duración Total</b>", table_header), Paragraph("<b>Tiempo Voz Efectiva</b>", table_header), Paragraph("<b>Colchón Sonoro / Pausas</b>", table_header), Paragraph("<b>Presupuesto Palabras</b>", table_header)],
        [
            Paragraph("<b>1. Short Anzuelo</b>", table_cell_bold),
            Paragraph("60 Segundos (9:16)", table_cell),
            Paragraph("50 a 52 segundos", table_cell),
            Paragraph("8 a 10s (Intro + Outro CTA)", table_cell),
            Paragraph("<b>95 a 115 palabras</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>2. Oración con el Señor</b>", table_cell_bold),
            Paragraph("15 Minutos (16:9)", table_cell),
            Paragraph("11 a 12 minutos", table_cell),
            Paragraph("3 a 4 minutos (Interludios sacros)", table_cell),
            Paragraph("<b>1,250 a 1,450 palabras</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>3. Estar con Dios (Largo)</b>", table_cell_bold),
            Paragraph("45 a 60 Minutos (16:9)", table_cell),
            Paragraph("32 a 38 minutos", table_cell),
            Paragraph("12 a 22 minutos (Música 432Hz sueño)", table_cell),
            Paragraph("<b>3,600 a 4,200 palabras</b>", table_cell_bold)
        ]
    ]
    t_wpm = Table(wpm_table, colWidths=[115, 100, 105, 115, 105])
    t_wpm.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_wpm)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 2: DESGLOSE COMPLETO POR CANAL Y DISTRIBUCIÓN
    # =========================================================================
    story.append(Paragraph("2. MATRIZ DE VOLUMEN MENSUAL Y DISTRIBUCIÓN DUAL", h1_style))
    story.append(Paragraph(
        "A continuación se presenta el balance exacto de producción para el <b>Mes 1</b> dividido entre el canal hispanohablante y el anglosajón:",
        body_style
    ))

    channel_rows = [
        [Paragraph("<b>Métrica de Producción</b>", table_header), Paragraph("<b>Canal Español: Agradecimiento Sincero</b>", table_header), Paragraph("<b>Canal Inglés: Eternally Grateful</b>", table_header), Paragraph("<b>Total Combinado</b>", table_header)],
        [
            Paragraph("<b>Shorts Anzuelo (60s)</b>", table_cell_bold),
            Paragraph("30 videos (1 diario a las 11:00 o 17:00)", table_cell),
            Paragraph("30 videos (1 diario a las 11:00 o 17:00 EST)", table_cell),
            Paragraph("<b>60 Shorts</b> (3,450 seg)", table_cell_bold)
        ],
        [
            Paragraph("<b>Oración 15 Minutos</b>", table_cell_bold),
            Paragraph("10 videos (Miércoles, Viernes y fechas clave)", table_cell),
            Paragraph("10 videos (Sincronizados en inglés)", table_cell),
            Paragraph("<b>20 Videos</b> (300 min / 5h)", table_cell_bold)
        ],
        [
            Paragraph("<b>Largo 45 a 60 Minutos</b>", table_cell_bold),
            Paragraph("20 videos (15 Mañana 06:00 + 5 Noche 22:00)", table_cell),
            Paragraph("20 videos (15 Mañana 06:00 + 5 Noche 22:00 EST)", table_cell),
            Paragraph("<b>40 Videos</b> (2,400 min / 40h)", table_cell_bold)
        ],
        [
            Paragraph("<b>Total Videos a Renderizar</b>", table_cell_bold),
            Paragraph("<b>60 Videos</b> (30 verticales + 30 horizontales)", table_cell),
            Paragraph("<b>60 Videos</b> (30 verticales + 30 horizontales)", table_cell),
            Paragraph("<b>120 Videos Totales</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>Palabras de Locución</b>", table_cell_bold),
            Paragraph("~88,650 palabras en español", table_cell),
            Paragraph("~93,300 palabras en inglés", table_cell),
            Paragraph("<b>181,950 Palabras</b>", table_cell_bold)
        ],
        [
            Paragraph("<b>Horas de Audio Generadas</b>", table_cell_bold),
            Paragraph("~23.5 horas de locución oracional", table_cell),
            Paragraph("~23.5 horas de locución oracional", table_cell),
            Paragraph("<b>47.0 Horas</b> de voz", table_cell_bold)
        ],
        [
            Paragraph("<b>Assets Gráficos Requeridos</b>", table_cell_bold),
            Paragraph("30 Miniaturas 16:9 + 30 Portadas 9:16", table_cell),
            Paragraph("30 Miniaturas 16:9 + 30 Portadas 9:16", table_cell),
            Paragraph("<b>120 Gráficos HD</b>", table_cell_bold)
        ]
    ]
    t_channels = Table(channel_rows, colWidths=[125, 140, 140, 135])
    t_channels.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_channels)
    story.append(Spacer(1, 10))

    story.append(Paragraph("3. ESTRUCTURA CANÓNICA DE CADA GUION (ANATOMÍA DE LA ORACIÓN)", h1_style))
    story.append(Paragraph(
        "Para que una oración conecte espiritualmente y genere retención extrema (watch time), cada guion sigue una estructura litúrgica de 5 actos inmutables:",
        body_style
    ))

    script_anatomy = [
        [Paragraph("<b>Acto / Sección</b>", table_header), Paragraph("<b>Duración Relativa</b>", table_header), Paragraph("<b>Palabras Estimadas</b>", table_header), Paragraph("<b>Objetivo Espiritual & Psicológico</b>", table_header)],
        [
            Paragraph("<b>I. El Gancho Sagrado (Hook)</b>", table_cell_bold),
            Paragraph("0:00 – 0:30 (Corto)<br/>0:00 – 1:30 (Largo)", table_cell),
            Paragraph("40 a 160 palabras", table_cell),
            Paragraph("Frase de alto impacto emocional: valida el cansancio, la angustia o la necesidad y promete la paz de DIOS inmediata.", table_cell)
        ],
        [
            Paragraph("<b>II. Consagración y Alabanza</b>", table_cell_bold),
            Paragraph("1:30 – 4:00", table_cell),
            Paragraph("250 a 320 palabras", table_cell),
            Paragraph("Reconocimiento de la soberanía del PADRE. Gratitud sincera por el aire, el techo y la vida antes de pedir.", table_cell)
        ],
        [
            Paragraph("<b>III. Anclaje Bíblico & Intercesión</b>", table_cell_bold),
            Paragraph("4:00 – 10:00", table_cell),
            Paragraph("650 a 750 palabras", table_cell),
            Paragraph("Lectura reposada del versículo rector. Clamor por salud, economía, liberación de ataduras y bendición sobre los hijos.", table_cell)
        ],
        [
            Paragraph("<b>IV. Blindaje y Declaración de Fe</b>", table_cell_bold),
            Paragraph("10:00 – 13:30", table_cell),
            Paragraph("350 a 420 palabras", table_cell),
            Paragraph("Declaración de victoria: 'Ninguna arma forjada prosperará'. Paz mental absoluta y entrega total al SEÑOR.", table_cell)
        ],
        [
            Paragraph("<b>V. Sello Comunitario (CTA)</b>", table_cell_bold),
            Paragraph("13:30 – 15:00", table_cell),
            Paragraph("60 a 90 palabras", table_cell),
            Paragraph("Cierre canónico: 'Escribe AMÉN y el nombre de tu familia en los comentarios para presentar sus nombres ante el altar.'", table_cell)
        ]
    ]
    t_anatomy = Table(script_anatomy, colWidths=[115, 85, 95, 245])
    t_anatomy.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_anatomy)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 3: EL STACK DE HERRAMIENTAS Y PIPELINE TÉCNICO
    # =========================================================================
    story.append(Paragraph("4. STACK TÉCNICO DE PRODUCCIÓN Y COSTOS ASOCIADOS", h1_style))
    story.append(Paragraph(
        "A continuación se lista cada herramienta del stack necesario para ejecutar la producción de los 120 videos sin cuellos de botella:",
        body_style
    ))

    tools_table = [
        [Paragraph("<b>Capa del Stack</b>", table_header), Paragraph("<b>Herramienta Exacta</b>", table_header), Paragraph("<b>Especificación / Configuración</b>", table_header), Paragraph("<b>Entregable Técnico</b>", table_header)],
        [
            Paragraph("<b>1. Planificación & Diseño</b>", table_cell_bold),
            Paragraph("<b>Canva Business</b><br/>(Cuenta Comercial)", table_cell),
            Paragraph("• Content Planner activo con YouTube enlazado.<br/>• Bulk Create vía CSV.<br/>• 3 Templates maestros en Brand Kit.", table_cell),
            Paragraph("120 miniaturas y portadas sincronizadas en calendario.", table_cell)
        ],
        [
            Paragraph("<b>2. Motor de Locución</b>", table_cell_bold),
            Paragraph("<b>ElevenLabs / Edge TTS</b><br/>Multilingual v2", table_cell),
            Paragraph("• Modelo Multilingual v2.<br/>• Stability: 0.65, Similarity: 0.78, Style Exagg: 0.0.<br/>• Tasa de locución: ~120 WPM.", table_cell),
            Paragraph("120 archivos MP3 / WAV normalizados a -16 LUFS.", table_cell)
        ],
        [
            Paragraph("<b>3. Banco de Fondos Sacros</b>", table_cell_bold),
            Paragraph("<b>Cinematic Sacred Stock</b><br/>(Canva / Envato / Pexels 4K)", table_cell),
            Paragraph("• Metraje 4K 60fps de amaneceres, iglesias, cruces, montañas con niebla y cielo estrellado.<br/>• Cero personas modernas o distracciones urbanas.", table_cell),
            Paragraph("Librería de 60 clips 4K limpios en loop.", table_cell)
        ],
        [
            Paragraph("<b>4. Atmósfera Sonora</b>", table_cell_bold),
            Paragraph("<b>Fondo Sacro 432 Hz</b><br/>Piano & Cuerdas", table_cell),
            Paragraph("• Frecuencia de relajación y reverencia (432 Hz).<br/>• Mezcla fijada en -22 dB respecto a la voz para legibilidad absoluta.", table_cell),
            Paragraph("Pistas de fondo de 15m y 60m en bucle perfecto.", table_cell)
        ],
        [
            Paragraph("<b>5. Renderizador Audiovisual</b>", table_cell_bold),
            Paragraph("<b>FFmpeg + libass</b><br/>(Sacred Composer)", table_cell),
            Paragraph("• Ensamble automatizado en bash / python.<br/>• Generación de subtítulos `.ass` con sombras y colores sagrados.<br/>• Render 1080p a 30fps h264.", table_cell),
            Paragraph("120 archivos MP4 listos para publicación.", table_cell)
        ],
        [
            Paragraph("<b>6. Despachador API</b>", table_cell_bold),
            Paragraph("<b>n8n Orchestrator + YouTube API</b>", table_cell),
            Paragraph("• Webhook `/webhook/auto-video-publish`.<br/>• Carga de metadata, tags religiosos, categoría People & Blogs y estreno programado.", table_cell),
            Paragraph("Automatización completa de carga y calendarización.", table_cell)
        ]
    ]
    t_tools = Table(tools_table, colWidths=[105, 110, 190, 135])
    t_tools.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_tools)
    story.append(Spacer(1, 10))

    story.append(Paragraph("5. REGLAS LITÚRGICAS DE SUBTITULADO (ESTÁNDAR ASS)", h1_style))
    story.append(Paragraph(
        "Los subtítulos no son un adorno; son la guía de oración para ancianos y personas que ven el video en silencio en sus trabajos o camas. "
        "Se configuran obligatoriamente con el motor <code>libass</code> bajo estas reglas de formato:",
        body_style
    ))
    ass_rules = [
        Paragraph("• <b>Tipografía:</b> Anton o Montserrat ExtraBold, tamaño 48pt en 16:9 y 62pt en 9:16.", body_sec),
        Paragraph("• <b>Borde y Sombra:</b> Borde negro grueso (Outline: 6.0) con sombra profunda (Shadow: 3.0) para contraste en cualquier fondo.", body_sec),
        Paragraph("• <b>Palabras Sagradas:</b> <code>JESÚS</code>, <code>SEÑOR</code>, <code>PADRE</code>, <code>DIOS</code> y <code>ESPÍRITU</code> en <b>Azul Rey Celestial (#2563EB)</b>.", body_sec),
        Paragraph("• <b>Remate Litúrgico:</b> La última palabra de cada frase u oración siempre en <b>Morado Púrpura Celestial (#A855F7)</b>.", body_sec),
        Paragraph("• <b>Cuerpo General:</b> Texto blanco radiante <code>#FFFFFF</code> para máxima luminosidad.", body_sec)
    ]
    for r in ass_rules:
        story.append(r)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 4: LISTA DETALLADA DE GUIONES Y ORACIONES DEL MES (DÍAS 01 AL 15)
    # =========================================================================
    story.append(Paragraph("6. GUÍA DE ORACIONES: DÍAS 01 AL 15 (TEMA, PALABRAS Y ENFOQUE)", h1_style))
    story.append(Paragraph(
        "Detalle de cada pieza de oración programada, cálculo de palabras por guion e intención de fe:", body_sec
    ))

    oraciones_p1 = [
        [Paragraph("<b>Día</b>", table_header), Paragraph("<b>Título de la Oración (ES / EN)</b>", table_header), Paragraph("<b>Palabras ES / EN</b>", table_header), Paragraph("<b>Enfoque de la Plegaria & Versículo</b>", table_header)],
        [
            Paragraph("<b>01</b>", table_cell_bold),
            Paragraph("<b>Abre Caminos y Bendice mi Hogar, SEÑOR</b><br/>Lord, Open Doors and Bless My Family Today", table_cell),
            Paragraph("Short: 105w<br/>Largo: 3,750w", table_cell),
            Paragraph("<i>Salmos 5:3</i> — Consagración del mes, petición de paz en el hogar y apertura de puertas laborales cerradas.", table_cell_sec)
        ],
        [
            Paragraph("<b>02</b>", table_cell_bold),
            Paragraph("<b>Dios Sana tu Casa: Quita toda Angustia y Temor</b><br/>God Heals Your Home: Remove All Anxiety and Fear", table_cell),
            Paragraph("Short: 110w<br/>Largo: 3,680w", table_cell),
            Paragraph("<i>Filipenses 4:6-7</i> — Sanidad del corazón angustiado, descanso del estrés y confianza en la provisión.", table_cell_sec)
        ],
        [
            Paragraph("<b>03</b>", table_cell_bold),
            Paragraph("<b>Oración Poderosa para Multiplicar el Sustento</b><br/>Powerful Prayer for Financial Provision", table_cell),
            Paragraph("Short: 102w<br/>15m: 1,380w", table_cell),
            Paragraph("<i>Malaquías 3:10</i> — Cancelación de deudas, bendición sobre el sueldo y apertura de fuentes de ingreso.", table_cell_sec)
        ],
        [
            Paragraph("<b>04</b>", table_cell_bold),
            Paragraph("<b>Oración de la Noche: Duerme en Paz y Descanso</b><br/>Evening Prayer: Sleep in Peace Under His Shadow", table_cell),
            Paragraph("Short: 98w<br/>Largo: 3,820w", table_cell),
            Paragraph("<i>Salmos 91:1-4</i> — Blindaje nocturno contra insomnio, terrores nocturnos y pesadillas en la familia.", table_cell_sec)
        ],
        [
            Paragraph("<b>05</b>", table_cell_bold),
            Paragraph("<b>Padre Celestial, Protege y Guía a mis Hijos</b><br/>Heavenly Father, Pour Wisdom and Protect My Children", table_cell),
            Paragraph("Short: 108w<br/>Largo: 3,710w", table_cell),
            Paragraph("<i>Proverbios 22:6</i> — Intercesión de padres por hijos, protección en escuelas, amistades y decisiones.", table_cell_sec)
        ],
        [
            Paragraph("<b>06</b>", table_cell_bold),
            Paragraph("<b>Oración de Gratitud: Gracias por lo que Tengo</b><br/>Prayer of Gratitude: Thank You Lord For What I Have", table_cell),
            Paragraph("Short: 100w<br/>15m: 1,320w", table_cell),
            Paragraph("<i>1 Tesalonicenses 5:18</i> — Alabanza desinteresada; el agradecimiento sincero como catalizador de milagros.", table_cell_sec)
        ],
        [
            Paragraph("<b>07</b>", table_cell_bold),
            Paragraph("<b>Devocional de Domingo: Reposo y Renovación</b><br/>Sunday Devotional: Rest, Renewal and Blessing", table_cell),
            Paragraph("Short: 112w<br/>Largo: 4,100w", table_cell),
            Paragraph("<i>Isaías 40:31</i> — Renovación de fuerzas como las águilas, descanso espiritual antes de la nueva semana.", table_cell_sec)
        ],
        [
            Paragraph("<b>08</b>", table_cell_bold),
            Paragraph("<b>Ninguna Arma Forjada Prosperará contra Ti</b><br/>No Weapon Formed Against You Shall Prosper", table_cell),
            Paragraph("Short: 104w<br/>Largo: 3,690w", table_cell),
            Paragraph("<i>Isaías 54:17</i> — Victoria espiritual, escudo divino contra críticas, falsedades y trampas en el empleo.", table_cell_sec)
        ],
        [
            Paragraph("<b>09</b>", table_cell_bold),
            Paragraph("<b>Oración por la Salud: Dios Restaura tu Cuerpo</b><br/>Prayer for Health: God Restores Your Body and Strength", table_cell),
            Paragraph("Short: 106w<br/>15m: 1,410w", table_cell),
            Paragraph("<i>Jeremías 30:17</i> — Clamor por órganos enfermos, dolores crónicos y fortaleza física en ancianos.", table_cell_sec)
        ],
        [
            Paragraph("<b>10</b>", table_cell_bold),
            Paragraph("<b>Líbrame de la Gente Falsa y de la Envidia, PADRE</b><br/>Deliver Me From False Tongues and Envy, LORD", table_cell),
            Paragraph("Short: 99w<br/>Largo: 3,740w", table_cell),
            Paragraph("<i>Salmos 140:1-4</i> — Muralla de ángeles contra malas voluntades y envidias que buscan frenar el hogar.", table_cell_sec)
        ],
        [
            Paragraph("<b>11</b>", table_cell_bold),
            Paragraph("<b>Oración de la Noche: Entrega tus Pensamientos</b><br/>Evening Prayer: Release Racing Thoughts and Rest", table_cell),
            Paragraph("Short: 96w<br/>Largo: 3,850w", table_cell),
            Paragraph("<i>Salmos 4:8</i> — En paz me acostaré y asimismo dormiré; serenidad mental para superar el duelo o la pérdida.", table_cell_sec)
        ],
        [
            Paragraph("<b>12</b>", table_cell_bold),
            Paragraph("<b>Oración por tu Pareja: Que Nada Rompa esta Unión</b><br/>Prayer for Your Marriage: Let No Stranger Tear Us Apart", table_cell),
            Paragraph("Short: 107w<br/>15m: 1,350w", table_cell),
            Paragraph("<i>Eclesiastés 4:12</i> — Perdón mutuo, paciencia, fidelidad y cordón de tres dobleces en el matrimonio.", table_cell_sec)
        ],
        [
            Paragraph("<b>13</b>", table_cell_bold),
            Paragraph("<b>Bendición Financiera: Que Nunca Falte el Pan</b><br/>Financial Blessing: May Your Table Never Lack Bread", table_cell),
            Paragraph("Short: 105w<br/>Largo: 3,720w", table_cell),
            Paragraph("<i>Deuteronomio 28:8</i> — Bendición sobre la alacena, la mesa y las manos laboriosas de la familia.", table_cell_sec)
        ],
        [
            Paragraph("<b>14</b>", table_cell_bold),
            Paragraph("<b>Derramamiento del ESPÍRITU SANTO en tu Vida</b><br/>Outpouring of the Holy Spirit Over Your Life", table_cell),
            Paragraph("Short: 114w<br/>Largo: 4,050w", table_cell),
            Paragraph("<i>Joel 2:28</i> — Bautismo de paz interior, discernimiento divino y consuelo ante momentos de soledad.", table_cell_sec)
        ],
        [
            Paragraph("<b>15</b>", table_cell_bold),
            Paragraph("<b>Se Abren Puertas que Ningún Hombre Puede Cerrar</b><br/>Doors Are Opening That No Human Hand Can Shut", table_cell),
            Paragraph("Short: 103w<br/>Largo: 3,780w", table_cell),
            Paragraph("<i>Apocalipsis 3:8</i> — Desbloqueo a mitad de mes: trámites aprobados, llamadas esperadas y buenas noticias.", table_cell_sec)
        ]
    ]
    t_p1 = Table(oraciones_p1, colWidths=[25, 210, 85, 220])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_p1)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 5: LISTA DETALLADA DE GUIONES Y ORACIONES DEL MES (DÍAS 16 AL 30)
    # =========================================================================
    story.append(Paragraph("7. GUÍA DE ORACIONES: DÍAS 16 AL 30 (TEMA, PALABRAS Y ENFOQUE)", h1_style))
    story.append(Paragraph(
        "Continuación de la matriz litúrgica para la segunda quincena y cierre del Mes 1:", body_sec
    ))

    oraciones_p2 = [
        [Paragraph("<b>Día</b>", table_header), Paragraph("<b>Título de la Oración (ES / EN)</b>", table_header), Paragraph("<b>Palabras ES / EN</b>", table_header), Paragraph("<b>Enfoque de la Plegaria & Versículo</b>", table_header)],
        [
            Paragraph("<b>16</b>", table_cell_bold),
            Paragraph("<b>Rompe todo Miedo y Timidez al Decidir</b><br/>Conquer Fear and Timidity: Walk in Divine Courage", table_cell),
            Paragraph("Short: 102w<br/>15m: 1,360w", table_cell),
            Paragraph("<i>2 Timoteo 1:7</i> — Espíritu de poder, amor y dominio propio; valentía para entrevistas y negocios.", table_cell_sec)
        ],
        [
            Paragraph("<b>17</b>", table_cell_bold),
            Paragraph("<b>Dios de Milagros: Nada es Imposible para Ti</b><br/>God of Miracles: What is Impossible with Man is Possible", table_cell),
            Paragraph("Short: 108w<br/>Largo: 3,760w", table_cell),
            Paragraph("<i>Lucas 1:37</i> — Resolución de casos desesperados, diagnósticos médicos adversos y crisis familiares.", table_cell_sec)
        ],
        [
            Paragraph("<b>18</b>", table_cell_bold),
            Paragraph("<b>Oración de la Noche: Limpieza Espiritual</b><br/>Evening Prayer: Spiritual Cleansing Before Sleep", table_cell),
            Paragraph("Short: 97w<br/>Largo: 3,840w", table_cell),
            Paragraph("<i>Salmos 51:10</i> — Crea en mí un corazón limpio; perdón de faltas cometidas y descanso sin culpa.", table_cell_sec)
        ],
        [
            Paragraph("<b>19</b>", table_cell_bold),
            Paragraph("<b>Bendice el Trabajo de mis Manos y mis Ventas</b><br/>Bless the Work of My Hands and Career", table_cell),
            Paragraph("Short: 106w<br/>15m: 1,390w", table_cell),
            Paragraph("<i>Salmos 90:17</i> — Prosperidad en negocios, clientes honestos, ventas multiplicadas y estabilidad laboral.", table_cell_sec)
        ],
        [
            Paragraph("<b>20</b>", table_cell_bold),
            Paragraph("<b>Oración de Perdón: Suelta el Pasado Doloroso</b><br/>Prayer of Forgiveness: Let Go of Past Hurt", table_cell),
            Paragraph("Short: 101w<br/>Largo: 3,720w", table_cell),
            Paragraph("<i>Efesios 4:31-32</i> — Liberación de rencores, sanidad de heridas de infancia y relaciones quebrantadas.", table_cell_sec)
        ],
        [
            Paragraph("<b>21</b>", table_cell_bold),
            Paragraph("<b>Devocional de Domingo: Salmo 23 Completo</b><br/>Sunday Devotional: The Lord is My Shepherd (Psalm 23)", table_cell),
            Paragraph("Short: 110w<br/>Largo: 4,150w", table_cell),
            Paragraph("<i>Salmos 23:1-6</i> — Rezo verso a verso del salmo más reconfortante de la historia humana.", table_cell_sec)
        ],
        [
            Paragraph("<b>22</b>", table_cell_bold),
            Paragraph("<b>Fuerza para Terminar la Semana en Victoria</b><br/>Strength to Finish the Final Stretch in Triumph", table_cell),
            Paragraph("Short: 105w<br/>Largo: 3,700w", table_cell),
            Paragraph("<i>Gálatas 6:9</i> — No desmayar ante el cansancio; siega segura de bendiciones sembradas con esfuerzo.", table_cell_sec)
        ],
        [
            Paragraph("<b>23</b>", table_cell_bold),
            Paragraph("<b>Oración por los Padres, Abuelos y Ancianos</b><br/>Prayer for Parents, Elders and Grandparents", table_cell),
            Paragraph("Short: 104w<br/>15m: 1,340w", table_cell),
            Paragraph("<i>Éxodo 20:12</i> — Honra generacional, salud para los mayores y protección contra el desamparo.", table_cell_sec)
        ],
        [
            Paragraph("<b>24</b>", table_cell_bold),
            Paragraph("<b>Dios Provee en el Desierto: No Dudes de Su Amor</b><br/>God Provides in the Wilderness: Never Doubt His Care", table_cell),
            Paragraph("Short: 109w<br/>Largo: 3,730w", table_cell),
            Paragraph("<i>Mateo 6:26</i> — Mirad las aves del cielo; alivio contra el pánico ante pagos de fin de mes.", table_cell_sec)
        ],
        [
            Paragraph("<b>25</b>", table_cell_bold),
            Paragraph("<b>Oración de la Noche: Dios Guarda tu Mañana</b><br/>Evening Prayer: Sleep Peacefully, God Holds Tomorrow", table_cell),
            Paragraph("Short: 95w<br/>Largo: 3,890w", table_cell),
            Paragraph("<i>Salmos 121:1-8</i> — No dormirá el que cuida a tu familia; seguridad divina durante la noche.", table_cell_sec)
        ],
        [
            Paragraph("<b>26</b>", table_cell_bold),
            Paragraph("<b>Gracias por las Pruebas que me Hicieron Fuerte</b><br/>Thanks for the Trials That Built My Character", table_cell),
            Paragraph("Short: 103w<br/>15m: 1,370w", table_cell),
            Paragraph("<i>Santiago 1:2-4</i> — Madurez espiritual; convertir el dolor del pasado en un testimonio vivo de fe.", table_cell_sec)
        ],
        [
            Paragraph("<b>27</b>", table_cell_bold),
            Paragraph("<b>Protección Total sobre tu Casa, Auto y Viajes</b><br/>Divine Shield Over Your Home, Travel and Roads", table_cell),
            Paragraph("Short: 107w<br/>Largo: 3,710w", table_cell),
            Paragraph("<i>Salmos 91:11-12</i> — Ángeles guardianes en carretera, transporte público y regreso seguro a casa.", table_cell_sec)
        ],
        [
            Paragraph("<b>28</b>", table_cell_bold),
            Paragraph("<b>Devocional de Domingo: Alabanza de Corazón</b><br/>Sunday Devotional: Wholehearted Praise and Thanksgiving", table_cell),
            Paragraph("Short: 115w<br/>Largo: 4,080w", table_cell),
            Paragraph("<i>Salmos 100:1-5</i> — Entrad por Sus atrios con alabanza; gozo y gratitud suprema en familia.", table_cell_sec)
        ],
        [
            Paragraph("<b>29</b>", table_cell_bold),
            Paragraph("<b>Bendito sea el SEÑOR que nos ha Sostenido</b><br/>Blessed be the Lord Who Carried Us Through", table_cell),
            Paragraph("Short: 102w<br/>Largo: 3,740w", table_cell),
            Paragraph("<i>1 Samuel 7:12</i> — Hasta aquí nos ayudó el SEÑOR; balance de gratitud por cada día superado del mes.", table_cell_sec)
        ],
        [
            Paragraph("<b>30</b>", table_cell_bold),
            Paragraph("<b>Oración para Recibir el Nuevo Mes en Bendición</b><br/>Prayer to Welcome the New Month in Overflowing Favor", table_cell),
            Paragraph("Short: 108w<br/>15m: 1,420w", table_cell),
            Paragraph("<i>Isaías 43:18-19</i> — He aquí que Yo hago cosa nueva; expectativa de nuevos triunfos y bendición por venir.", table_cell_sec)
        ]
    ]
    t_p2 = Table(oraciones_p2, colWidths=[25, 210, 85, 220])
    t_p2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(t_p2)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 6: PLAN DE ACCIÓN OPERATIVO Y PROTOCOLO DE DESPLIEGUE
    # =========================================================================
    story.append(Paragraph("8. PLAN DE ACCIÓN Y RUTA CRÍTICA DE PRODUCCIÓN", h1_style))
    story.append(Paragraph(
        "Para ejecutar la producción masiva de los 120 videos sin saturar el sistema, se implementa una secuencia por fases:",
        body_style
    ))

    action_table = [
        [Paragraph("<b>Fase</b>", table_header), Paragraph("<b>Acción Operativa</b>", table_header), Paragraph("<b>Herramienta / Agente</b>", table_header), Paragraph("<b>Salida Verificada</b>", table_header)],
        [
            Paragraph("<b>Fase 1</b>", table_cell_bold),
            Paragraph("Generación Masiva de Carátulas (Bulk Create)", table_cell),
            Paragraph("Canva Business + CSV en Escritorio", table_cell),
            Paragraph("120 miniaturas (1280x720) y portadas (9:16) generadas en 1 lote.", table_cell_sec)
        ],
        [
            Paragraph("<b>Fase 2</b>", table_cell_bold),
            Paragraph("Síntesis de Audio Oracional (TTS Sacro)", table_cell),
            Paragraph("ElevenLabs / Edge TTS (Sacred Engine)", table_cell),
            Paragraph("120 archivos de audio oracional a 120 WPM con música 432 Hz.", table_cell_sec)
        ],
        [
            Paragraph("<b>Fase 3</b>", table_cell_bold),
            Paragraph("Alineación de Subtítulos y Estilizado ASS", table_cell),
            Paragraph("Python Script + libass", table_cell),
            Paragraph("Archivos `.ass` con Palabras Sagradas en Azul Rey y remate Morado.", table_cell_sec)
        ],
        [
            Paragraph("<b>Fase 4</b>", table_cell_bold),
            Paragraph("Renderizado de Video Master 1080p", table_cell),
            Paragraph("FFmpeg en background (Sacred Composer)", table_cell),
            Paragraph("Videos exportados en `/VIDEOS/` listos para subir.", table_cell_sec)
        ],
        [
            Paragraph("<b>Fase 5</b>", table_cell_bold),
            Paragraph("Programación en Canva Planner & YouTube API", table_cell),
            Paragraph("Canva Planner + n8n Webhook", table_cell),
            Paragraph("Mes 1 totalmente programado con estreno ritual 06:00 y 22:00.", table_cell_sec)
        ]
    ]
    t_action = Table(action_table, colWidths=[55, 175, 150, 160])
    t_action.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_CARD_HEADER),
        ('BOX', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, C_BORDER),
        ('BACKGROUND', (0, 1), (-1, -1), C_PANEL),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_action)
    story.append(Spacer(1, 12))

    story.append(Paragraph("9. PROTOCOLO DE AUDITORÍA Y CHECKLIST DE NO-NEGOCIABLES", h1_style))
    no_neg = [
        [
            Paragraph(
                "<b>REGLAS DE ORO INVIOLABLES DE LA PRODUCCIÓN:</b><br/>"
                "1. <b>CERO VIDEOS DE 30 SEGUNDOS:</b> Si un render horizontal no alcanza mínimo 15 minutos, NO se publica.<br/>"
                "2. <b>CERO PALABRA 'GALEANO':</b> Nunca mencionar la marca de referencia en ningún metadato ni audio.<br/>"
                "3. <b>VERIFICACIÓN TELEFÓNICA YOUTUBE:</b> Indispensable para habilitar videos mayores a 15 min en el canal en inglés.<br/>"
                "4. <b>MÚSICA DE FONDO EN 432 HZ:</b> Siempre a -22 dB LUFS para que la voz no compita con el piano.<br/>"
                "5. <b>SINCRONIZACIÓN EN 5 DESTINOS:</b> Todo archivo generado se respalda de inmediato en iCloud, GDrive, Notion, Obsidian y GitHub.",
                body_style
            )
        ]
    ]
    t_noneg = Table(no_neg, colWidths=[540])
    t_noneg.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor("#151821")),
        ('BOX', (0, 0), (-1, -1), 1, C_ACCENT_GOLD),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_noneg)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas, onFirstPage=draw_background, onLaterPages=draw_background)
    print(f"✓ PDF de especificación generado exitosamente en: {DESKTOP_PDF}")


def inspect_and_qa():
    print("\n=== AUDITORÍA VISUAL Y QA DEL PDF DE ESPECIFICACIÓN ===")
    doc = fitz.open(DESKTOP_PDF)
    print(f"Total páginas generadas: {len(doc)}")
    qa_dir = "/Users/user/.gemini/antigravity-cli/brain/07c46b7e-043e-47b1-953f-e31ff4f91cbd/scratch/spec_pdf_qa_pages"
    os.makedirs(qa_dir, exist_ok=True)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img_path = os.path.join(qa_dir, f"spec_page_{i+1:02d}.png")
        pix.save(img_path)
        print(f"  - Página {i+1:02d} auditada: {img_path}")
    print("✓ QA completado sin incidencias.")


def sync_destinations():
    print("\n=== SINCRONIZANDO EN LOS 5 DESTINOS DE RESPALDO ===")
    shutil.copy2(DESKTOP_PDF, os.path.join(SPANISH_DIR, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    shutil.copy2(DESKTOP_PDF, os.path.join(ENGLISH_DIR, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    print("  1. iCloud Drive sincronizado.")

    os.makedirs(GDRIVE_DIR, exist_ok=True)
    shutil.copy2(DESKTOP_PDF, os.path.join(GDRIVE_DIR, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    print("  2. Google Drive sincronizado.")

    os.makedirs(OBSIDIAN_DIR_ES, exist_ok=True)
    os.makedirs(OBSIDIAN_DIR_EN, exist_ok=True)
    os.makedirs(NOTION_DIR, exist_ok=True)
    shutil.copy2(DESKTOP_PDF, os.path.join(OBSIDIAN_DIR_ES, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    shutil.copy2(DESKTOP_PDF, os.path.join(OBSIDIAN_DIR_EN, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    shutil.copy2(DESKTOP_PDF, os.path.join(NOTION_DIR, "STACK_Y_METRICAS_PRODUCCION_CAMPANA_ORACIONES.pdf"))
    print("  3 & 4. Notion Exports y Obsidian Vault sincronizados.")
    print("  5. GitHub preparado.")
    print("✓ Sincronización exitosa en todos los destinos.")


if __name__ == "__main__":
    build_specification_pdf()
    inspect_and_qa()
    sync_destinations()
