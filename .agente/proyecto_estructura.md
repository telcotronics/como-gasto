# Estructura del Proyecto — Cómo Gasto

**Aplicación:** Cómo Gasto (`como_gasto` / `app-gastos`)  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Árbol de Directorios Principal

```text
app-gastos/
├── .agente/                              # Sistema de documentación y directivas para IA / MCP
│   ├── infraestructura.md               # Espejo idéntico del mapa global de infraestructura Telcotronics
│   ├── objetivos.md                     # Objetivos del proyecto a corto, mediano y largo plazo
│   ├── ideas.md                         # Banco de ideas y backlog de mejoras funcionales
│   ├── proyecto_errores.md              # Bitácora de errores conocidos y soluciones aplicadas
│   ├── reglas.md                        # Directivas obligatorias y reglas operacionales
│   ├── proyecto_memoria.md              # Memoria histórica de decisiones técnicas
│   ├── proyecto_estructura.md           # Estructura y catálogo de módulos (este documento)
│   └── tareas.md                        # Tablero de tareas completadas y pendientes
├── android/                             # Configuración nativa para plataforma Android
│   ├── app/
│   │   ├── build.gradle                 # Configuración de compilación (applicationId, SDKs, firmas)
│   │   └── src/main/
│   │       ├── AndroidManifest.xml      # Permisos y actividades de Android
│   │       └── kotlin/ar/com/p39/como_gasto/
│   │           └── MainActivity.kt      # Actividad principal de entrada en Android
├── ios/                                 # Configuración nativa para plataforma iOS
│   ├── Runner/
│   │   └── Info.plist                   # Metadatos, permisos de cámara/galería y bundle ID
│   └── Runner.xcodeproj/               # Proyecto Xcode
├── assets/                              # Recursos gráficos y fuentes de la aplicación
│   ├── ComoGastoIcons.ttf               # Fuente de íconos personalizados
│   ├── launcher_icon_base.png           # Ícono base del launcher
│   ├── launcher_icon_ios.png            # Ícono cuadrado oficial
│   ├── login_background.flr             # Animación Flare para pantalla de inicio
│   ├── login_background.png             # Ilustración estática de bienvenida
│   └── no_data.png                      # Gráfico para estado vacío
├── lang/                                # Archivos de traducción y localización
│   ├── en.yml                           # Textos en inglés
│   └── es.yml                           # Textos en español
├── lib/                                 # Código fuente Dart de la aplicación
│   ├── main.dart                        # Punto de entrada de la aplicación y configuración de Providers
│   ├── di.dart                          # Inyección de dependencias con GetIt
│   ├── expenses_repository.dart         # Repositorio de datos (Cloud Firestore y Mock Demo Local)
│   ├── utils.dart                       # Funciones utilitarias (cálculo de días del mes, etc.)
│   ├── como_gasto_icons.dart            # Mapeo de íconos vectoriales
│   ├── como_gasto_localizations.dart    # Soporte para internacionalización (i18n)
│   ├── auth_providers/                  # Proveedores de autenticación
│   │   ├── auth_provider.dart           # Fábrica e interfaces de autenticación
│   │   └── google_auth_provider.dart    # Implementación con Google Sign-In
│   ├── states/                          # Controladores de estado (ChangeNotifiers)
│   │   ├── login_state.dart             # Estado de sesión (soporta Google y Modo Demo Revisor)
│   │   └── theme_state.dart             # Estado de tema visual (Modo Claro / Modo Oscuro)
│   ├── pages/                           # Pantallas y vistas de usuario
│   │   ├── login_page.dart              # Pantalla de inicio de sesión con botón de acceso demo
│   │   ├── home_page.dart               # Pantalla principal (meses, gráficos y categorías)
│   │   ├── add_page.dart                # Pantalla de registro de nuevo gasto con teclado numérico
│   │   ├── details_page.dart            # Vista detallada de transacciones por categoría
│   │   ├── details_page_container.dart  # Contenedor reactivo con stream de detalle
│   │   ├── settings_page.dart           # Configuración (Modo Oscuro y Cerrar Sesión)
│   │   ├── notifications/               # Gestión de notificaciones locales
│   │   └── ui/                          # Componentes reutilizables de interfaz
│   │       ├── day_expense_list_tile.dart  # Elemento individual de gasto en lista
│   │       ├── legal_notice_widget.dart    # Aviso legal en pantalla de login
│   │       ├── loading_widget.dart         # Indicador de carga
│   │       ├── month_selector_slider.dart  # Slider horizontal de selección de meses
│   │       ├── no_data_widget.dart         # Vista de pantalla sin datos
│   │       ├── social_login_widget.dart    # Botón social
│   │       └── stream_widget.dart          # Conector reactivo con QuerySnapshot
│   └── others/                          # Widgets auxiliares y visualizadores gráficos
│       ├── month_widget.dart            # Widget agrupador mensual de gastos y gráfico
│       ├── graph_widget.dart            # Gráficos de barras y torta (charts_flutter)
│       ├── category_selection_widget.dart # Selector de categorías por chip
│       └── add_page_transition.dart     # Transición animada personalizada para AddPage
├── store_listing/                       # Paquete oficial de publicación en tiendas
│   ├── ficha_tienda.md                  # Ficha técnica oficial para Google Play y App Store
│   ├── politica_privacidad.html         # Política de privacidad estática responsive
│   ├── generar_activos_graficos.py      # Script de generación de íconos, banners y capturas
│   ├── procesar_capturas.py             # Script de captura limpia ADB y recorte simétrico 2:1
│   └── graficos/                        # Carpeta de salida con todos los PNGs generados
├── test/                                # Pruebas unitarias y de widgets
├── pubspec.yaml                         # Configuración de dependencias y assets del proyecto
├── agents.md                            # Identidad y guía del agente de IA en este proyecto
└── README.md                            # Documentación principal del repositorio para humanos
```
