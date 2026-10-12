# Banco de Ideas y Mejoras Futuras — Cómo Gasto

**Aplicación:** Cómo Gasto  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Ideas de Producto y Experiencia de Usuario

### 💡 1. Reconocimiento Óptico (OCR) de Tickets con IA Local o API Telcotronics
- **Concepto:** Al tomar una foto del recibo o factura con la cámara, procesar la imagen con OCR (ML Kit o el servicio de IA de Telcotronics) para extraer automáticamente:
  - Nombre del establecimiento o comercio.
  - Fecha de la transacción.
  - Monto total a pagar.
- **Beneficio:** Reduce drásticamente la fricción al cargar gastos de supermercado y restaurantes.

### 💡 2. Presupuestos Mensuales y Alertas Inteligentes
- **Concepto:** Permitir al usuario fijar un presupuesto mensual global o por categoría (ej. "Máximo $200 en Comida").
- **Funcionalidad:**
  - Barra de progreso visual por rubro (Verde: < 70%, Ámbar: 70-90%, Rojo: > 100%).
  - Notificación local de aviso cuando el usuario se acerque al límite presupuestado.

### 💡 3. Exportación de Reportes Financieros (PDF y Excel/CSV)
- **Concepto:** Generar un reporte mensual consolidado en formato PDF descargable con gráficos vectoriales y desglose detallado de gastos.
- **Utilidad:** Facilita la rendición de gastos para contabilidad, deducciones de impuestos personales o compartir con la familia.

### 💡 4. Soporte Multi-Moneda y Conversión de Divisas
- **Concepto:** Soporte para registrar gastos en monedas extranjeras (USD, EUR, Pesos, etc.) con conversión estimada a la moneda principal del usuario.

### 💡 5. Categorías y Subcategorías Personalizadas
- **Concepto:** Permitir crear nuevas categorías personalizadas eligiendo un color y un ícono de la librería de Material Icons o FontAwesome.

### 💡 6. Sincronización Opcional con el Ecosistema SIGMA / Telcotronics
- **Concepto:** En lugar de depender exclusivamente de Firebase Firestore, habilitar un conector REST/HTTPS hacia un microservicio del ecosistema Telcotronics (ej. API-SIGMA-CLOUD o base de datos local SQLite sincronizable) para usuarios corporativos que requieran custodia propia de sus datos financieros.

---

## 2. Ideas Técnicas y Arquitectura

### 🛠️ 1. Persistencia Offline Híbrida con SQLite / Isar / Hive
- **Concepto:** Incorporar una base de datos local embebida de alta velocidad (SQLite con `sqflite` o Hive) como almacenamiento primario (Offline-First) y sincronización asíncrona hacia la nube en segundo plano cuando haya conectividad disponible.

### 🛠️ 2. Migración Limpia a Flutter 3.x con Sound Null Safety
- **Concepto:** Actualizar las dependencias del proyecto a sus versiones modernas en `pubspec.yaml`, sustituyendo las llamadas no-null-safe por código tipado riguroso, asegurando compatibilidad con las últimas versiones de Android (API 34/35) e iOS (iOS 17/18).
