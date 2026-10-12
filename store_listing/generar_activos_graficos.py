import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUTPUT_DIR = "store_listing/graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta cromática oficial de Cómo Gasto
COLOR_BG = (15, 23, 42)           # #0F172A - slate 900
COLOR_CARD = (30, 41, 59)         # #1E293B - slate 800
COLOR_PRIMARY = (74, 144, 226)    # #4A90E2 - azul principal de la app
COLOR_PRIMARY_DARK = (37, 99, 235)# #2563EB
COLOR_ACCENT = (99, 102, 241)     # #6366F1 - índigo
COLOR_TEXT = (241, 245, 249)      # #F1F5F9 - texto claro
COLOR_MUTED = (148, 163, 184)     # #94A3B8 - texto secundario
COLOR_SUCCESS = (52, 211, 153)    # #34D399 - verde ingresos/ahorro
COLOR_CHART_1 = (74, 144, 226)    # Azul
COLOR_CHART_2 = (244, 63, 94)     # Rojo / Comida
COLOR_CHART_3 = (245, 158, 11)    # Ámbar / Servicios
COLOR_CHART_4 = (16, 185, 129)    # Verde / Salud
COLOR_CHART_5 = (168, 85, 247)    # Violeta / Entretenimiento

# Fuentes tipográficas del sistema
FONT_BOLD_PATHS = [
    "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf",
]
FONT_REGULAR_PATHS = [
    "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf",
]

def get_font(paths, size):
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

# ─────────────────────────────────────────────────────────────────────────────
# 1. ÍCONO DE TIENDA: 512x512 PNG sin transparencias (100% Opaco para Play Store)
# ─────────────────────────────────────────────────────────────────────────────
def generar_icono_512():
    size = (512, 512)
    canvas = Image.new("RGB", size, COLOR_PRIMARY)
    draw = ImageDraw.Draw(canvas)
    
    # Fondo con sutil degradado radial
    for y in range(size[1]):
        ratio = y / size[1]
        r = int(COLOR_PRIMARY[0] * (1 - ratio * 0.2))
        g = int(COLOR_PRIMARY[1] * (1 - ratio * 0.2))
        b = int(COLOR_PRIMARY[2] * (1 - ratio * 0.15))
        draw.line([(0, y), (size[0], y)], fill=(r, g, b))
        
    # Cargar y centrar el logo oficial de la app
    logo_src_path = "assets/launcher_icon_ios.png"
    if os.path.exists(logo_src_path):
        logo_im = Image.open(logo_src_path).convert("RGBA")
        # Recortar márgenes si existen y redimensionar con Lanczos
        logo_size = 460
        logo_resized = logo_im.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Efecto de sombra suave
        shadow = Image.new("RGBA", size, (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        offset = (size[0] - logo_size) // 2
        shadow_draw.rounded_rectangle(
            [offset, offset + 6, offset + logo_size, offset + logo_size + 6],
            radius=90,
            fill=(0, 0, 0, 70)
        )
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=12))
        
        canvas_rgba = canvas.convert("RGBA")
        canvas_rgba.alpha_composite(shadow)
        canvas_rgba.alpha_composite(logo_resized, (offset, offset))
        final_icon = canvas_rgba.convert("RGB")
    else:
        final_icon = canvas
        
    dest_path = os.path.join(OUTPUT_DIR, "00_icono_512.png")
    final_icon.save(dest_path, "PNG", optimize=True)
    final_icon.save(os.path.join(OUTPUT_DIR, "icono_512.png"), "PNG", optimize=True)
    print(f"✓ Ícono oficial de tienda generado: {dest_path} (512x512 RGB)")

