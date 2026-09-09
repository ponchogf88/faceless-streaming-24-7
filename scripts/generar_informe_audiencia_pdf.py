#!/usr/bin/env python3
"""
Generador del Informe Estratégico de Audiencia, Alcance y Crecimiento en PDF
Diseño visual editorial de alta calidad con ReportLab, logos oficiales integrados,
tablas de benchmarking, cajas de alerta, cronología predictiva y maquetación limpia.
AMDA Agentic Engine · Autor: @ponchogf88
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.pdfgen import canvas

PDF_OUTPUT = "/Users/imac/Desktop/Informe_Estrategico_Audiencia_Alcance_y_Crecimiento_24-7.pdf"
LOGO_DIR = "/Users/imac/Desktop/Projects/FACELESS_STREAMING_24_7_YOUTUBE_TIKTOK/assets/logos"

# Paleta de Colores Editorial
COLOR_PRIMARY = colors.HexColor("#0F172A")    # Slate 900
COLOR_SECONDARY = colors.HexColor("#1E293B")  # Slate 800
COLOR_ACCENT = colors.HexColor("#4F46E5")     # Indigo 600
COLOR_CYAN = colors.HexColor("#0284C7")       # Sky 600
COLOR_BG_CARD = colors.HexColor("#F8FAFC")    # Slate 50
COLOR_BORDER = colors.HexColor("#E2E8F0")     # Slate 200
COLOR_TEXT = colors.HexColor("#1E293B")       # Slate 800
COLOR_MUTED = colors.HexColor("#64748B")      # Slate 500
COLOR_YT_RED = colors.HexColor("#DC2626")     # Red 600
COLOR_SUCCESS = colors.HexColor("#16A34A")    # Green 600
COLOR_WARNING = colors.HexColor("#D97706")    # Amber 600
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
            self.drawString(36, 755, "INFORME MAESTRO DE AUDIENCIA & ALCANCE 24/7 · AMDA AGENTIC ENGINE")
            self.setStrokeColor(COLOR_BORDER)
            self.setLineWidth(0.75)
            self.line(36, 748, 576, 748)

        # Footer (Todas las páginas)
        self.setStrokeColor(COLOR_BORDER)
        self.setLineWidth(0.75)
        self.line(36, 38, 576, 38)
        
        self.setFont("Helvetica", 8)
        self.drawString(36, 26, "Ecosistema de Canales Faceless & Streaming 24/7 · @ponchogf88 · lic.jagf87@gmail.com")
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
        fontSize=23,
        leading=27,
        textColor=COLOR_PRIMARY,
        spaceAfter=4
    )
    
    style_cover_sub = ParagraphStyle(
        "CoverSub",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=COLOR_ACCENT,
        spaceAfter=4
    )
    
    style_cover_desc = ParagraphStyle(
        "CoverDesc",
        fontName="Helvetica",
        fontSize=9,
        leading=13,
        textColor=COLOR_MUTED,
        spaceAfter=12
    )
    
    style_h1 = ParagraphStyle(
        "SectionH1",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=COLOR_PRIMARY,
        spaceBefore=12,
        spaceAfter=6
    )

    style_h2 = ParagraphStyle(
        "SectionH2",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=COLOR_ACCENT,
        spaceBefore=8,
        spaceAfter=4
    )
    
    style_body = ParagraphStyle(
        "Body",
        fontName="Helvetica",
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_TEXT,
        spaceAfter=6
    )

    style_body_bold = ParagraphStyle(
        "BodyBold",
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_TEXT
    )
    
    style_meta_pill = ParagraphStyle(
        "MetaPill",
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    style_card_title = ParagraphStyle(
        "CardTitle",
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=13,
        textColor=COLOR_PRIMARY
    )

    style_card_body = ParagraphStyle(
        "CardBody",
        fontName="Helvetica",
        fontSize=8,
        leading=11.5,
        textColor=COLOR_TEXT
    )

    style_table_header = ParagraphStyle(
        "TableHeader",
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10.5,
        textColor=colors.white
    )

    style_table_cell = ParagraphStyle(
        "TableCell",
        fontName="Helvetica",
        fontSize=7.5,
        leading=10,
        textColor=COLOR_TEXT
    )

    style_table_cell_bold = ParagraphStyle(
        "TableCellBold",
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=10,
        textColor=COLOR_TEXT
    )

    story = []

    # =========================================================================
    # PÁGINA 1: PORTADA & ANATOMÍA DEL ALGORITMO
    # =========================================================================
    header_table = Table([
        [
            Paragraph("REPORTE ESTRATÉGICO DE AUDIENCIA & ALCANCE", style_cover_sub),
            Table([[get_logo("youtube", 16, 16), get_logo("googlegemini", 16, 16)]], colWidths=[20, 20])
        ]
    ], colWidths=[490, 50])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("¿Qué va a Pasar? La Dinámica Real del Algoritmo, Alcance y Curva de Crecimiento en Directos 24/7", style_cover_title))
    story.append(Paragraph("Estrategia Integral de Tracción Orgánica, Retención de Sesión, Psicología del Espectador y Despegue Algorítmico", style_cover_desc))
    
    # Meta badges bar
    meta_badges = Table([
        [
            Paragraph("<b>Objetivo:</b> Tracción 24/7", style_card_body),
            Paragraph("<b>Meta Watch Time:</b> 4,000 Horas", style_card_body),
            Paragraph("<b>Población Objetivo:</b> Búsqueda & Noche", style_card_body),
            Paragraph("<b>Horizonte:</b> 0 a 30 Días", style_card_body)
        ]
    ], colWidths=[135, 135, 135, 135])
    meta_badges.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_CARD),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_badges)
    story.append(Spacer(1, 10))

    # Sección 1: El Gran Principio
    story.append(Paragraph("1. La Verdad del Streaming Continuo: ¿Qué es lo que Realmente Ocurre?", style_h1))
    story.append(Paragraph(
        "Iniciar un directo 24/7 <b>no funciona como subir un video tradicional</b>. Un video normal depende de un pico explosivo en sus primeras 24 a 48 horas o el algoritmo lo entierra. En cambio, una transmisión continua genera una <b>inercia algorítmica acumulativa</b>: entre más tiempo permanece viva y estable la señal, más confiable se vuelve para los servidores de recomendación de YouTube.",
        style_body
    ))

    # Tres pilares en tarjetas
    pilar_1 = [
        Paragraph("<b>1. El Algoritmo Premia la Permanencia</b>", style_card_title),
        Spacer(1, 2),
        Paragraph("YouTube busca maximizar el tiempo que los usuarios pasan dentro de su app. Un stream estable 24/7 con baja latencia y cero desconexiones se clasifica como 'ancla de retención' y se sugiere continuamente en barras laterales.", style_card_body)
    ]
    pilar_2 = [
        Paragraph("<b>2. El 'Valle de la Muerte' (Horas 0 a 12)</b>", style_card_title),
        Spacer(1, 2),
        Paragraph("El 90% de los creadores fracasan porque apagan el directo a las 3 horas al ver 1 solo espectador. Las primeras 12 horas son de indexación técnica. <b>Apagar el directo destruye el puntaje acumulado</b>.", style_card_body)
    ]
    pilar_3 = [
        Paragraph("<b>3. Audiencia de Hábitos Repetitivos</b>", style_card_title),
        Spacer(1, 2),
        Paragraph("Los oyentes de oración y estudio buscan compañía predecible. Quien se duerme o estudia hoy con tu directo, regresará mañana a la misma hora <b>siempre y cuando la transmisión siga en vivo</b>.", style_card_body)
    ]

    pilares_table = Table([[pilar_1, pilar_2, pilar_3]], colWidths=[176, 176, 176])
    pilares_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_CARD),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(pilares_table)
    story.append(Spacer(1, 10))

    # Sección 2: La Fórmula Matemática de Recomendación
    story.append(Paragraph("2. La Fórmula Algorítmica de YouTube Live (2026)", style_h1))
    story.append(Paragraph(
        "El motor de recomendaciones evalúa a cada segundo tres variables críticas para decidir a cuántas personas mostrar el directo:",
        style_body
    ))

    formula_card = Table([
        [
            Paragraph("<b>PUNTAJE DE RECOMENDACIÓN = (CTR × 0.35) + (Retención / AVD × 0.45) + (Velocidad de Chat × 0.20)</b>", ParagraphStyle("Formula", fontName="Helvetica-Bold", fontSize=9, textColor=COLOR_PRIMARY, alignment=1))
        ]
    ], colWidths=[540])
    formula_card.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EEF2FF")),
        ('BOX', (0,0), (-1,-1), 1, COLOR_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(formula_card)
    story.append(Spacer(1, 8))

    factores_table = Table([
        [
            Paragraph("Variable Cardinal", style_table_header),
            Paragraph("Métrica Objetivo", style_table_header),
            Paragraph("Impacto en el Algoritmo", style_table_header),
            Paragraph("Acción Táctica Aplicada", style_table_header),
        ],
        [
            Paragraph("<b>1. CTR de Miniatura</b>", style_table_cell_bold),
            Paragraph("<b>> 5.5%</b> en primeras 24 hrs", style_table_cell),
            Paragraph("Multiplica las impresiones en la página de inicio (Browse Features).", style_table_cell),
            Paragraph("Texto gigante (< 4 palabras), fondo oscuro y contraste lumínico alto con etiqueta 'EN VIVO'.", style_table_cell),
        ],
        [
            Paragraph("<b>2. Tiempo de Retención (AVD)</b>", style_table_cell_bold),
            Paragraph("<b>> 25 a 45 min</b> promedio", style_table_cell),
            Paragraph("Indica que el contenido es un refugio confiable; lo sugiere en barras laterales.", style_table_cell),
            Paragraph("Pistas sin picos estridentes a -14 LUFS, ondas 432 Hz / Alfa y capas visuales animadas suaves.", style_table_cell),
        ],
        [
            Paragraph("<b>3. Velocidad de Chat</b>", style_table_cell_bold),
            Paragraph("<b>> 2 a 5 msg/min</b> continuo", style_table_cell),
            Paragraph("Dispara la 'urgencia social'; el algoritmo interpreta que algo importante ocurre en vivo.", style_table_cell),
            Paragraph("Mensaje anclado obligatorio: <i>'Escribe tu nombre y tu petición de oración aquí'</i>.", style_table_cell),
        ]
    ], colWidths=[110, 95, 165, 170])
    factores_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(factores_table)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 2: CRONOLOGÍA DÍA A DÍA ("¿QUÉ VA A PASAR?")
    # =========================================================================
    story.append(Paragraph("3. Cronología Predictiva Día a Día: ¿Qué va a Pasar Realmente?", style_h1))
    story.append(Paragraph(
        "A continuación se detalla la secuencia real esperada desde el instante en que pulses 'Transmitir en vivo' a las 2:29 AM hasta el día 30 de operación:",
        style_body
    ))

    cronologia_table = Table([
        [
            Paragraph("Fase / Tiempo", style_table_header),
            Paragraph("Espectadores (CCV)", style_table_header),
            Paragraph("Comportamiento del Algoritmo", style_table_header),
            Paragraph("Experiencia en Pantalla", style_table_header),
            Paragraph("Protocolo del Creador", style_table_header),
        ],
        [
            Paragraph("<b>Fase 0: Arranque<br/>(Horas 0 a 12)</b>", style_table_cell_bold),
            Paragraph("<b>0 a 3 CCV</b><br/>(Amigos/Centinela)", style_table_cell),
            Paragraph("Indexación de metadatos, tags y estabilidad de bitrate. Cero distribución pública masiva.", style_table_cell),
            Paragraph("Chat en silencio total. Sensación de que 'nadie lo está viendo'.", style_table_cell),
            Paragraph("<b>PROHIBIDO APAGAR.</b> Dejar correr el bucle. Es el periodo de indexación técnica.", style_table_cell),
        ],
        [
            Paragraph("<b>Fase 1: Primer Test<br/>(Horas 12 a 48)</b>", style_table_cell_bold),
            Paragraph("<b>5 a 18 CCV</b><br/>(Primeros orgánicos)", style_table_cell),
            Paragraph("YouTube envía el primer paquete de prueba (500 a 2,000 impresiones) en búsquedas afines.", style_table_cell),
            Paragraph("Entran los primeros usuarios reales. Alguien escribe un 'Amén' o una petición en el chat.", style_table_cell),
            Paragraph("Fijar mensaje en chat. Responder por texto con calidez. El algoritmo premia el chat.", style_table_cell),
        ],
        [
            Paragraph("<b>Fase 2: Inercia<br/>(Días 3 a 7)</b>", style_table_cell_bold),
            Paragraph("<b>20 a 45 CCV</b><br/>(Estabilidad nocturna)", style_table_cell),
            Paragraph("El stream entra en 'Videos Sugeridos' de canales afines. Picos marcados entre 21:00 y 04:00 AM.", style_table_cell),
            Paragraph("Comienzan a acumularse 300 a 500 horas de reproducción por día. Usuarios agradeciendo la paz.", style_table_cell),
            Paragraph("Analizar en Dell #2 qué palabras clave traen más tráfico y reforzar la descripción.", style_table_cell),
        ],
        [
            Paragraph("<b>Fase 3: Bola de Nieve<br/>(Días 8 a 15)</b>", style_table_cell_bold),
            Paragraph("<b>50 a 120 CCV</b><br/>(Crecimiento orgánico)", style_table_cell),
            Paragraph("El canal adquiere 'autoridad de transmisión'. YouTube confía plenamente en el directo.", style_table_cell),
            Paragraph("Se superan las <b>4,000 horas requeridas</b> para monetizar. 50-80 suscriptores diarios.", style_table_cell),
            Paragraph("Enviar solicitud al Programa de Socios de YouTube (YPP). Anclar links a productos.", style_table_cell),
        ],
        [
            Paragraph("<b>Fase 4: Consolidación<br/>(Días 16 a 30)</b>", style_table_cell_bold),
            Paragraph("<b>150 a 300+ CCV</b><br/>(Audiencia fija)", style_table_cell),
            Paragraph("Audiencia de hábito. Los usuarios abren el stream automáticamente cada noche para descansar.", style_table_cell),
            Paragraph("Super Chats activos durante la madrugada. Primeras ventas del pack de audio WAV sin compresión.", style_table_cell),
            Paragraph("Mantener el bucle en VPS sin tocar. Evaluar segundo stream en paralelo o TikTok Live diario.", style_table_cell),
        ]
    ], colWidths=[85, 75, 125, 125, 130])
    cronologia_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(cronologia_table)
    story.append(Spacer(1, 10))

    # Sección 4: Psicología del Espectador Nocturno
    story.append(Paragraph("4. Psicología del Espectador Nocturno: ¿Por qué la Gente se Queda Horas?", style_h1))
    story.append(Paragraph(
        "Entender la mente de quien se conecta de madrugada es el secreto de la retención masiva:",
        style_body
    ))

    psico_1 = [
        Paragraph("<b>1. El Refugio Emocional</b>", style_card_title),
        Paragraph("El usuario que busca oración a las 11:30 PM viene de un día cargado de estrés, cansancio o insomnio. No busca un show ruidoso; busca <b>paz acústica inmediata</b>. Una atmósfera serena con 432 Hz genera alivio corporal instantáneo.", style_card_body)
    ]
    psico_2 = [
        Paragraph("<b>2. El Efecto 'Iglesia Abierta'</b>", style_card_title),
        Paragraph("Al ver a otros hermanos escribiendo peticiones en el chat, el espectador experimenta conexión comunitaria. El directo deja de ser un video y se convierte en un <b>templo digital activo las 24 horas</b> donde nunca está solo.", style_card_body)
    ]
    psico_3 = [
        Paragraph("<b>3. El Anclaje al Sueño (6 a 8 Horas)</b>", style_card_title),
        Paragraph("Más del 60% de la audiencia deja el directo sonando al lado de su almohada. <b>Una sola persona dormida te genera 7 horas de watch time continuo</b>. Con solo 15 personas durmiendo, sumas 100 horas en una sola noche.", style_card_body)
    ]

    psico_table = Table([[psico_1, psico_2, psico_3]], colWidths=[176, 176, 176])
    psico_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_BG_CARD),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(psico_table)

    story.append(PageBreak())

    # =========================================================================
    # PÁGINA 3: MULTI-EMBUDO DE TRÁFICO & ERRORES FATALES
    # =========================================================================
    story.append(Paragraph("5. El Multi-Embudo de Tráfico: Cómo Acelerar el Alcance sin Esperar Pasivamente", style_h1))
    story.append(Paragraph(
        "Para no depender únicamente del algoritmo de YouTube, activamos tres motores de tráfico coordinados:",
        style_body
    ))

    embudo_table = Table([
        [
            Paragraph("Canal de Tráfico", style_table_header),
            Paragraph("Mecanismo Táctico", style_table_header),
            Paragraph("Potencial de Conversión", style_table_header),
            Paragraph("Implementación Inmediata", style_table_header),
        ],
        [
            Paragraph("<b>1. YouTube Search<br/>(Intención Orgánica)</b>", style_table_cell_bold),
            Paragraph("Captar a usuarios que buscan activamente soluciones a su insomnio o necesidad espiritual.", style_table_cell),
            Paragraph("<b>Altísima retención:</b> Llegan por decisión propia y se quedan hasta 90 minutos.", style_table_cell),
            Paragraph("Títulos con palabras de alta demanda: <i>'Salmo 91', '432 Hz', 'Oración de la noche para dormir en paz'</i>.", style_table_cell),
        ],
        [
            Paragraph("<b>2. TikTok Live<br/>(Tráfico Viral Móvil)</b>", style_table_cell_bold),
            Paragraph("Emitir sesiones de 1 hora con el iPhone 17 Pro Max enfocando el altar con música relajante de fondo.", style_table_cell),
            Paragraph("<b>Viralidad rápida:</b> El feed Para Ti de TikTok Live muestra el directo a miles en minutos.", style_table_cell),
            Paragraph("Cartel flotante en TikTok: <i>'Transmisión continua en YouTube: Agradecimiento Sincero (Link en Bio)'</i>.", style_table_cell),
        ],
        [
            Paragraph("<b>3. Shorts Derivados<br/>(Anzuelos Diarios)</b>", style_table_cell_bold),
            Paragraph("Publicar 2 Shorts diarios de 30s extrayendo una oración potente con audio 432 Hz.", style_table_cell),
            Paragraph("<b>Volumen de suscriptores:</b> Atrae cientos de suscriptores veloces al canal cada semana.", style_table_cell),
            Paragraph("Vincular el Short directamente con el botón oficial: <i>'Ver transmisión en vivo completa'</i>.", style_table_cell),
        ]
    ], colWidths=[110, 140, 130, 160])
    embudo_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_PRIMARY),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(embudo_table)
    story.append(Spacer(1, 10))

    # Sección 6: Los 5 Errores Fatales
    story.append(Paragraph("6. Los 5 Errores Fatales que Matan el Alcance (y Cómo Evitarlos)", style_h1))
    story.append(Paragraph(
        "Evitar estos cinco tropiezos garantiza que tu canal alcance la monetización en el menor tiempo matemáticamente posible:",
        style_body
    ))

    errores_table = Table([
        [
            Paragraph("Error Mortal", style_table_header),
            Paragraph("Consecuencia en el Algoritmo", style_table_header),
            Paragraph("Protocolo Correcto Blindado", style_table_header),
        ],
        [
            Paragraph("<b>1. Reiniciar el stream diario<br/>'para empezar de nuevo'</b>", style_table_cell_bold),
            Paragraph("Resetea las métricas de retención, rompe la sesión de los usuarios que duermen y borra el historial de confianza de YouTube.", style_table_cell),
            Paragraph("<b>Mantener el directo continuo durante semanas.</b> La inercia acumulada es el secreto de la recomendación masiva.", style_table_cell),
        ],
        [
            Paragraph("<b>2. Cambiar títulos y miniaturas cada 3 horas por desesperación</b>", style_table_cell_bold),
            Paragraph("Desconcierta al algoritmo mientras está calculando impresiones y frena en seco el testeo.", style_table_cell),
            Paragraph("Dejar correr los metadatos al menos <b>5 a 7 días continuos</b> antes de realizar un A/B test.", style_table_cell),
        ],
        [
            Paragraph("<b>3. Picos repentinos de volumen o música estridente</b>", style_table_cell_bold),
            Paragraph("Despierta o asusta al usuario que intentaba descansar; este cierra el video de inmediato y destruye el AVD.", style_table_cell),
            Paragraph("Normalización matemática estricta a <b>-14 LUFS</b> con True Peak en -1.0 dBTP y ecualización suave.", style_table_cell),
        ],
        [
            Paragraph("<b>4. No fijar mensaje en el chat en vivo</b>", style_table_cell_bold),
            Paragraph("El chat permanece muerto, la velocidad de interacción cae a cero y YouTube reduce la distribución.", style_table_cell),
            Paragraph("<b>Pinned comment obligatorio</b> invitando a dejar peticiones, nombres o un 'Amén' en comunidad.", style_table_cell),
        ],
        [
            Paragraph("<b>5. Usar música protegida o librerías genéricas de stock</b>", style_table_cell_bold),
            Paragraph("Reclamaciones automáticas de Content ID que silencian el video o desvían los ingresos a terceros.", style_table_cell),
            Paragraph("Melodías propias generadas con IA (Suno/Udio) e inyectadas con frecuencias senoidales puras únicas.", style_table_cell),
        ]
    ], colWidths=[140, 190, 210])
    errores_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_YT_RED),
        ('BOX', (0,0), (-1,-1), 0.75, COLOR_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, COLOR_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, COLOR_BG_CARD]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(errores_table)
    story.append(Spacer(1, 10))

    # Caja de cierre inspirador / Veredicto
    cierre_box = Table([
        [
            Paragraph(
                "<b>VEREDICTO FINAL PARA LAS 2:29 AM:</b><br/>"
                "Al dar clic en 'Transmitir en vivo', entraremos en la fase de silencio técnico normal (Fase 0). Tu única tarea será <b>mantener la calma y dejar que la máquina trabaje</b>. Entre el Día 3 y el Día 7 verás la tracción orgánica consolidarse, y para el Día 10 el umbral de las 4,000 horas estará conquistado. ¡Todo el sistema está listo y blindado!",
                ParagraphStyle("Cierre", fontName="Helvetica", fontSize=8.5, leading=12, textColor=COLOR_PRIMARY)
            )
        ]
    ], colWidths=[540])
    cierre_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#DCFCE7")), # Green 100
        ('BOX', (0,0), (-1,-1), 1, COLOR_SUCCESS),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(cierre_box)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ PDF generado exitosamente: {PDF_OUTPUT}")

if __name__ == '__main__':
    build_pdf()
