# Ficha Técnica Oficial de Publicación en Tienda
**Aplicación:** Cómo Gasto  
**Identificador de Paquete (Application ID - Android):** `ar.com.p39.como_gasto`  
**Bundle ID (iOS):** `ar.com.p39.comoGasto`  
**Versión Inicial:** `1.0.0` (Build `1`)  
**Plataformas Objetivo:** Google Play Store & Apple App Store  

---

## 1. Ficha Principal de la Tienda

### Nombre de la Aplicación (Máx. 30 caracteres)
> **Cómo Gasto: Control de Gastos** (29 caracteres)

*(Alternativa concisa: `Cómo Gasto` — 10 caracteres)*

### Descripción Breve (Máx. 80 caracteres)
> **Registra tus gastos diarios, analiza estadísticas y controla tu presupuesto.** (76 caracteres)

### Descripción Completa (Máx. 4000 caracteres)
```text
¿Quieres saber con precisión en qué se va tu dinero cada mes? Cómo Gasto es la herramienta ágil y visual diseñada para ayudarte a tomar el control absoluto de tus finanzas personales y hábitos de consumo diario.

Diseñada con un enfoque limpio y directo, Cómo Gasto te permite registrar cada compra en segundos, clasificarla por rubro y comprender de un vistazo tu balance financiero mediante gráficos intuitivos.

MÓDULOS Y FUNCIONALIDADES PRINCIPALES:

1. REGISTRO ÁGIL DE GASTOS DIARIOS
• Ingreso rápido con teclado numérico optimizado para registrar montos sin fricción.
• Asignación inmediata por categorías visuales: Supermercado, Comida, Transporte, Servicios, Salud, Entretenimiento y más.
• Selección de fecha flexible para asentar transacciones pasadas o del día en curso.
• Captura y adjunto de comprobantes fotográficos: guarda fotos de tus recibos físicos o facturas para un respaldo digital ordenado.

2. ANÁLISIS ESTADÍSTICO Y GRÁFICOS VISUALES
• Conmutador gráfico instantáneo: alterna entre vista de gráfico de barras temporal y diagrama de torta (gráfico circular) porcentual.
• Desglose comparativo por rubro: identifica rápidamente qué porcentaje de tu presupuesto absorbe cada categoría.
• Total acumulado mensual visible en todo momento para evitar sorpresas a fin de mes.

3. NAVEGACIÓN Y CRONOLOGÍA MENSUAL
• Selector deslizante de meses (Slider): viaja fluidamente entre el historial de meses anteriores o planifica el mes en curso.
• Vista detallada por rubro: inspecciona el desglose de cada gasto individual agrupado por categoría.
• Gestión simplificada: elimina registros deslizando el elemento con confirmación inmediata.

4. RECORDATORIOS Y NOTIFICACIONES LOCALES
• Configuración de alertas locales para recordar el registro oportuno de tus gastos diarios.
• Sistema de notificaciones 100% en el dispositivo, respetando tu concentración y privacidad.

5. PRIVACIDAD Y PERSONALIZACIÓN
• Modo Oscuro integrado (Dark Theme): cuida tu vista y optimiza la batería en sesiones nocturnas con un contraste elegante.
• Soporte multilingüe: interfaz adaptada en español e inglés según la configuración de tu sistema.
• Respaldo en la nube con Google o uso en modo local: tú decides cómo gestionar tu información.

Cómo Gasto convierte el seguimiento financiero en un hábito sencillo, accesible y transparente. Comienza a registrar tus gastos hoy y toma decisiones financieras inteligentes.
```

---

## 2. Categorización y Declaraciones Legales

### Categorización
- **Categoría principal (Google Play):** Finanzas (*Finance*)
- **Categoría secundaria (Google Play):** Productividad (*Productivity*) / Estilo de vida (*Lifestyle*)
- **Categoría principal (Apple App Store):** Finance (Finanzas)
- **Categoría secundaria (Apple App Store):** Productivity (Productividad)
- **Etiquetas sugeridas:** Finanzas personales, Control de gastos, Presupuesto, Ahorro, Contabilidad personal, Gastos diarios.

### Clasificación de Contenido (IARC / PEGI / ESRB)
- **Clasificación IARC estimada:** **Para todos / PEGI 3 / Everyone**
- **Violencia:** No contiene violencia gráfica ni textual.
- **Contenido sexual:** No.
- **Lenguaje potencialmente ofensivo:** No.
- **Sustancias controladas:** No.
- **Apuestas o juegos de azar:** No.
- **Acceso libre a Internet / Navegador abierto:** No.

### Declaración de Anuncios
- **¿La app contiene anuncios?:** **NO**
  *(La aplicación no contiene SDKs de publicidad programática de terceros como AdMob, Unity Ads o Facebook Audience Network).*

### Declaración de Seguridad de los Datos (Data Safety / Privacy Nutrition Labels)

