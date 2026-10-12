# Memoria Histórica del Proyecto — Cómo Gasto

**Aplicación:** Cómo Gasto (`como_gasto` / `app-gastos`)  
**Ecosistema:** Telcotronics  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Origen y Contexto Histórico
- **2020:** Proyecto concebido originalmente por Ricardo Markiewicz como una aplicación Flutter móvil y web para el registro personal de gastos cotidianos, con arquitectura basada en `Provider`, inyección con `GetIt` y almacenamiento en Firebase Cloud Firestore.
- **2022 - 2025:** Mantenimiento del código base dentro del repositorio de Telcotronics (`https://github.com/telcotronics/como-gasto.git`).
- **Octubre 2026:**
  - El proyecto entra en fase de preparación DevOps integral para su publicación oficial en **Google Play Store** y **Apple App Store**.
  - Se identifica la necesidad crítica de blindar la aplicación contra rechazos de tienda por evaluaciones automatizadas y manuales.
  - Se diseña e implementa la arquitectura de cuenta demo (`demo@comogasto.com` / `123456`) desacoplada de la red con generación de datos de prueba en memoria.
  - Se normalizan los activos de tienda (ícono 512x512 opaco, gráfico 1024x500 y capturas con relación 2:1 a 1344x2688).
  - Se redacta la ficha técnica oficial (`ficha_tienda.md`) y la política de privacidad estática (`politica_privacidad.html`).

---

## 2. Decisiones de Arquitectura Tomadas

### A. Gestión de Estado y Repositorio Desacoplado
- Se mantuvo el patrón `Provider` con `ChangeNotifier` para `ThemeState` y `LoginState`, y un `ProxyProvider` para instanciar `ExpensesRepository`.
- Se introdujo el identificador de usuario `demo_reviewer` en `ProxyProvider` para conmutar transparentemente entre la base de datos de Firestore en la nube y la estructura de simulación local en memoria.
- `ExpensesRepository` implementa `_DemoQuerySnapshot` y `_DemoDocumentSnapshot` con streams broadcast para que los componentes visuales existentes (`StreamWidget`, `MonthWidget`, `MonthSelectorSlider`, `DayExpenseListTile`, `DetailsPage`) funcionen de manera idéntica sin requerir reescrituras invasivas.

### B. Modo Demo / Revisor In-App
- En `LoginPage`, se añadió un botón visible y un diálogo modal con las credenciales demo preconfiguradas. Esto permite que el evaluador humano de Apple o Google acceda a la app con 1 solo toque y explore gráficos, detalles y transacciones sin necesidad de configurar una cuenta de Google en el dispositivo.

### C. Pipeline Gráfico Matemático
- Siguiendo el estándar validado en otros proyectos de Telcotronics (como `seguridad_electronica`), se adoptó el estándar de captura con recorte matemático simétrico `(0, 152, 1344, 152 + 2688)` para eliminar las barras de estado y gestos de Android en resolución nativa de 1344×2992 (Pixel 8 Pro), generando activos limpios en relación 1:2 / 2:1 (`1344×2688`).

### D. Gateway Sigma-robot y Chat basado en MCP
- Se formalizó la distinción arquitectónica: **Sigma-robot es el Gateway de comunicaciones universal para todo el ecosistema Telcotronics** (usuarios, clientes, plataformas omnicanal y servicios).
- Dentro de dicho Gateway, el **chat basado en MCP** es el componente específico reservado exclusivamente para la comunicación e interoperabilidad entre agentes de IA. La aplicación móvil Flutter no implementa el chat MCP al ser un protocolo de agentes.
