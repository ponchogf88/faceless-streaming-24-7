#!/usr/bin/env python3
"""
Generador de Informe Ejecutivo en PDF: Canales Faceless y Transmisiones 24/7
Diseño visual editorial de alta calidad con ReportLab, logos oficiales integrados en cada página, tablas estilizadas y maquetación limpia.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.pdfgen import canvas

PDF_OUTPUT = "/Users/imac/Desktop/Informe_Maestro_Canales_Faceless_y_Streaming_24-7.pdf"
LOGO_DIR = "/Users/imac/.gemini/antigravity/scratch/logos"

# Paleta de Colores Moderna
COLOR_PRIMARY = colors.HexColor("#0F172A")    # Slate 900
COLOR_ACCENT = colors.HexColor("#4F46E5")     # Indigo 600
COLOR_CYAN = colors.HexColor("#0284C7")       # Sky 600
COLOR_BG_CARD = colors.HexColor("#F8FAFC")    # Slate 50
COLOR_BORDER = colors.HexColor("#E2E8F0")     # Slate 200
COLOR_TEXT = colors.HexColor("#1E293B")       # Slate 800
COLOR_MUTED = colors.HexColor("#64748B")      # Slate 500
COLOR_YT_RED = colors.HexColor("#DC2626")     # Red 600
COLOR_SUCCESS = colors.HexColor("#16A34A")    # Green 600
COLOR_WARNING = colors.HexColor("#D97706")    # Amber 600

class NumberedCanvas(canvas.Canvas):
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
            self.drawString(36, 755, "GUÍA MAESTRA · CANALES FACELESS & TRANSMISIONES 24/7 · AMDA AGENTIC ENGINE")
            self.setStrokeColor(COLOR_BORDER)
            self.setLineWidth(0.75)
            self.line(36, 748, 576, 748)

        # Footer (Todas las páginas)
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.75)
        self.line(36, 38, 576, 38)
        
        self.setFont("Helvetica", 8)
        self.drawString(36, 26, "Gemini Notebook: Canales Faceless & Streaming 24/7 · lic.jagf87@gmail.com")
        self.drawRightString(576, 26, f"Página {self._pageNumber} de {page_count}")
        self.restoreState()

def get_logo(name, width=16, height=16):
    path = os.path.join(LOGO_DIR, f"{name}.png")
    if os.path.exists(path):
        return Image(path, width=width, height=height)
    return Paragraph("", ParagraphStyle("empty"))

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_OUTPUT,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=44,
        bottomMargin=46
    )
    
    styles = getSampleStyleSheet()
    
    style_cover_title = ParagraphStyle(
        "CoverTitle",
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=COLOR_PRIMARY,
        spaceAfter=6
    )
    
    style_cover_sub = ParagraphStyle(
        "CoverSub",
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=COLOR_CYAN,
        spaceAfter=14
    )
    
    style_h1 = ParagraphStyle(
        "Heading1_Custom",
        fontName="Helvetica-Bold",
        fontSize=13.5,
        leading=17,
        textColor=COLOR_PRIMARY,
        spaceBefore=8,
        spaceAfter=5
    )

    style_h2 = ParagraphStyle(
        "Heading2_Custom",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=COLOR_ACCENT,
        spaceBefore=6,
        spaceAfter=4
    )
    
    style_body = ParagraphStyle(
        "Body_Custom",
        fontName="Helvetica",
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_TEXT,
        spaceAfter=3
    )

    style_body_bold = ParagraphStyle(
        "Body_Bold",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_TEXT
    )

    style_body_muted = ParagraphStyle(
        "Body_Muted",
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=COLOR_MUTED
    )

    style_code = ParagraphStyle(
        "CodeStyle",
        fontName="Courier",
        fontSize=7.2,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )
    
    story = []
    
    # -------------------------------------------------------------
    # PÁGINA 1: PORTADA & ARQUITECTURA HÍBRIDA
    # -------------------------------------------------------------
    logo_bar_data = [
        [
            get_logo("youtube", 26, 18),
            Paragraph("<b>YouTube Live 24/7</b>", style_body_bold),
            get_logo("googlegemini", 18, 18),
            Paragraph("<b>Gemini Notebook</b>", style_body_bold),
            get_logo("apple", 15, 18),
            Paragraph("<b>Apple M1 / macOS</b>", style_body_bold),
            get_logo("ffmpeg", 22, 16),
            Paragraph("<b>FFmpeg Core</b>", style_body_bold),
        ]
    ]
    t_logos = Table(logo_bar_data, colWidths=[24, 110, 24, 115, 20, 110, 24, 100])
    t_logos.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_logos)
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_ACCENT, spaceAfter=12))

    story.append(Paragraph("Informe Maestro de Arquitectura & Operación", style_cover_sub))
    story.append(Paragraph("Canales Faceless & Transmisiones en Vivo 24/7", style_cover_title))
    story.append(Paragraph("<i>Música para Concentración, Oración, Meditación y Sueño Profundo</i>", ParagraphStyle("subsub", fontName="Helvetica-Oblique", fontSize=11, textColor=COLOR_MUTED, spaceAfter=12)))
    
    exec_text = """
    <b>Propósito Estratégico:</b> Implementar un ecosistema de producción automatizada y transmisión continua 24/7 sin caídas para canales faceless de alta retención. Combina renderizado acelerado con hardware local (Mac M1), automatización de audio en lote (iMac 2015 24GB RAM), contingencia física (Dells Windows), captura de B-roll original 4K (iPhone 17 Pro Max) y emisión cloud ininterrumpida vía VPS Hetzner con FFmpeg, eliminando desgaste en discos duros locales y cortes por red doméstica.
    """
    t_exec = Table([[Paragraph(exec_text, style_body)]], colWidths=[540])
    t_exec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_CARD),
        ('BOX', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('LINELEFT', (0,0), (0,-1), 4, COLOR_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_exec)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Diagrama de Flujo del Ecosistema Híbrido", style_h1))
    
    arch_flow = [
        [
            Paragraph("<b>FASE 1: PRODUCCIÓN LOCAL</b>", ParagraphStyle("h_fase1", fontName="Helvetica-Bold", fontSize=8.5, textColor=COLOR_ACCENT)),
            Paragraph("<b>FASE 2: SINCRONIZACIÓN</b>", ParagraphStyle("h_fase2", fontName="Helvetica-Bold", fontSize=8.5, textColor=COLOR_CYAN)),
            Paragraph("<b>FASE 3: EMISIÓN 24/7 CLOUD</b>", ParagraphStyle("h_fase3", fontName="Helvetica-Bold", fontSize=8.5, textColor=COLOR_YT_RED))
        ],
        [
            Paragraph("• <b>Mac M1:</b> Render loops video (CapCut/Metal)<br/>• <b>iMac 24GB:</b> Audio master + Frecuencias Solfeggio<br/>• <b>iPhone 17 PM:</b> B-Roll 4K ProRes (Huella original)", style_body),
            Paragraph("• Subida por bloques vía Google Drive o rsync.<br/>• Archivos maestros MP4 de 4 a 6 horas ya codificados en H.264/AAC.", style_body),
            Paragraph("• <b>VPS Ubuntu (Hetzner ~$7/mes):</b><br/>  Daemon FFmpeg continuo en loop.<br/>• <b>YouTube Live RTMP</b> sin cortes.<br/>• <b>Redmi Note 8:</b> Monitor centinela.", style_body)
        ]
    ]
    t_arch = Table(arch_flow, colWidths=[180, 170, 190])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#EEF2FF")),
        ('BACKGROUND', (1,0), (1,-1), colors.HexColor("#F0F9FF")),
        ('BACKGROUND', (2,0), (2,-1), colors.HexColor("#FEF2F2")),
        ('BOX', (0,0), (0,-1), 1, colors.HexColor("#C7D2FE")),
        ('BOX', (1,0), (1,-1), 1, colors.HexColor("#BAE6FD")),
        ('BOX', (2,0), (2,-1), 1, colors.HexColor("#FECACA")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Evaluación Técnica de Estrategias de Emisión", style_h2))
    comp_data = [
        [Paragraph("<b>Estrategia</b>", style_body_bold), Paragraph("<b>Costo Est.</b>", style_body_bold), Paragraph("<b>Estabilidad 24/7</b>", style_body_bold), Paragraph("<b>Impacto en Hardware Local</b>", style_body_bold), Paragraph("<b>Veredicto</b>", style_body_bold)],
        [Paragraph("<b>Híbrido (Local + VPS)</b>", style_body), Paragraph("$7 USD / mes", style_body), Paragraph("99.9% Uptime (Datacenter)", style_body), Paragraph("Cero desgaste (Solo renderiza)", style_body), Paragraph("<font color='#16A34A'><b>ÓPTIMO</b></font>", style_body)],
        [Paragraph("<b>100% Local (Dell/iMac)</b>", style_body), Paragraph("Cero extra", style_body), Paragraph("Riesgo cortes luz/WiFi", style_body), Paragraph("Alto desgaste HDD/CPU 24/7", style_body), Paragraph("<font color='#D97706'>Vulnerable</font>", style_body)],
        [Paragraph("<b>SaaS (Gyre/LivePush)</b>", style_body), Paragraph("$35 - $60 / mes", style_body), Paragraph("Alta", style_body), Paragraph("Cero desgaste", style_body), Paragraph("<font color='#DC2626'>Costoso</font>", style_body)]
    ]
    t_comp = Table(comp_data, colWidths=[120, 75, 125, 140, 80])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_CARD),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_comp)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # PÁGINA 2: MATRIZ DE ASIGNACIÓN DE HARDWARE CON LOGOS
    # -------------------------------------------------------------
    story.append(Paragraph("Matriz Táctica de Asignación de Flota", style_h1))
    story.append(Paragraph("Aprovechamiento balanceado de cada dispositivo según su arquitectura de procesador, memoria RAM y almacenamiento.", style_body_muted))
    story.append(Spacer(1, 6))

    fleet_table = [
        [
            Paragraph("<b>Dispositivo & Hardware</b>", style_body_bold),
            Paragraph("<b>Especificaciones</b>", style_body_bold),
            Paragraph("<b>Rol Asignado</b>", style_body_bold),
            Paragraph("<b>Pipeline Específico</b>", style_body_bold)
        ],
        [
            Table([[get_logo("apple", 15, 18), Paragraph("<b>MacBook Pro 13\"</b><br/>Chip M1 (2020)", style_body)]], colWidths=[20, 105]),
            Paragraph("Apple Silicon M1<br/>8GB RAM · 256GB SSD", style_body_muted),
            Paragraph("<font color='#4F46E5'><b>Motor de Render Video</b></font>", style_body_bold),
            Paragraph("Render de loops 4K/1080p con aceleración Metal en CapCut/DaVinci. Ensamble de secuencias de 4-6 horas. Cero fatiga térmica.", style_body)
        ],
        [
            Table([[get_logo("apple", 15, 18), Paragraph("<b>iMac 27\"</b><br/>Monterey (2015)", style_body)]], colWidths=[20, 105]),
            Paragraph("Intel Core i5/i7<br/><b>24GB RAM</b> · 1TB HDD", style_body_muted),
            Paragraph("<font color='#0284C7'><b>Hub de Audio & Workflows</b></font>", style_body_bold),
            Paragraph("Aprovecha sus 24GB de RAM para bibliotecas masivas de audio. Generación de frecuencias binaurales, normalización a -14 LUFS y n8n.", style_body)
        ],
        [
            Table([[get_logo("dell", 16, 16), Paragraph("<b>Dell Windows #1</b><br/>Monitor 24\" 2K", style_body)]], colWidths=[20, 105]),
            Paragraph("Intel x64 · 8GB RAM<br/>512GB HDD · Windows", style_body_muted),
            Paragraph("<font color='#16A34A'><b>Staging & OBS Backup</b></font>", style_body_bold),
            Paragraph("Escenas pre-cargadas en OBS Studio como nodo de respaldo inmediato si el VPS entra en mantenimiento.", style_body)
        ],
        [
            Table([[get_logo("windows", 15, 15), Paragraph("<b>Dell Windows #2</b><br/>Monitor 24\" 2K", style_body)]], colWidths=[20, 105]),
            Paragraph("Intel x64 · 8GB RAM<br/>512GB HDD · Windows", style_body_muted),
            Paragraph("<font color='#D97706'><b>YouTube Studio & SEO</b></font>", style_body_bold),
            Paragraph("Monitor de analítica, optimización de palabras clave (VidIQ/TubeBuddy), diseño de miniaturas de alto CTR y moderación de chat.", style_body)
        ],
        [
            Table([[get_logo("apple", 15, 18), Paragraph("<b>iPhone 17 Pro Max</b><br/>Cámaras 48MP", style_body)]], colWidths=[20, 105]),
            Paragraph("A18 Pro · <b>1TB Storage</b><br/>Video ProRes 4K HDR", style_body_muted),
            Paragraph("<font color='#DC2626'><b>Huella Creativa Original</b></font>", style_body_bold),
            Paragraph("Grabación en 4K ProRes de lluvia sobre cristales, fuego, velas y santuarios (Prueba legal anti-contenido repetitivo). Directos 9:16 en TikTok.", style_body)
        ],
        [
            Table([[get_logo("xiaomi", 15, 15), Paragraph("<b>Redmi Note 8</b><br/>Pantalla 6.3\"", style_body)]], colWidths=[20, 105]),
            Paragraph("Snapdragon Octa-Core<br/>64GB + 128GB MicroSD", style_body_muted),
            Paragraph("<font color='#64748B'><b>Centinela 24/7 Dock</b></font>", style_body_bold),
            Paragraph("Instalado permanentemente en dock de escritorio para telemetría continua: app YouTube Studio y alertas inmediatas si el stream cae.", style_body)
        ],
    ]

    t_fleet = Table(fleet_table, colWidths=[130, 110, 120, 180])
    t_fleet.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_CARD),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_fleet)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Protocolo de Interconexión y Transferencia Local", style_h2))
    transfer_text = """
    1. <b>Captura a iMac:</b> El iPhone 17 PM descarga B-Roll original 4K vía AirDrop o cable Thunderbolt directo al disco de 1TB del iMac.<br/>
    2. <b>Audio Master:</b> El iMac procesa el audio con scripts de Python/FFmpeg integrando capas de naturaleza + frecuencias + voces de ElevenLabs.<br/>
    3. <b>Ensamble M1:</b> La MacBook M1 toma el audio y los clips visuales, generando el archivo maestro MP4 de 4 a 6 horas a 1080p con codificación acelerada por Metal.<br/>
    4. <b>Carga a VPS:</b> Se transfiere el archivo final mediante <code>rsync -P</code> o Google Drive directo al VPS de Hetzner para inicio inmediato.
    """
    t_trans = Table([[Paragraph(transfer_text, style_body)]], colWidths=[540])
    t_trans.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_trans)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # PÁGINA 3: BLINDAJE DE MONETIZACIÓN Y MATRIZ DE FRECUENCIAS
    # -------------------------------------------------------------
    bar_yt = [
        [
            get_logo("youtube", 24, 17),
            Paragraph("<b>Blindaje de Monetización YouTube (YPP 2026)</b>", style_h1),
            get_logo("googlegemini", 18, 18),
            Paragraph("<b>Estrategia Validada en Gemini Notebook</b>", ParagraphStyle("gn_tag", fontName="Helvetica", fontSize=9, textColor=COLOR_MUTED))
        ]
    ]
    t_baryt = Table(bar_yt, colWidths=[24, 250, 22, 244])
    t_baryt.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_baryt)
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_YT_RED, spaceAfter=8))

    story.append(Paragraph("Normas vigentes para evitar la desmonetización por 'Contenido Reutilizado' o 'Inauténtico'.", style_body_muted))
    story.append(Spacer(1, 4))

    rules_table = [
        [
            Paragraph("<b>Factor de Rechazo Frecuente</b>", style_body_bold),
            Paragraph("<b>Riesgo</b>", style_body_bold),
            Paragraph("<b>Estrategia de Blindaje Implementada</b>", style_body_bold)
        ],
        [
            Paragraph("<b>Contenido Reutilizado (Reused Content)</b>", style_body_bold),
            Paragraph("<font color='#DC2626'>CRÍTICO</font>", style_body),
            Paragraph("Prohibido usar solo librerías públicas gratuitas de YouTube. <b>Solución:</b> Se mezcla música generada por IA con licencia comercial (Suno/Udio) + grabaciones propias capturadas con el iPhone 17 PM.", style_body)
        ],
        [
            Paragraph("<b>Contenido Inauténtico / Repetitivo</b>", style_body_bold),
            Paragraph("<font color='#DC2626'>ALTO</font>", style_body),
            Paragraph("Imágenes fijas o bucles de video de 5 segundos son penalizados. <b>Solución:</b> Capas dinámicas HUD (temporizador de estudio, citas bíblicas o reflexiones cambiantes, partículas de lluvia o luz).", style_body)
        ],
        [
            Paragraph("<b>Falta de Valor Creativo (Background noise)</b>", style_body_bold),
            Paragraph("<font color='#D97706'>MEDIO</font>", style_body),
            Paragraph("Canales puramente de ruido blanco sufren baja preferencia de anunciantes. <b>Solución:</b> Incorporación de meditaciones y oraciones guiadas redactadas a medida con voz de ElevenLabs.", style_body)
        ]
    ]
    t_rules = Table(rules_table, colWidths=[150, 70, 320])
    t_rules.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_CARD),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_rules)
    story.append(Spacer(1, 8))

    story.append(Paragraph("Matriz de Frecuencias, Audio y Visuales por Nicho", style_h2))
    freq_table = [
        [
            Paragraph("<b>Nicho de Transmisión</b>", style_body_bold),
            Paragraph("<b>Frecuencia Clave</b>", style_body_bold),
            Paragraph("<b>Capa de Audio Base</b>", style_body_bold),
            Paragraph("<b>Escena Visual Recomendada</b>", style_body_bold)
        ],
        [
            Paragraph("📚 <b>Estudio & Foco Profundo</b>", style_body),
            Paragraph("<b>Ondas Alfa (8 - 12 Hz)</b><br/>Ruido Marrón continuo", style_body),
            Paragraph("Lofi Chillhop suave, teclado mecánico, lluvia lejana.", style_body),
            Paragraph("Habitación anime/minimalista, lluvia en ventana, luz cálida de lámpara.", style_body)
        ],
        [
            Paragraph("✝️ <b>Oración & Paz Espiritual</b>", style_body),
            Paragraph("<b>432 Hz / 528 Hz</b><br/>Frecuencia Reparadora", style_body),
            Paragraph("Pad etéreo celestial, piano suave, cuerdas tenues, salmos guiados.", style_body),
            Paragraph("Santuario iluminado, velas encendidas, amanecer en montañas sagradas.", style_body)
        ],
        [
            Paragraph("🧘 <b>Meditación & Calma</b>", style_body),
            Paragraph("<b>Ondas Theta (4 - 7 Hz)</b><br/>Frecuencia de trance", style_body),
            Paragraph("Cuencos tibetanos, arpa suave, sonido de agua corriente.", style_body),
            Paragraph("Bosque de bambú con brisa suave, lago al atardecer en loop imperceptible.", style_body)
        ],
        [
            Paragraph("🌙 <b>Sueño Profundo & Insomnio</b>", style_body),
            Paragraph("<b>Ondas Delta (0.5 - 3 Hz)</b><br/>Ruido Rosa / Lluvia", style_body),
            Paragraph("Drones estables de graves, tormenta sin truenos bruscos.", style_body),
            Paragraph("Cabina rústica en noche lluviosa con chimenea tenue, cielo estrellado.", style_body)
        ]
    ]
    t_freq = Table(freq_table, colWidths=[120, 110, 150, 160])
    t_freq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_BG_CARD),
        ('GRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_freq)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # PÁGINA 4: INFRAESTRUCTURA TÉCNICA VPS & SCRIPT FFmpeg CON LOGOS
    # -------------------------------------------------------------
    bar_vps = [
        [
            get_logo("hetzner", 18, 18),
            Paragraph("<b>Hetzner Cloud VPS</b>", style_body_bold),
            get_logo("ubuntu", 18, 18),
            Paragraph("<b>Ubuntu 24.04 LTS</b>", style_body_bold),
            get_logo("ffmpeg", 22, 16),
            Paragraph("<b>FFmpeg Streaming Engine</b>", style_body_bold),
            get_logo("obsstudio", 18, 18),
            Paragraph("<b>OBS Contingencia</b>", style_body_bold),
        ]
    ]
    t_barvps = Table(bar_vps, colWidths=[22, 115, 22, 110, 24, 140, 22, 85])
    t_barvps.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_barvps)
    story.append(HRFlowable(width="100%", thickness=1, color=COLOR_ACCENT, spaceAfter=8))

    story.append(Paragraph("1. Comando Maestro de Emisión Continua hacia YouTube Live", style_h2))
    code_ffmpeg = """# Transmisión en bucle cerrado (CBR estricto, 2s keyframe, cero buffering)