| Campo | Declaración Google Play | Declaración App Store | Justificación |
|---|---|---|---|
| **¿La app recopila datos?** | Sí | Sí | Datos estrictamente necesarios para sincronizar los gastos del usuario si inicia sesión. |
| **¿Los datos se comparten con terceros?** | **NO** | **NO** | No se transfieren ni venden datos personales a brokers, empresas de publicidad ni agregadores de datos. |
| **Información Personal (Correo electrónico, ID de usuario)** | Recopilado (Opcional) | Data Linked to You | Autenticación de cuenta mediante Firebase Auth / Google Sign-In para vincular la base de datos de gastos. |
| **Fotos y Videos (Galería / Cámara)** | Recopilado (Opcional) | Data Not Linked to You | Exclusivamente si el usuario decide fotografiar o adjuntar un recibo de compra. |
| **Información Financiera (Montos de gastos)** | Recopilado | App Functionality | Almacenamiento de valores numéricos de gastos y categorías para generar estadísticas personales. |
| **Cifrado en tránsito** | **Sí (HTTPS / TLS 1.3)** | Cifrado en tránsito | Toda transferencia de datos con Cloud Firestore y Firebase Storage se realiza mediante canales cifrados TLS. |
| **Mecanismo de eliminación de datos** | **Sí** | Solicitud de borrado | Opción de cerrar sesión y eliminar registros directamente en la app o solicitando borrado de cuenta a soporte. |

---

## 3. Instrucciones para el Revisor de la Tienda (Acceso a la App)

> **IMPORTANTE PARA EL EVALUADOR (Google Play Console & Apple App Review):**  
> Para verificar la totalidad de los módulos de la aplicación sin depender de cuentas OAuth de Google ni factores de red externos, se ha implementado una cuenta de evaluación con credenciales fijas y datos pre-cargados.

### Credenciales de Demostración:
- **Correo Electrónico (Demo):** `demo@comogasto.com`
- **PIN / Clave de Acceso:** `123456`

### Paso a Paso para el Acceso del Revisor:
1. Abra la aplicación en el dispositivo o emulador de prueba.
2. En la pantalla de bienvenida / inicio de sesión, presione el botón situado bajo los íconos sociales: **"Acceso Revisor de Tienda (Demo)"**.
3. Aparecerá un cuadro de diálogo con el correo `demo@comogasto.com` y la clave `123456` preconfigurados.
4. Presione **"Ingresar Demo"**.
5. La aplicación iniciará sesión inmediatamente en modo fuera de línea con datos de gastos de muestra (Supermercado, Transporte, Comida, etc.).
6. Podrá explorar:
   - Gráfico de barras y gráfico circular de gastos del mes actual.
   - Navegación temporal con el deslizador de meses.
   - Detalle por categoría al pulsar cualquier rubro.
   - Eliminación de registros deslizando a la izquierda.
   - Botón central `+` para añadir un nuevo gasto de prueba.
   - Pantalla de Configuración con alternador de Modo Oscuro y botón de cierre de sesión.

---

## 4. Notas de la Versión (What's New)

### Lanzamiento Inicial — Versión 1.0.0 (Build 1)
```text
¡Te damos la bienvenida a Cómo Gasto!
• Registra tus gastos diarios fácilmente con categorías visuales.
• Gráficos dinámicos de barras y torta para analizar tu consumo por rubro.
• Selector interactivo de meses para revisar tu historial financiero.
• Adjunta fotografías de tus facturas y comprobantes.
• Modo Oscuro integrado para una experiencia visual confortable.
• Modo demo local para evaluación rápida.
```
*(Total caracteres: 425 — Límite máx. de tienda: 500 caracteres).*

---

## 5. Checklist de Publicación (Pre-lanzamiento)

### A. Configuración de Compilación y Firma (DevOps)
- [x] Identificador de aplicación Android: `ar.com.p39.como_gasto`.
- [x] Identificador de paquete iOS: `ar.com.p39.comoGasto`.
- [x] Versión inicial establecida: `1.0.0` (código de build `1`).
- [x] Soporte de Keystore de producción configurado en `android/app/build.gradle` y plantilla `android/key.properties.example` disponible.
- [ ] Certificados de Distribución y Provisioning Profiles de iOS generados en Apple Developer Portal.
- [ ] Generación de paquete Android App Bundle: `flutter build appbundle --release`.
- [ ] Generación de paquete iOS IPA: `flutter build ipa --release`.

### B. Consola de Google Play (Google Play Console)
- [ ] Ficha principal cargada: Título (29 cars), Breve (76 cars), Completa (2650 cars).
- [ ] Cuestionario de clasificación IARC completado (Clasificación: Para todos).
- [ ] Declaración de política de privacidad vinculada (`politica_privacidad.html`).
- [ ] Declaración de Anuncios: "No contiene anuncios".
- [ ] Formulario de Seguridad de los Datos (Data Safety) completado según la tabla declarada.
- [ ] Acceso a la app: Credenciales fijas ingresadas (`demo@comogasto.com` / `123456`).
- [x] Ícono de tienda (512×512 PNG sin transparencias) generado (`00_icono_512.png`).
- [x] Gráfico destacado (1024×500 PNG) generado (`grafico_destacado_1024x500.png`).
- [x] Capturas de pantalla oficiales (resolución 2:1, 6 capturas de teléfono) generadas (`01_login.png` a `06_ajustes.png`).

### C. Apple App Store Connect
- [ ] Nombre de app y subtítulo configurados.
- [ ] Texto promocional y descripción cargados.
- [ ] URL de Política de Privacidad vinculada con HTTPS.
- [ ] Cuestionario de Privacidad de la App (App Privacy Nutrition Labels) completado.
- [ ] Notas de revisión de la app (App Review Information) con credenciales demo provistas.
- [x] Ícono oficial de 1024×1024 sin canales alfa generado (`icono_1024.png`).
- [x] Capturas de pantalla para dispositivos móviles (relación 2:1 limpia) generadas.