# ─────────────────────────────────────────────────────────────────────────────
# 2. GRÁFICO DESTACADO: 1024x500 PNG sin transparencias
# ─────────────────────────────────────────────────────────────────────────────
def generar_grafico_destacado():
    width, height = 1024, 500
    canvas = Image.new("RGB", (width, height), COLOR_BG)
    draw = ImageDraw.Draw(canvas)
    
    # Fondo degradado horizontal y vertical
    for y in range(height):
        ratio_y = y / height
        for x in range(0, width, 4):
            ratio_x = x / width
            r = int(COLOR_BG[0] * (1 - ratio_x * 0.3) + COLOR_PRIMARY_DARK[0] * ratio_x * 0.15)
            g = int(COLOR_BG[1] * (1 - ratio_x * 0.3) + COLOR_PRIMARY_DARK[1] * ratio_x * 0.25)
            b = int(COLOR_BG[2] * (1 - ratio_x * 0.1) + COLOR_PRIMARY_DARK[2] * ratio_x * 0.35)
            draw.line([(x, y), (x + 3, y)], fill=(r, g, b))
            
    # Cuadrícula sutil financiera
    grid_color = (25, 36, 56)
    for x in range(0, width, 36):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 36):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)
        
    # Halo luminoso detrás del logo y títulos
    halo = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    halo_draw = ImageDraw.Draw(halo)
    halo_draw.ellipse([60, 40, 440, 460], fill=(74, 144, 226, 120))
    halo_draw.ellipse([450, 80, 980, 420], fill=(37, 99, 235, 90))
    halo = halo.filter(ImageFilter.GaussianBlur(radius=50))
    
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba.alpha_composite(halo)
    
    # Logo a la izquierda (300x300)
    logo_src_path = "assets/launcher_icon_ios.png"
    if os.path.exists(logo_src_path):
        logo_im = Image.open(logo_src_path).convert("RGBA")
        logo_size = 310
        logo_resized = logo_im.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        canvas_rgba.alpha_composite(logo_resized, (70, (height - logo_size) // 2))
        
    # Textos y elementos tipográficos
    title_font = get_font(FONT_BOLD_PATHS, 48)
    badge_font = get_font(FONT_BOLD_PATHS, 14)
    sub_font = get_font(FONT_BOLD_PATHS, 21)
    feat_font = get_font(FONT_REGULAR_PATHS, 16)
    
    text_draw = ImageDraw.Draw(canvas_rgba)
    
    # Badge superior
    badge_x, badge_y = 430, 95
    badge_w, badge_h = 320, 32
    text_draw.rounded_rectangle(
        [badge_x, badge_y, badge_x + badge_w, badge_y + badge_h],
        radius=16,
        fill=(30, 58, 138, 220),
        outline=COLOR_PRIMARY,
        width=1
    )
    text_draw.text((badge_x + 18, badge_y + 7), "CONTROL FINANCIERO PERSONAL", font=badge_font, fill=COLOR_PRIMARY)
    
    # Título principal
    text_draw.text((430, 140), "CÓMO GASTO", font=title_font, fill=(255, 255, 255))
    
    # Subtítulo descriptivo
    text_draw.text((430, 208), "Gestiona tus finanzas y gastos diarios", font=sub_font, fill=COLOR_PRIMARY)
    
    # Viñetas de características clave
    features = [
        "• Gráficos dinámicos de barras y torta por rubro",
        "• Registro ágil de compras con teclado numérico",
        "• Selector mensual interactivo con desglose",
        "• Modo Fuera de Línea con Modo Oscuro integrado"
    ]
    fy = 255
    for feat in features:
        text_draw.text((430, fy), feat, font=feat_font, fill=COLOR_TEXT)
        fy += 32
        
    final_graphic = canvas_rgba.convert("RGB")
    dest_path = os.path.join(OUTPUT_DIR, "grafico_destacado_1024x500.png")
    final_graphic.save(dest_path, "PNG", optimize=True)
    print(f"✓ Gráfico destacado generado: {dest_path} (1024x500 RGB)")

# ─────────────────────────────────────────────────────────────────────────────
# 3. GENERADOR DE CAPTURAS DE PANTALLA EN RESOLUCIÓN EXACTA (1344 x 2688 - 1:2)
# ─────────────────────────────────────────────────────────────────────────────
SCREEN_W = 1344
SCREEN_H = 2688

def crear_base_pantalla(titulo_appbar="Cómo Gasto", tiene_appbar=True, modo_oscuro=False):
    bg_col = (18, 18, 18) if modo_oscuro else (248, 250, 252)
    card_col = (30, 30, 30) if modo_oscuro else (255, 255, 255)
    text_col = (255, 255, 255) if modo_oscuro else (15, 23, 42)
    
    im = Image.new("RGB", (SCREEN_W, SCREEN_H), bg_col)
    d = ImageDraw.Draw(im)
    
    font_appbar = get_font(FONT_BOLD_PATHS, 48)
    
    if tiene_appbar:
        # AppBar superior
        appbar_h = 160
        d.rectangle([(0, 0), (SCREEN_W, appbar_h)], fill=(103, 58, 183) if not modo_oscuro else (33, 33, 33))
        d.text((70, 50), titulo_appbar, font=font_appbar, fill=(255, 255, 255))
        
    return im, d, bg_col, card_col, text_col

def generar_capturas_tienda():
    font_big = get_font(FONT_BOLD_PATHS, 64)
    font_mid = get_font(FONT_BOLD_PATHS, 42)
    font_regular = get_font(FONT_REGULAR_PATHS, 34)
    font_small = get_font(FONT_REGULAR_PATHS, 28)
    
    # ── 01_login.png ─────────────────────────────────────────────────────────
    im1 = Image.new("RGB", (SCREEN_W, SCREEN_H), (255, 255, 255))
    d1 = ImageDraw.Draw(im1)
    
    # Título login
    d1.text((SCREEN_W // 2 - 180, 280), "Cómo Gasto", font=font_big, fill=COLOR_PRIMARY)
    
    # Ilustración / imagen central de login
    login_img_path = "assets/login_background.png"
    if os.path.exists(login_img_path):
        bg_logo = Image.open(login_img_path).convert("RGBA")
        bg_logo = bg_logo.resize((820, 520), Image.Resampling.LANCZOS)
        im1.paste(bg_logo, ((SCREEN_W - 820) // 2, 540), bg_logo)
        
    d1.text((SCREEN_W // 2 - 320, 1160), "Controla tus gastos diarios y personales", font=font_regular, fill=(100, 116, 139))
    
    # Botones sociales simulados
    btn_y = 1380
    # Botón Google central destacado
    d1.ellipse([(SCREEN_W // 2 - 60, btn_y), (SCREEN_W // 2 + 60, btn_y + 120)], fill=(66, 133, 244))
    d1.text((SCREEN_W // 2 - 18, btn_y + 35), "G", font=font_mid, fill=(255, 255, 255))
    
    # Botón Demo / Revisor destacado para evaluación
    demo_btn_box = [(SCREEN_W // 2 - 380, btn_y + 240), (SCREEN_W // 2 + 380, btn_y + 360)]
    d1.rounded_rectangle(demo_btn_box, radius=60, fill=(241, 245, 249), outline=COLOR_PRIMARY, width=4)
    d1.text((SCREEN_W // 2 - 310, btn_y + 278), "✓ Acceso Revisor de Tienda (Demo)", font=font_mid, fill=COLOR_PRIMARY)
    d1.text((SCREEN_W // 2 - 270, btn_y + 400), "demo@comogasto.com  •  PIN: 123456", font=font_small, fill=(100, 116, 139))
    
    # Aviso legal inferior
    d1.text((SCREEN_W // 2 - 320, 2400), "Términos del Servicio y Política de Privacidad", font=font_small, fill=(148, 163, 184))
    
    path1 = os.path.join(OUTPUT_DIR, "01_login.png")
    im1.save(path1, "PNG", optimize=True)
    print(f"✓ Captura 01 generada: {path1}")
    
    # ── 02_inicio.png (Inicio con Gráfico de Barras) ──────────────────────────
    im2, d2, _, card_col, text_col = crear_base_pantalla("Cómo Gasto", tiene_appbar=False)
    
    # Slider de Meses superior
    d2.rectangle([(0, 0), (SCREEN_W, 200)], fill=(103, 58, 183))
    d2.text((80, 70), "← Septiembre", font=font_regular, fill=(209, 196, 233))
    d2.text((SCREEN_W // 2 - 100, 60), "OCTUBRE", font=font_big, fill=(255, 255, 255))
    d2.text((SCREEN_W - 360, 70), "Noviembre →", font=font_regular, fill=(209, 196, 233))
    
    # Total acumulado card
    d2.rounded_rectangle([(70, 240), (SCREEN_W - 70, 480)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d2.text((120, 280), "Gasto Total del Mes", font=font_regular, fill=(100, 116, 139))
    d2.text((120, 340), "$ 498.50", font=get_font(FONT_BOLD_PATHS, 78), fill=(103, 58, 183))
    
    # Gráfico de barras temporales del mes
    d2.rounded_rectangle([(70, 520), (SCREEN_W - 70, 1140)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d2.text((120, 560), "Tendencia Diaria (Gráfico de Barras)", font=font_mid, fill=(30, 41, 59))
    
    # Dibujar barras simuladas
    bar_data = [20, 85, 30, 18, 45, 10, 34, 15, 60, 110, 25, 45, 15, 30, 25, 40, 50, 28, 20, 35, 92, 10, 15, 15, 30, 20, 50, 10, 20, 15, 10]
    bar_w = 30
    bar_gap = 9
    start_x = 110
    base_y = 1060
    max_h = 420
    max_val = 110
    
    for i, v in enumerate(bar_data):
        bx = start_x + i * (bar_w + bar_gap)
        bh = int((v / max_val) * max_h)
        col = COLOR_PRIMARY if v < 70 else (103, 58, 183)
        d2.rounded_rectangle([bx, base_y - bh, bx + bar_w, base_y], radius=6, fill=col)
        
    # Desglose de Categorías en lista
    d2.text((80, 1200), "Desglose por Categoría", font=font_mid, fill=(15, 23, 42))
    
    categories = [
        ("Supermercado", "$ 177.80", COLOR_CHART_1, "12 gastos"),
        ("Servicios", "$ 160.00", COLOR_CHART_3, "4 servicios"),
        ("Comida y Restaurantes", "$ 62.70", COLOR_CHART_2, "8 comidas"),
        ("Salud y Medicamentos", "$ 45.00", COLOR_CHART_4, "2 compras"),
        ("Transporte", "$ 33.00", COLOR_PRIMARY, "6 viajes"),
        ("Entretenimiento", "$ 25.00", COLOR_CHART_5, "3 eventos"),
    ]
    
    cy = 1280
    for name, val, col, count in categories:
        d2.rounded_rectangle([(70, cy), (SCREEN_W - 70, cy + 130)], radius=20, fill=(255, 255, 255), outline=(241, 245, 249), width=2)
        d2.ellipse([(110, cy + 30), (180, cy + 100)], fill=col)
        d2.text((220, cy + 30), name, font=font_mid, fill=(30, 41, 59))
        d2.text((220, cy + 80), count, font=font_small, fill=(148, 163, 184))
        d2.text((SCREEN_W - 320, cy + 42), val, font=font_mid, fill=(15, 23, 42))
        cy += 150
        
    # Barra de navegación inferior con FAB central
    d2.rectangle([(0, SCREEN_H - 180), (SCREEN_W, SCREEN_H)], fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d2.ellipse([(SCREEN_W // 2 - 75, SCREEN_H - 250), (SCREEN_W // 2 + 75, SCREEN_H - 100)], fill=(103, 58, 183))
    d2.text((SCREEN_W // 2 - 22, SCREEN_H - 220), "+", font=get_font(FONT_BOLD_PATHS, 80), fill=(255, 255, 255))
    
    path2 = os.path.join(OUTPUT_DIR, "02_inicio.png")
    im2.save(path2, "PNG", optimize=True)
    print(f"✓ Captura 02 generada: {path2}")
    
    # ── 03_graficos.png (Gráfico Circular / Torta) ───────────────────────────
    im3, d3, _, _, _ = crear_base_pantalla("Distribución de Gastos", tiene_appbar=False)
    
    # Header mensual
    d3.rectangle([(0, 0), (SCREEN_W, 200)], fill=(103, 58, 183))
    d3.text((SCREEN_W // 2 - 190, 60), "OCTUBRE 2026", font=font_big, fill=(255, 255, 255))
    
    # Card gráfico circular
    d3.rounded_rectangle([(70, 240), (SCREEN_W - 70, 1160)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d3.text((120, 280), "Distribución Porcentual (Gráfico de Torta)", font=font_mid, fill=(30, 41, 59))
    
    # Dibujar torta circular simulada
    pie_center = (SCREEN_W // 2, 700)
    pie_r = 300
    pie_box = [pie_center[0] - pie_r, pie_center[1] - pie_r, pie_center[0] + pie_r, pie_center[1] + pie_r]
    
    # Sectores circulares
    d3.pieslice(pie_box, 0, 130, fill=COLOR_CHART_1)      # Supermercado 36%
    d3.pieslice(pie_box, 130, 245, fill=COLOR_CHART_3)    # Servicios 32%
    d3.pieslice(pie_box, 245, 290, fill=COLOR_CHART_2)    # Comida 13%
    d3.pieslice(pie_box, 290, 325, fill=COLOR_CHART_4)    # Salud 9%
    d3.pieslice(pie_box, 325, 350, fill=COLOR_PRIMARY)    # Transporte 7%
    d3.pieslice(pie_box, 350, 360, fill=COLOR_CHART_5)    # Entretenimiento 5%
    
    # Agujero interior (Donut chart estilizado)
    donut_r = 140
    d3.ellipse([pie_center[0] - donut_r, pie_center[1] - donut_r, pie_center[0] + donut_r, pie_center[1] + donut_r], fill=(255, 255, 255))
    d3.text((pie_center[0] - 80, pie_center[1] - 40), "$ 498", font=font_big, fill=(103, 58, 183))
    d3.text((pie_center[0] - 50, pie_center[1] + 30), "Total", font=font_regular, fill=(100, 116, 139))
    
    # Leyenda cromática
    d3.text((80, 1220), "Resumen Estadístico", font=font_mid, fill=(15, 23, 42))
    leyenda = [
        ("Supermercado (36%)", "$ 177.80", COLOR_CHART_1),
        ("Servicios Públicos (32%)", "$ 160.00", COLOR_CHART_3),
        ("Comida y Salidas (13%)", "$ 62.70", COLOR_CHART_2),
        ("Salud y Farmacia (9%)", "$ 45.00", COLOR_CHART_4),
        ("Transporte Urbano (7%)", "$ 33.00", COLOR_PRIMARY),
        ("Entretenimiento (5%)", "$ 25.00", COLOR_CHART_5),
    ]
    ly = 1300
    for label, monto, color in leyenda:
        d3.rounded_rectangle([(70, ly), (SCREEN_W - 70, ly + 130)], radius=18, fill=(255, 255, 255), outline=(241, 245, 249), width=2)
        d3.ellipse([(110, ly + 40), (160, ly + 90)], fill=color)
        d3.text((190, ly + 42), label, font=font_mid, fill=(30, 41, 59))
        d3.text((SCREEN_W - 300, ly + 42), monto, font=font_mid, fill=(15, 23, 42))
        ly += 150
        
    # Barra de navegación inferior
    d3.rectangle([(0, SCREEN_H - 180), (SCREEN_W, SCREEN_H)], fill=(255, 255, 255), outline=(226, 232, 240), width=1)
    d3.ellipse([(SCREEN_W // 2 - 75, SCREEN_H - 250), (SCREEN_W // 2 + 75, SCREEN_H - 100)], fill=(103, 58, 183))
    d3.text((SCREEN_W // 2 - 22, SCREEN_H - 220), "+", font=get_font(FONT_BOLD_PATHS, 80), fill=(255, 255, 255))
    
    path3 = os.path.join(OUTPUT_DIR, "03_graficos.png")
    im3.save(path3, "PNG", optimize=True)
    print(f"✓ Captura 03 generada: {path3}")
    
    # ── 04_agregar.png (Registrar Gasto) ──────────────────────────────────────
    im4, d4, _, _, _ = crear_base_pantalla("Registrar Nuevo Gasto", tiene_appbar=True)
    
    # Campo de Monto grande
    d4.rounded_rectangle([(70, 200), (SCREEN_W - 70, 480)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d4.text((120, 240), "Monto a registrar", font=font_regular, fill=(100, 116, 139))
    d4.text((120, 310), "$ 85.50", font=get_font(FONT_BOLD_PATHS, 96), fill=(103, 58, 183))
    
    # Selector de categorías chips
    d4.text((80, 520), "Selecciona Categoría", font=font_mid, fill=(15, 23, 42))
    chips = ["Supermercado", "Transporte", "Comida", "Servicios", "Salud", "Ocio"]
    chip_x, chip_y = 70, 590
    for idx, c in enumerate(chips):
        selected = idx == 0
        w = 380
        box = [chip_x, chip_y, chip_x + w, chip_y + 100]
        fill_col = (103, 58, 183) if selected else (255, 255, 255)
        text_c = (255, 255, 255) if selected else (71, 85, 105)
        d4.rounded_rectangle(box, radius=50, fill=fill_col, outline=(103, 58, 183) if selected else (203, 213, 225), width=2)
        d4.text((chip_x + 60, chip_y + 26), c, font=font_regular, fill=text_c)
        chip_x += w + 25
        if chip_x > SCREEN_W - 400:
            chip_x = 70
            chip_y += 125
            
    # Fecha y adjunto de comprobante
    d4.rounded_rectangle([(70, 870), (SCREEN_W - 70, 1040)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d4.text((120, 910), "Fecha: Hoy, 11 de Octubre", font=font_mid, fill=(30, 41, 59))
    d4.text((120, 970), "📷 Foto de comprobante adjunta (ticket_compra.jpg)", font=font_small, fill=COLOR_PRIMARY)
    
    # Teclado numérico táctil optimizado
    key_y = 1100
    keys = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        [".", "0", "⌫"]
    ]
    kw = 370
    kh = 160
    gap = 20
    
    for row in keys:
        kx = 85
        for k in row:
            d4.rounded_rectangle([(kx, key_y), (kx + kw, key_y + kh)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
            d4.text((kx + kw // 2 - 20, key_y + 40), k, font=font_big, fill=(15, 23, 42))
            kx += kw + gap
        key_y += kh + gap
        
    # Botón Guardar Gasto
    d4.rounded_rectangle([(70, SCREEN_H - 240), (SCREEN_W - 70, SCREEN_H - 80)], radius=36, fill=(103, 58, 183))
    d4.text((SCREEN_W // 2 - 170, SCREEN_H - 185), "GUARDAR GASTO", font=font_mid, fill=(255, 255, 255))
    
    path4 = os.path.join(OUTPUT_DIR, "04_agregar.png")
    im4.save(path4, "PNG", optimize=True)
    print(f"✓ Captura 04 generada: {path4}")
    
    # ── 05_detalle.png (Detalle de Categoría) ─────────────────────────────────
    im5, d5, _, _, _ = crear_base_pantalla("Detalle: Supermercado", tiene_appbar=True)
    
    # Card Resumen Categoría
    d5.rounded_rectangle([(70, 200), (SCREEN_W - 70, 480)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d5.text((120, 240), "Gasto Total en Supermercado", font=font_regular, fill=(100, 116, 139))
    d5.text((120, 310), "$ 177.80", font=get_font(FONT_BOLD_PATHS, 78), fill=(103, 58, 183))
    d5.text((120, 410), "36% del presupuesto del mes • 4 registros", font=font_small, fill=(71, 85, 105))
    
    # Lista de transacciones en la categoría
    d5.text((80, 520), "Transacciones Registradas", font=font_mid, fill=(15, 23, 42))
    
    items = [
        ("Día 21", "$ 92.30", "Supermercado Mayorista", "Con comprobante adjunto"),
        ("Día 15", "$ 45.00", "Compras de víveres semanales", "Sin comprobante"),
        ("Día 8", "$ 28.50", "Frutas y verduras frescas", "Con comprobante adjunto"),
        ("Día 2", "$ 12.00", "Panadería y lácteos", "Sin comprobante"),
    ]
    
    iy = 590
    for dia, monto, desc, comp in items:
        d5.rounded_rectangle([(70, iy), (SCREEN_W - 70, iy + 200)], radius=24, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        # Calendario badge
        d5.rounded_rectangle([(110, iy + 35), (220, iy + 165)], radius=16, fill=(241, 245, 249), outline=(203, 213, 225), width=2)
        d5.text((125, iy + 55), "📅", font=font_mid, fill=(103, 58, 183))
        d5.text((130, iy + 115), dia.replace("Día ", "D"), font=font_small, fill=(71, 85, 105))
        
        d5.text((260, iy + 45), desc, font=font_mid, fill=(15, 23, 42))
        d5.text((260, iy + 110), comp, font=font_small, fill=COLOR_PRIMARY if "Con" in comp else (148, 163, 184))
        d5.text((SCREEN_W - 320, iy + 70), monto, font=font_mid, fill=(103, 58, 183))
        iy += 230
        
    # Mensaje informativo de deslizamiento para eliminar
    d5.text((SCREEN_W // 2 - 320, SCREEN_H - 140), "💡 Desliza hacia la izquierda para eliminar un registro", font=font_small, fill=(100, 116, 139))
    
    path5 = os.path.join(OUTPUT_DIR, "05_detalle.png")
    im5.save(path5, "PNG", optimize=True)
    print(f"✓ Captura 05 generada: {path5}")
    
    # ── 06_ajustes.png (Ajustes y Modo Oscuro) ───────────────────────────────
    im6, d6, _, _, _ = crear_base_pantalla("Configuración", tiene_appbar=True, modo_oscuro=True)
    
    # Opciones de configuración
    sy = 240
    # Modo Oscuro
    d6.rounded_rectangle([(70, sy), (SCREEN_W - 70, sy + 180)], radius=24, fill=(30, 30, 30), outline=(50, 50, 50), width=2)
    d6.text((130, sy + 60), "Modo Oscuro (Dark Theme)", font=font_mid, fill=(255, 255, 255))
    # Switch activado
    d6.rounded_rectangle([(SCREEN_W - 250, sy + 50), (SCREEN_W - 130, sy + 120)], radius=35, fill=(239, 68, 68))
    d6.ellipse([(SCREEN_W - 190, sy + 55), (SCREEN_W - 135, sy + 115)], fill=(255, 255, 255))
    
    # Notificaciones y recordatorios
    sy += 220
    d6.rounded_rectangle([(70, sy), (SCREEN_W - 70, sy + 180)], radius=24, fill=(30, 30, 30), outline=(50, 50, 50), width=2)
    d6.text((130, sy + 60), "Recordatorio Diario de Gastos", font=font_mid, fill=(255, 255, 255))
    d6.rounded_rectangle([(SCREEN_W - 250, sy + 50), (SCREEN_W - 130, sy + 120)], radius=35, fill=(239, 68, 68))
    d6.ellipse([(SCREEN_W - 190, sy + 55), (SCREEN_W - 135, sy + 115)], fill=(255, 255, 255))
    
    # Idioma
    sy += 220
    d6.rounded_rectangle([(70, sy), (SCREEN_W - 70, sy + 180)], radius=24, fill=(30, 30, 30), outline=(50, 50, 50), width=2)
    d6.text((130, sy + 60), "Idioma de la Aplicación", font=font_mid, fill=(255, 255, 255))
    d6.text((SCREEN_W - 280, sy + 60), "Español ›", font=font_regular, fill=(156, 163, 175))
    
    # Información de versión
    sy += 220
    d6.rounded_rectangle([(70, sy), (SCREEN_W - 70, sy + 180)], radius=24, fill=(30, 30, 30), outline=(50, 50, 50), width=2)
    d6.text((130, sy + 60), "Versión de la Aplicación", font=font_mid, fill=(255, 255, 255))
    d6.text((SCREEN_W - 260, sy + 60), "1.0.0 (1)", font=font_regular, fill=(156, 163, 175))
    
    # Botón Cerrar Sesión inferior
    d6.rounded_rectangle([(70, SCREEN_H - 240), (SCREEN_W - 70, SCREEN_H - 80)], radius=36, fill=(239, 68, 68))
    d6.text((SCREEN_W // 2 - 150, SCREEN_H - 185), "CERRAR SESIÓN", font=font_mid, fill=(255, 255, 255))
    
    path6 = os.path.join(OUTPUT_DIR, "06_ajustes.png")
    im6.save(path6, "PNG", optimize=True)
    print(f"✓ Captura 06 generada: {path6}")

if __name__ == "__main__":
    print("Iniciando generación de activos gráficos y capturas de tienda...")
    generar_icono_512()
    generar_grafico_destacado()
    generar_capturas_tienda()
    print("Todos los activos gráficos y capturas oficiales fueron generados con éxito.")
