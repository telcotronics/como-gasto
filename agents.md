# agents.md — Punto de Entrada del Proyecto

> **Reglas:**
> - Este archivo es el eslabón más importante. Leerlo siempre antes de cualquier tarea.
> - Cada cambio significativo debe reflejarse en este archivo y en los demás archivos del índice.
> - Debe ser técnico, claro y detallado para que cualquier humano, agente o IA lo entienda sin explicaciones previas.
> - **Cuando se diga "actualizar proyecto":** verificar estado de Git, actualizar `agents.md`, `README.md` y `.agente/proyecto_estructura.md` con el árbol de archivos actual.

---

## 1. Estado Vigente — 11 de Octubre de 2026

Aplicación móvil **Cómo Gasto** (`como_gasto` / `ar.com.p39.como_gasto`), auditada y preparada con su paquete completo de publicación oficial para **Google Play Store** y **Apple App Store**. 

Se ha implementado una arquitectura anti-rechazo con cuenta demo local desacoplada de la red:
- **Usuario Demo:** `demo@comogasto.com`
- **PIN Demo:** `123456`
- **Persistencia y datos locales:** Repositorio en memoria con transacciones precargadas para que el revisor humano de la tienda aprecie de inmediato los gráficos de barras, gráficos de torta y balances sin depender de Firebase ni conexión a internet.
- **Activos de tienda:** Ficha técnica oficial (`ficha_tienda.md`), política de privacidad responsive (`politica_privacidad.html`), ícono 512×512 PNG sin transparencias, gráfico destacado 1024×500 PNG y set ordenado de 6 capturas de teléfono en relación 2:1 (`1344×2688`) con recorte simétrico.

---

## 2. Antecedentes
Aplicación Flutter para el registro y control ágil de gastos personales por rubros y meses. Originalmente desarrollada con Firebase Firestore, evolucionó para incorporar modo fuera de línea para evaluación de tiendas y estándares visuales modernos con Modo Oscuro (Dark Theme).

---

## 3. Objetivo General
Brindar a los usuarios una herramienta financiera ágil para registrar compras diarias, auditar comprobantes fotográficos y comprender la distribución porcentual de su presupuesto mensual mediante representaciones gráficas interactivas.

---

## 4. Stack Técnico

| Componente | Tecnología |
|---|---|
| **Lenguaje / Framework** | Dart / Flutter |
| **Identificador Android (applicationId)** | `ar.com.p39.como_gasto` |
| **Identificador iOS (Bundle ID)** | `ar.com.p39.comoGasto` |
| **Versión Inicial de Release** | `1.0.0+1` (VersionCode `1`) |
| **Gestión de Estado** | `Provider` (`ThemeState`, `LoginState`, `ProxyProvider`) |
| **Inyección de Dependencias** | `GetIt` (`lib/di.dart`) |
| **Persistencia Primaria** | Cloud Firestore / Local In-Memory Demo (`ExpensesRepository`) |
| **Almacenamiento de Recibos** | Firebase Storage / Galería local (`image_picker`) |
| **Notificaciones** | `flutter_local_notifications` (100% en el dispositivo) |
| **Modo Oscuro** | Soportado mediante `ThemeState` con `ThemeData.dark()` |
| **Internacionalización** | Soporte bilingüe en español (`lang/es.yml`) e inglés (`lang/en.yml`) |

---

## 5. Módulos del Sistema

1. **Autenticación y Modo Revisor Demo:**
   - Soporte para Google Sign-In mediante Firebase Auth.
   - Acceso inmediato para el evaluador de tienda mediante botón y diálogo modal preconfigurado con `demo@comogasto.com` y clave `123456`.
2. **Tablero Principal (Home):**
   - Selector deslizante horizontal de meses (`MonthSelectorSlider`).
   - Total acumulado mensual en tiempo real.
   - Alternador gráfico: Gráfico de barras temporales vs. Gráfico circular de torta (`GraphWidget`).
   - Desglose ordenado por categorías con conteo de transacciones.
3. **Registro de Gastos (Add Expense):**
   - Teclado numérico táctil optimizado para entrada de montos sin teclado del sistema.
   - Selector interactivo de categorías por chips (Supermercado, Comida, Transporte, Servicios, Salud, Ocio).
   - Selector de fecha y adjunto fotográfico de ticket físico.
4. **Detalle de Categoría (Details Page):**
   - Lista detallada de compras por día.
   - Vista preliminar del comprobante adjunto.
   - Acción de deslizar para eliminar (`Dismissible`) con confirmación reactiva.
5. **Configuración y Personalización:**
   - Conmutador reactivo de Modo Oscuro.
   - Gestión de recordatorios diarios locales.
   - Cierre seguro de sesión con limpieza de preferencias.

---

## 6. Infraestructura y MCP Telcotronics

> ⚠️ La infraestructura es compartida por todo el ecosistema Telcotronics.
> La fuente de verdad es el **MCP de Infraestructura Telcotronics** (SSE `http://192.168.10.160:3006/sse`, panel `:3007`).
> La copia espejo local mantenida en el proyecto es [`.agente/infraestructura.md`](.agente/infraestructura.md).
>
> 💡 **Nota sobre Sigma-robot y el Chat MCP:** **Sigma-robot** es el Gateway de comunicaciones para todo el ecosistema (para todos: usuarios, servicios, clientes, CRM, WhatsApp, etc.). Dentro de este Gateway, el **chat basado en MCP** es el componente diseñado exclusivamente para la coordinación entre **agentes de IA**. La app móvil `como_gasto` no utiliza el chat MCP.

- **Repositorio Git Oficial:** `https://github.com/telcotronics/como-gasto.git`
- **Categoría MCP:** `application` / `client-app`

---

## 7. Índice de Documentación del Proyecto

| Documento | Ubicación | Propósito |
|---|---|---|
| **Objetivos** | [`.agente/objetivos.md`](.agente/objetivos.md) | Metas cumplidas, en progreso y roadmap |
| **Ideas** | [`.agente/ideas.md`](.agente/ideas.md) | Backlog de funcionalidades futuras |
| **Errores** | [`.agente/proyecto_errores.md`](.agente/proyecto_errores.md) | Errores detectados y soluciones aplicadas |
| **Reglas** | [`.agente/reglas.md`](.agente/reglas.md) | Directivas inquebrantables del proyecto |
| **Memoria** | [`.agente/proyecto_memoria.md`](.agente/proyecto_memoria.md) | Historial de decisiones técnicas y arquitectura |
| **Estructura** | [`.agente/proyecto_estructura.md`](.agente/proyecto_estructura.md) | Árbol completo de archivos y módulos |
| **Tareas** | [`.agente/tareas.md`](.agente/tareas.md) | Tablero de control de actividades |
| **Infraestructura** | [`.agente/infraestructura.md`](.agente/infraestructura.md) | Espejo del mapa global de servidores y servicios |
| **Ficha de Tienda** | [`store_listing/ficha_tienda.md`](store_listing/ficha_tienda.md) | Textos y declaraciones oficiales para tiendas |
| **Política de Privacidad** | [`store_listing/politica_privacidad.html`](store_listing/politica_privacidad.html) | Política legal estática para Google y Apple |
