# Objetivos del Proyecto — Cómo Gasto

**Aplicación:** Cómo Gasto (`como_gasto` / `app-gastos`)  
**Ecosistema:** Telcotronics — Aplicaciones Móviles de Productividad y Finanzas  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Visión General
Proveer a los usuarios una aplicación móvil ágil, visualmente atractiva y confiable para el registro de gastos diarios, visualización de tendencias mensuales y resguardo de comprobantes de compra, garantizando una arquitectura que soporte operación autónoma sin conexión a internet y sincronización en la nube.

---

## 2. Objetivos Principales

### A. Preparación para Publicación en Tiendas (Google Play Store & Apple App Store)
- [x] **Identificadores y Versionado Oficial:** Validar `applicationId: ar.com.p39.como_gasto` (Android) y `CFBundleIdentifier: ar.com.p39.comoGasto` (iOS), con versión `1.0.0+1`.
- [x] **Acceso de Revisión Garantizado (Anti-Rechazo):** Implementar cuenta demo de evaluación con credenciales fijas (`demo@comogasto.com` / `123456`) y datos locales precargados de prueba que operen 100% fuera de línea sin requerir factores externos (SMS, OAuth complejo, servidores caídos ni aprobaciones manuales).
- [x] **Ficha Técnica Oficial de Tienda:** Redactar y normalizar el documento Markdown (`store_listing/ficha_tienda.md`) con textos de marketing validados (máx. 30 y 80 caracteres), cuestionario legal IARC, declaración de anuncios y tabla de Seguridad de los Datos (Data Safety).
- [x] **Política de Privacidad Estática:** Generar `store_listing/politica_privacidad.html` responsive y autocontenido conforme a GDPR, CCPA y requerimientos de Google Play y App Store.
- [x] **Activos Gráficos y Capturas Simétricas:** Generar el ícono de 512×512 PNG sin transparencias, banner destacado de 1024×500 PNG y set ordenado de 6 capturas de teléfono en relación 2:1 (1344×2688) recortadas simétricamente eliminando barras de sistema.
- [ ] **Empaque y Firma de Producción:** Configurar keystore de release y compilar el paquete Android App Bundle (`.aab`) y archivo `.ipa` de iOS.

### B. Estabilidad y Compatibilidad Técnica
- [x] **Aislamiento de Dependencias de Red:** Desacoplar el repositorio de datos (`ExpensesRepository`) para alternar fluidamente entre Cloud Firestore y streams en memoria locales cuando se opera en modo demostración.
- [ ] **Modernización del SDK de Flutter:** Migrar el proyecto de forma progresiva a Flutter 3.x / Dart 3.x con Null Safety, reemplazando dependencias legadas descontinuadas (como `flare_flutter`) por alternativas modernas (`rive` o animaciones vectoriales nativas).
- [ ] **Actualización de Embeddings de Android:** Actualizar `MainActivity.kt` al nuevo Android v2 embedding de Flutter para permitir compilación nativa directa en versiones recientes de Android Gradle Plugin.

### C. Funcionalidad de Negocio
- [x] **Registro Rápido de Gastos:** Entrada numérica optimizada para asentar gastos en menos de 5 segundos.
- [x] **Categorización Visual:** Clasificación por rubros esenciales (Supermercado, Transporte, Comida, Servicios, Salud, Entretenimiento).
- [x] **Visualización Gráfica Dual:** Conmutación fluida entre gráfico de barras cronológico y diagrama de torta porcentual.
- [x] **Soporte de Comprobantes:** Capacidad de capturar fotos de tickets físicos y recibos.
- [x] **Personalización Visual:** Modo Oscuro (Dark Theme) integrado y soporte bilingüe (español/inglés).

---

## 3. Hoja de Ruta (Roadmap)

| Fase | Hito | Estado | Prioridad |
|---|---|---|---|
| **Fase 1** | Auditoría de paquete y credenciales demo de revisión | **COMPLETADO** | Alta |
| **Fase 2** | Redacción de Ficha Técnica (`store_listing/ficha_tienda.md`) | **COMPLETADO** | Alta |
| **Fase 3** | Política de Privacidad (`store_listing/politica_privacidad.html`) | **COMPLETADO** | Alta |
| **Fase 4** | Activos gráficos (512x512, 1024x500 y capturas 1344x2688) | **COMPLETADO** | Alta |
| **Fase 5** | Infraestructura `.agente/` y documentación MCP | **COMPLETADO** | Alta |
| **Fase 6** | Compilación de release firmada (AAB / IPA) | **PENDIENTE** | Media |
| **Fase 7** | Integración opcional con API-SIGMA / Backend Telcotronics | **FUTURO** | Baja |
