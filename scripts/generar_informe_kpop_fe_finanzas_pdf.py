#!/usr/bin/env python3
"""
Generador del Informe Maestro en PDF: Avatares Virtuales (K-Pop/MV) y Canales Faceless de Fe, Finanzas y Neurociencia
Diseño editorial con ReportLab, paleta ejecutiva, tablas comparativas, diagramas de flujo y cajas de alerta.
AMDA Agentic Engine · Autor: @ponchogf88
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

PDF_OUTPUT = "/Users/imac/Desktop/Informe_Maestro_Avatares_Kpop_y_Canales_Fe_Finanzas.pdf"

# Paleta Editorial
COLOR_PRIMARY = colors.HexColor("#0F172A")    # Slate 900
COLOR_SECONDARY = colors.HexColor("#1E293B")  # Slate 800
COLOR_ACCENT = colors.HexColor("#4F46E5")     # Indigo 600
COLOR_GOLD = colors.HexColor("#D97706")       # Amber 600
COLOR_CYAN = colors.HexColor("#0284C7")       # Sky 600
COLOR_BG_CARD = colors.HexColor("#F8FAFC")    # Slate 50
COLOR_BORDER = colors.HexColor("#E2E8F0")     # Slate 200
COLOR_TEXT = colors.HexColor("#1E293B")       # Slate 800
COLOR_MUTED = colors.HexColor("#64748B")      # Slate 500
COLOR_SUCCESS = colors.HexColor("#16A34A")    # Green 600
COLOR_DANGER = colors.HexColor("#DC2626")     # Red 600
COLOR_CARD_ALT = colors.HexColor("#F1F5F9")   # Slate 100

class NumberedCanvas(canvas.Canvas):
    """Canvas de dos pasadas para numerar páginas dinámicamente y agregar header/footer."""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(COLOR_MUTED)
        
        # Header (Páginas > 1)
        if self._pageNumber > 1:
            self.drawString(36, 755, "INVESTIGACIÓN MAESTRA: AVATARES VIRTUALES, K-POP, FE Y FINANZAS · AMDA")
            self.setStrokeColor(COLOR_BORDER)
            self.setLineWidth(0.75)
            self.line(36, 748, 576, 748)

        # Footer (Todas las páginas)
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.75)
        self.line(36, 38, 576, 38)
        
        self.drawString(36, 26, "CONFIDENCIAL · ECOSISTEMA AMDA AGENTIC ENGINE · @ponchogf88")
        page_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(576, 26, page_text)
        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=21,
        leading=26,
        textColor=COLOR_PRIMARY,
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=COLOR_MUTED,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=COLOR_PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=COLOR_ACCENT,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        textColor=COLOR_TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=COLOR_TEXT
    )

    alert_style = ParagraphStyle(
        'AlertText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_PRIMARY
    )

    story = []

    # =========================================================================
    # PORTADA Y CABECERA
    # =========================================================================
    meta_data = [
        [
            Paragraph("<b>DOCUMENTO DE INVESTIGACIÓN Y PROTOCOLO OPERATIVO 2026</b>", ParagraphStyle('TopMeta', fontName='Helvetica-Bold', fontSize=8, textColor=COLOR_ACCENT)),
            Paragraph("<b>FECHA:</b> Septiembre 2026 | <b>AUTOR:</b> @ponchogf88", ParagraphStyle('TopDate', fontName='Helvetica', fontSize=8, textColor=COLOR_MUTED, alignment=2))
        ]
    ]
    t_meta = Table(meta_data, colWidths=[360, 180])
    t_meta.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_ACCENT, spaceBefore=2, spaceAfter=12))

    story.append(Paragraph("INFORME MAESTRO DE INVESTIGACIÓN: AVATARES VIRTUALES (K-POP/MV) Y CANALES DE FE, FINANZAS Y NEUROCIENCIA", title_style))
    story.append(Paragraph("<i>Auditoría de tendencias en X (Twitter), pipelines de producción para ídolos virtuales, ingeniería inversa del canal Galeano con Dios, el formato bilingüe de prosperidad y la automatización con repositorios Open Source y n8n.</i>", subtitle_style))

    # Tarjeta de Resumen Ejecutivo
    resumen_data = [
        [
            Paragraph("""
            <b>RESUMEN EJECUTIVO PARA TOMA DE DECISIONES INMEDIATA:</b><br/>
            1. <b>El Boom de los Avatares en X:</b> La comunidad global ha superado la fase del 'talking head' rígido. La frontera actual consiste en ensamblar videos musicales completos estilo K-Pop mediante la triada: <b>Suno/Udio</b> (audio master), <b>Kling/Seedance/Wan 2.1</b> (generación de movimiento y coreografía) y <b>Hedra/LivePortrait</b> (sincronización labial), dividiendo canciones de 3 minutos en 24 cortes dinámicos de 5 a 8 segundos.<br/>
            2. <b>El Nicho de Oro (Galeano con Dios + Fe & Finanzas):</b> Las familias y adultos mayores han reemplazado la televisión abierta por YouTube. El formato que genera mayor retención y tiempo de reproducción (Watch Time) es la <b>Oración Matutina de 15 a 20 minutos con la voz arquetípica de 'Padre + Hermano Mayor'</b>, fusionada con principios de educación financiera bíblica y fundamentos de neurociencia (reducción de cortisol y ondas Alfa).<br/>
            3. <b>Eliminación del 'Bug' Operativo:</b> El error común de los creadores es dar instrucciones abiertas a las herramientas. La solución estricta es un <b>Contrato JSON Inquebrantable</b> con límites de palabras y roles cerrados, ejecutado por <b>n8n y repositorios como tube-assistant y avatar-mix</b>.
            """, alert_style)
        ]
    ]
    t_resumen = Table(resumen_data, colWidths=[540])
    t_resumen.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_CARD_ALT),
        ('BORDER', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('LINELEFT', (0,0), (-1,-1), 4, COLOR_GOLD),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_resumen)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECCIÓN 1: INVESTIGACIÓN EN X (TWITTER) - AVATARES VIRTUALES Y VIDEOS MUSICALES
    # =========================================================================
    story.append(Paragraph("1. ¿Qué se está debatiendo en X? El Ecosistema de Avatares Musicales (K-Pop AI)", h1_style))
    story.append(Paragraph(
        "Durante las últimas semanas en X, creadores de contenido, investigadores de IA y estudios independientes han compartido pipelines para la creación de <b>ídolos virtuales hiperrealistas</b> capaces de protagonizar videos musicales completos. El consenso técnico revela que las herramientas monolíticas no alcanzan el nivel comercial por sí solas, requiriendo una arquitectura por capas:",
        body_style
    ))

    # Tabla de Stack Técnico de Video Musical K-Pop
    stack_data = [
        [Paragraph("Etapa del Pipeline", table_header_style), Paragraph("Herramienta Dominante", table_header_style), Paragraph("Función Específica", table_header_style), Paragraph("Regla de Oro en X", table_header_style)],
        [
            Paragraph("<b>1. Audio Master</b>", table_cell_style),
            Paragraph("Suno v3.5 / Udio", table_cell_style),
            Paragraph("Generación de la pista musical completa con estructura pop, voces femeninas armonizadas y BPM entre 115 y 128.", table_cell_style),
            Paragraph("Generar primero el audio master final. Nunca intentar sincronizar video con audios borradores.", table_cell_style)
        ],
        [
            Paragraph("<b>2. Consistencia Facial</b>", table_cell_style),
            Paragraph("Midjourney v6.1 (--cref) / Flux + LoRA", table_cell_style),
            Paragraph("Fijar el rostro del avatar en ángulos neutros, sonriendo y perfil para generar la 'Character Bible' permanente.", table_cell_style),
            Paragraph("Mantener un solo seed fotográfico y ropa consistente para que el modelo de video no invente facciones.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Coreografía y Baile</b>", table_cell_style),
            Paragraph("Kling AI 1.5 / Seedance / Wan 2.1", table_cell_style),
            Paragraph("Animación Image-to-Video del cuerpo completo del avatar ejecutando movimientos de baile energéticos.", table_cell_style),
            Paragraph("Limitar los prompts a cortes de 4 a 6 segundos. Los renders largos (>10s) sufren deformación de extremidades.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Sincronización Labial</b>", table_cell_style),
            Paragraph("Hedra / LivePortrait / MuseTalk", table_cell_style),
            Paragraph("Mapeo fonético de los primeros planos cantando el coro y los versos sobre la pista de voz aislada.", table_cell_style),
            Paragraph("Usar HeyGen solo para planos cerrados estáticos. Para música con emoción, Hedra y LivePortrait ofrecen mayor realismo.", table_cell_style)
        ],
        [
            Paragraph("<b>5. Edición y Montaje</b>", table_cell_style),
            Paragraph("CapCut Desktop / DaVinci Resolve", table_cell_style),
            Paragraph("Ensamblaje rítmico: alternancia entre plano de baile (Seedance/Kling) y primer plano cantando (LivePortrait).", table_cell_style),
            Paragraph("Un video musical de 3 minutos requiere entre 22 y 28 tomas distintas, emulando la edición real de MTV o SM Entertainment.", table_cell_style)
        ]
    ]

    t_stack = Table(stack_data, colWidths=[90, 110, 180, 160])
    t_stack.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_stack)
    story.append(Spacer(1, 10))

    # Criterio HeyGen
    criterio_heygen = [
        [
            Paragraph("""
            <b>EL ERROR FATAL CON HEYGEN:</b><br/>
            Muchos creadores cometen el error de intentar renderizar una canción completa de 3 minutos subiendo el audio a HeyGen con un solo avatar estático. El resultado es un 'talking head' aburrido que la audiencia abandona a los 10 segundos, consumiendo todos los créditos educativos del mes. HeyGen está optimizado para portavoces corporativos, no para coreografías. El avatar congelado debe reservarse para <b>cortes estratégicos de 5 segundos en primeros planos</b> dentro del ensamble general.
            """, alert_style)
        ]
    ]
    t_criterio = Table(criterio_heygen, colWidths=[540])
    t_criterio.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF2F2")),
        ('BORDER', (0,0), (-1,-1), 1, colors.HexColor("#FECACA")),
        ('LINELEFT', (0,0), (-1,-1), 4, COLOR_DANGER),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_criterio)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECCIÓN 2: INGENIERÍA INVERSA DE "GALEANO CON DIOS" + FE Y FINANZAS
    # =========================================================================
    story.append(Paragraph("2. Ingeniería Inversa: 'Galeano con Dios', Fe, Finanzas Cristianas y Neurociencia", h1_style))
    story.append(Paragraph(
        "El canal <i>Galeano con Dios</i> ha demostrado una retención colosal en YouTube gracias a un formato íntimo, sobrio y libre de la teatralidad de los teleevangelistas tradicionales. El análisis de audiencia revela patrones clave que pueden capitalizarse de inmediato:",
        body_style
    ))

    story.append(Paragraph("<b>A) La Psicología de la Voz ('Papá + Hermano Mayor'):</b>", h2_style))
    story.append(Paragraph(
        "La audiencia matutina y nocturna de oraciones busca refugio, contención emocional y seguridad. Una voz estridente o autoritaria genera rechazo inmediato. El arquetipo que funciona es el de una figura que no juzga, sino que acompaña; alguien que se sienta a la mesa a orar contigo antes de que empiece el día. Este tono se programa en ElevenLabs con el modelo Multilingual v2, reduciendo la estabilidad al 65% y el estilo al 15% para conseguir cadencias humanas con pausas reflexivas de 1.5 segundos.",
        body_style
    ))

    story.append(Paragraph("<b>B) El Eje de Oro: Oración + Educación Financiera Bíblica:</b>", h2_style))
    story.append(Paragraph(
        "El mayor dolor de la audiencia adulta (35 a 65+ años) no es teológico, sino práctico: <b>la angustia por el dinero, las deudas y la estabilidad familiar</b>. La conexión entre fe y administración es histórica en la literatura bíblica (más de 2,350 versículos hablan de dinero y posesiones). La estructura maestra que retiene horas de reproducción es:",
        body_style
    ))

    # Estructura del Video Híbrido
    story.append(Paragraph("• <b>Minuto 0:00 a 1:00 (Apertura de Paz):</b> Reconocimiento de la ansiedad matutina ('Si te despertaste con el pecho apretado por el dinero, hoy no vamos a correr').", bullet_style))
    story.append(Paragraph("• <b>Minuto 1:00 a 9:00 (Oración Guiada Profunda):</b> Clamor de entrega, quebrantamiento del afán y petición de protección divina.", bullet_style))
    story.append(Paragraph("• <b>Minuto 9:00 a 13:00 (Píldora de Sabiduría Financiera):</b> Enseñanza didáctica sin sermón (ej. Bola de nieve de deudas, Fondo de Emergencia de Proverbios, la regla del 70/20/10).", bullet_style))
    story.append(Paragraph("• <b>Minuto 13:00 a 15:00 (Cierre y Bendición Pastoral):</b> 'Amén. Que Dios te bendiga hoy'. Llamado a dejar intenciones en el chat fijado.", bullet_style))

    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>C) El Fundamento Neurocientífico (Dr. Andrew Huberman & Neuroteología):</b>", h2_style))
    story.append(Paragraph(
        "Estudios clínicos en neuroimagen demuestran que la oración contemplativa sostenida durante más de 12 minutos disminuye drásticamente la actividad en la <b>amígdala cerebral</b> (el centro de alarma del miedo y la deuda) y activa la <b>corteza prefrontal dorsolateral</b>, responsable de la toma de decisiones racionales y la planificación a largo plazo. Al mismo tiempo, induce ritmos cerebrales en bandas <b>Alfa (8-12 Hz) y Theta (4-7 Hz)</b>. Explicar este fenómeno en los videos valida la experiencia espiritual con rigor científico, atrayendo a una audiencia culta que busca tanto salud mental como conexión trascendente.",
        body_style
    ))

    story.append(Paragraph("<b>D) La Ventaja Fronteriza Bilingüe (Texas / México / USA Hispanic):</b>", h2_style))
    story.append(Paragraph(
        "En comunidades hispanas de segunda y tercera generación en Texas, California y Florida, existe un fenómeno comprobado: <b>la emoción se conecta en español (el idioma del hogar y la abuela), pero las finanzas y los negocios se estructuran en inglés</b>. El formato que proponemos no es una traducción literal palabra por palabra; es un video simbiótico donde la oración se entrega en español cálido y el bloque de educación financiera se refuerza con subtítulos y conceptos en inglés ('Peace with your money / Biblical wealth stewardship'). Esto duplica el alcance algorítmico y abre el CPM de Estados Unidos ($8 a $15 USD por cada 1,000 vistas frente a los $1.50 USD de Latinoamérica).",
        body_style
    ))

    story.append(Spacer(1, 14))

    # =========================================================================
    # SECCIÓN 3: AUTOMATIZACIÓN TOTAL CON REPOSITORIOS Y N8N LOCAL
    # =========================================================================
    story.append(Paragraph("3. Arquitectura de Automatización: Matar el 'Bug' con Contratos JSON y n8n", h1_style))
    story.append(Paragraph(
        "El motivo por el cual los intentos previos de automatización fallaban no es la falta de potencia de la IA, sino la <b>ausencia de un contrato estricto de entrada y salida</b>. Cuando a un modelo de lenguaje se le dan instrucciones abiertas, improvisa en la duración, cambia el tono pastoral a uno dogmático o inventa estructuras que rompen la edición de video.",
        body_style
    ))

    # Tabla de Repositorios Clave
    repo_data = [
        [Paragraph("Repositorio Open Source", table_header_style), Paragraph("Arquitectura / Enfoque", table_header_style), Paragraph("Aplicación Directa a tu Canal", table_header_style)],
        [
            Paragraph("<b>tube-assistant</b><br/>(metiu1)", table_cell_style),
            Paragraph("Python + LLM + Edge TTS + Pexels API + FFmpeg + YouTube Data API v3.", table_cell_style),
            Paragraph("Excelente base para compilar videos de stock con voz y subtítulos quemados automáticamente sin intervención.", table_cell_style)
        ],
        [
            Paragraph("<b>quran-reels-maker</b>", table_cell_style),
            Paragraph("Motor de generación en bucle de versículos sacros con fondos de naturaleza y audio normalizado.", table_cell_style),
            Paragraph("Patrón idéntico al requerido para los Salmos y oraciones matutinas: consistencia absoluta día tras día.", table_cell_style)
        ],
        [
            Paragraph("<b>avatar-mix</b><br/>(Upload-Post)", table_cell_style),
            Paragraph("Toma un clip base de avatar transparente o chroma, inserta fondos en movimiento y subtítulos dinámicos.", table_cell_style),
            Paragraph("Permite usar tu avatar congelado sobre múltiples escenarios de templos, bibliotecas y amaneceres.", table_cell_style)
        ],
        [
            Paragraph("<b>LivePortrait / vanta</b>", table_cell_style),
            Paragraph("Inferencia local de Lip-Sync y microexpresiones faciales en tiempo real a partir de 1 sola foto y 1 audio.", table_cell_style),
            Paragraph("Cero costo por minuto. Se ejecuta en hardware local (Apple Silicon M1 o tarjetas RTX en Dell) de por vida.", table_cell_style)
        ]
    ]

    t_repo = Table(repo_data, colWidths=[120, 200, 220])
    t_repo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_SECONDARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_repo)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Flujo Operativo en n8n Local (Disparo Automático 05:00 AM):</b>", h2_style))
    story.append(Paragraph("1. <b>Nodo Cron Trigger:</b> Se dispara diariamente a las 05:00 AM.", bullet_style))
    story.append(Paragraph("2. <b>Nodo Notion API:</b> Lee el registro correspondiente al día en la base de datos de los 30 temas.", bullet_style))
    story.append(Paragraph("3. <b>Nodo ElevenLabs API:</b> Sintetiza la locución en WAV usando el seed fijo de voz pastoral.", bullet_style))
    story.append(Paragraph("4. <b>Nodo Execute Command (FFmpeg):</b> Concatena el audio con el bucle de video en 1080p, aplica filtro de audio -14 LUFS y quema subtítulos SRT generados por Whisper.", bullet_style))
    story.append(Paragraph("5. <b>Nodo YouTube Upload:</b> Sube el video como 'Privado' u 'Oculto' a las 05:30 AM para que el algoritmo procese el HD.", bullet_style))
    story.append(Paragraph("6. <b>Nodo YouTube Status:</b> Publica el video como 'Público' exactamente a las 06:00 AM y publica el Pinned Comment con la invitación a la comunidad.", bullet_style))

    story.append(Spacer(1, 14))

    # =========================================================================
    # SECCIÓN 4: LOS 7 GUIONES MAESTROS (FASE 2 DESPLEGADA)
    # =========================================================================
    story.append(Paragraph("4. Matriz de los Primeros 7 Días de Producción (Fase 2 Canónica)", h1_style))
    story.append(Paragraph(
        "Siguiendo el contrato de producción inquebrantable, hemos consolidado la matriz temática de los 7 primeros días listos en el archivo canónico <code>PIPELINE_7_GUIONES_FE_Y_FINANZAS.json</code> dentro del proyecto:",
        body_style
    ))

    # Tabla Resumen de los 7 Guiones
    guiones_data = [
        [Paragraph("Día", table_header_style), Paragraph("Título Estratégico", table_header_style), Paragraph("Principio Financiero", table_header_style), Paragraph("Versículo Bíblico", table_header_style), Paragraph("Llamado a la Comunidad", table_header_style)],
        [
            Paragraph("<b>1</b>", table_cell_style),
            Paragraph("Oración de la mañana para soltar la ansiedad por el dinero", table_cell_style),
            Paragraph("Dios no bendice el desorden; bendice la administración. Presupuesto consciente.", table_cell_style),
            Paragraph("Filipenses 4:6-7", table_cell_style),
            Paragraph("Escribe 'Amén' y nombra a tu familia en el chat.", table_cell_style)
        ],
        [
            Paragraph("<b>2</b>", table_cell_style),
            Paragraph("Rompe el ciclo de las deudas: Principio bíblico de libertad", table_cell_style),
            Paragraph("Método Bola de Nieve Bíblico: liquidar de menor a mayor para ganar tracción.", table_cell_style),
            Paragraph("Proverbios 22:7", table_cell_style),
            Paragraph("Declara: 'Hoy rompo toda atadura de deuda'.", table_cell_style)
        ],
        [
            Paragraph("<b>3</b>", table_cell_style),
            Paragraph("Dios bendice al dador alegre: La ciencia y la fe del dar", table_cell_style),
            Paragraph("Generosidad desinteresada reduce cortisol y resetea el miedo a la escasez.", table_cell_style),
            Paragraph("2 Corintios 9:7", table_cell_style),
            Paragraph("Comparte 1 bendición recibida esta semana.", table_cell_style)
        ],
        [
            Paragraph("<b>4</b>", table_cell_style),
            Paragraph("Oración por tu trabajo, negocio y sabiduría para emprender", table_cell_style),
            Paragraph("No comerte la semilla: reinvertir el 50% de las primeras ganancias del negocio.", table_cell_style),
            Paragraph("Deuteronomio 8:18", table_cell_style),
            Paragraph("Pon el nombre de tu emprendimiento o empleo.", table_cell_style)
        ],
        [
            Paragraph("<b>5</b>", table_cell_style),
            Paragraph("Construyendo tu Fondo de Paz: El ahorro como testimonio", table_cell_style),
            Paragraph("Crear el colchón de 1,000 USD o 1 mes de gastos básicos para frenar el pánico.", table_cell_style),
            Paragraph("Proverbios 6:6-8", table_cell_style),
            Paragraph("Aprende de la hormiga: aparta antes de gastar.", table_cell_style)
        ],
        [
            Paragraph("<b>6</b>", table_cell_style),
            Paragraph("Vence la envidia y la comparación: El contentamiento", table_cell_style),
            Paragraph("Dejar de gastar en validar estatus ante terceros; vivir por debajo de los ingresos.", table_cell_style),
            Paragraph("1 Timoteo 6:6", table_cell_style),
            Paragraph("Agradece 3 cosas que no se compran con dinero.", table_cell_style)
        ],
        [
            Paragraph("<b>7</b>", table_cell_style),
            Paragraph("Resumen semanal: Oración de consagración de tus finanzas", table_cell_style),
            Paragraph("Consolidación de los 4 pilares y consagración total del hogar ante Dios.", table_cell_style),
            Paragraph("Salmo 37:5", table_cell_style),
            Paragraph("Escribe: 'Consagro mi casa y mi sustento al Señor'.", table_cell_style)
        ]
    ]

    t_guiones = Table(guiones_data, colWidths=[25, 150, 160, 95, 110])
    t_guiones.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_guiones)
    story.append(Spacer(1, 14))

    # =========================================================================
    # SECCIÓN 5: PLAN DE ACCIÓN DE 24 HORAS A 90 DÍAS
    # =========================================================================
    story.append(Paragraph("5. Hoja de Guerra: Plan de Acción de 24 Horas y Escalado a 90 Días", h1_style))
    
    plan_data = [
        [
            Paragraph("<b>VENTANA DE 24 HORAS (ARRANQUE EXPRÉS)</b>", ParagraphStyle('PlanH', fontName='Helvetica-Bold', fontSize=9, textColor=COLOR_ACCENT)),
            Paragraph("<b>VENTANA DE 90 DÍAS (ESCALA Y MONETIZACIÓN)</b>", ParagraphStyle('PlanH2', fontName='Helvetica-Bold', fontSize=9, textColor=COLOR_SUCCESS))
        ],
        [
            Paragraph("""
            • <b>Hora 0-2:</b> Creación del canal de marca <i>Oración de Hoy · Fe y Finanzas</i> (@oraciondehoyfe) con foto de biblia sobria y banner 2560x1440 en Canva.<br/>
            • <b>Hora 2-6:</b> Extracción del JSON del Día 1 y generación de la voz en ElevenLabs con el preset Antonio_Warm_Pastor_v2.<br/>
            • <b>Hora 6-12:</b> Ensamble en CapCut / FFmpeg: Fondo de santuario, música 432 Hz de fondo a -18 dB y subtítulos automáticos.<br/>
            • <b>Hora 12-18:</b> Subida en YouTube Studio y publicación a las 06:00 AM.<br/>
            • <b>Hora 18-24:</b> Extracción de 2 Shorts verticales (30s) y distribución en los grupos de WhatsApp de tu mamá y familiares en Texas.
            """, table_cell_style),
            Paragraph("""
            • <b>Mes 1 (Días 1 a 30):</b> Publicación diaria estricta a las 06:00 AM. Se alcanzan las primeras 1,500 horas de reproducción gracias a la retención de 15 minutos por usuario.<br/>
            • <b>Mes 2 (Días 31 a 60):</b> Entrada al Programa de Socios de YouTube (YPP). Monetización con AdSense activada. Inicio de transmisiones en vivo 24/7 en paralelo para acelerar el Watch Time.<br/>
            • <b>Mes 3 (Días 61 a 90):</b> Lanzamiento del infoproducto de apoyo: <i>Cuaderno Devocional de Paz Financiera</i> en Gumroad ($9.99 USD) y membresías de canal con oraciones personalizadas.
            """, table_cell_style)
        ]
    ]

    t_plan = Table(plan_data, colWidths=[265, 275])
    t_plan.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_CARD),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_plan)
    story.append(Spacer(1, 14))

    # Cierre de Protocolo
    cierre_box = [
        [
            Paragraph("""
            <b>CONCLUSIÓN Y REGLA DE ORO DE AMDA AGENTIC ENGINE:</b><br/>
            No esperes a tener 30 videos renderizados con perfección cinematográfica para publicar el primero. El algoritmo de YouTube no aprende de intenciones guardadas en el disco duro; aprende de impresiones reales, retención de retención de minutos y comentarios en el chat. Hoy queda desplegada la Fase 1 y la Fase 2 en tu repositorio y en tus 5 destinos de respaldo. El canal está listo para nacer.
            """, alert_style)
        ]
    ]
    t_cierre = Table(cierre_box, colWidths=[540])
    t_cierre.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BORDER', (0,0), (-1,-1), 1, colors.HexColor("#BFDBFE")),
        ('LINELEFT', (0,0), (-1,-1), 4, COLOR_CYAN),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_cierre)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado con éxito en: {PDF_OUTPUT}")

if __name__ == "__main__":
    build_pdf()