ffmpeg -re -stream_loop -1 -i /home/stream/media/master_stream.mp4 \\
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \\
  -c:v libx264 -preset veryfast -profile:v high \\
  -b:v 4500k -maxrate 4500k -bufsize 9000k \\
  -g 60 -keyint_min 60 -r 30 -pix_fmt yuv420p \\
  -c:a aac -b:a 160k -ar 44100 -ac 2 \\
  -f flv "rtmp://a.rtmp.youtube.com/live2/TU_CLAVE_DE_STREAM_AQUI"
"""
    t_code = Table([[Paragraph(code_ffmpeg.replace('\n', '<br/>'), style_code)]], colWidths=[540])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_code)
    story.append(Spacer(1, 6))

    story.append(Paragraph("2. Servicio de Auto-Arranque Permanente (systemd)", style_h2))
    code_systemd = """[Unit]
Description=YouTube 24/7 Live Stream Daemon
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/stream
ExecStart=/usr/bin/ffmpeg -re -stream_loop -1 -i /home/stream/media/master_stream.mp4 -c:v copy -c:a copy -f flv "rtmp://a.rtmp.youtube.com/live2/CLAVE_AQUI"
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
"""
    t_sys = Table([[Paragraph(code_systemd.replace('\n', '<br/>'), style_code)]], colWidths=[540])
    t_sys.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_sys)
    story.append(Spacer(1, 6))

    story.append(Paragraph("3. Plan de Acción de Ejecución Autónoma", style_h2))
    steps_text = """
    • <b>Paso 1 (Creación de Activos):</b> Generar paquete de 10 pistas de 30 min en el iMac (Suno/Udio + frecuencias 432Hz/ondas alfa).<br/>
    • <b>Paso 2 (Render M1):</b> Ensamblar un video continuo de 4-6 horas con CapCut acelerado por Metal en la MacBook M1.<br/>
    • <b>Paso 3 (Despliegue VPS):</b> Levantar el VPS en Hetzner Cloud (Ubuntu) y cargar el archivo <code>master_stream.mp4</code>.<br/>
    • <b>Paso 4 (Lanzamiento YouTube):</b> Configurar evento de emisión en directo en YouTube Studio con clave persistente.<br/>
    • <b>Paso 5 (Centinela):</b> Montar el Xiaomi Redmi Note 8 en dock como pantalla de monitoreo y activar el demonio systemd.
    """
    t_steps = Table([[Paragraph(steps_text, style_body)]], colWidths=[540])
    t_steps.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#ECFDF5")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#A7F3D0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_steps)
    story.append(Spacer(1, 6))

    gn_text = """
    <b>Sincronización en la Nube:</b> Este documento y su matriz técnica están respaldados en tu cuenta activa de Gemini Notebook:<br/>
    <a href="https://notebook.google.com/notebook/5669c58a-cca1-4701-bc02-b8db7f5bbb24"><u><b>https://notebook.google.com/notebook/5669c58a-cca1-4701-bc02-b8db7f5bbb24</b></u></a>
    """
    story.append(Paragraph(gn_text, style_body_muted))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado con éxito en: {PDF_OUTPUT}")

if __name__ == "__main__":
    build_pdf()
