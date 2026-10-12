# Tablero de Tareas — Cómo Gasto

**Aplicación:** Cómo Gasto (`como_gasto`)  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Tareas Completadas ✅

- [x] **Auditoría de Identificadores y Paquetes:** Inspeccionados `applicationId: ar.com.p39.como_gasto` y `CFBundleIdentifier: ar.com.p39.comoGasto`.
- [x] **Implementación de Cuenta Demo:**
  - Creadas credenciales fijas `demo@comogasto.com` y PIN `123456`.
  - Implementado `loginDemo` y persistencia en `SharedPreferences` en `lib/states/login_state.dart`.
  - Agregado botón y diálogo modal de evaluación en `lib/pages/login_page.dart`.
  - Agregado soporte en memoria para `demo_reviewer` con `_DemoQuerySnapshot` y `_DemoDocumentSnapshot` en `lib/expenses_repository.dart`.
  - Conectado `ProxyProvider` en `lib/main.dart` para evitar excepciones de `null`.
  - Documentados todos los cambios con comentarios explicativos.
- [x] **Redacción de la Ficha Técnica de Tienda:** Documento completo creado en `store_listing/ficha_tienda.md` con límites de caracteres validados y tabla de seguridad de datos.
- [x] **Política de Privacidad Estática:** Archivo responsive generado en `store_listing/politica_privacidad.html` sin librerías externas.
- [x] **Generación de Activos Gráficos Oficiales:**
  - Ícono 512×512 PNG 100% opaco generado (`00_icono_512.png`).
  - Banner destacado 1024×500 PNG generado (`grafico_destacado_1024x500.png`).
  - Set de 6 capturas de teléfono 1344×2688 (relación 2:1) generadas (`01_login.png` a `06_ajustes.png`).
- [x] **Scripts de Automatización Gráfica:** `generar_activos_graficos.py` y `procesar_capturas.py` creados y probados.
- [x] **Configuración del Espejo de Infraestructura:** Copiado el archivo canónico `/home/pablinux/Projects/infraestructura.md` hacia `.agente/infraestructura.md`.
- [x] **Ecosistema de Documentación `.agente/`:** Creados `objetivos.md`, `ideas.md`, `proyecto_errores.md`, `reglas.md`, `proyecto_memoria.md`, `proyecto_estructura.md` y `tareas.md`.

---

## 2. Tareas en Curso y Siguientes Pasos 🚀

- [ ] **Actualización del README.md:** Reemplazar el archivo legado de 19 líneas por una guía integral, visual y legible para humanos.
- [ ] **Creación del archivo `agents.md`:** Establecer la guía del agente para el proyecto de acuerdo con el estándar de Telcotronics.
- [ ] **Registro en el MCP de Infraestructura:** Registrar el servicio `como-gasto` en el MCP en vivo (`http://192.168.10.160:3006/sse`).
- [ ] **Revisión de Commits y Sincronización:** Confirmar estado limpio del árbol de trabajo con el usuario antes de cualquier push.
- [ ] **Firma y Empaque de Producción:** Configurar `key.properties` para generar el Android App Bundle (`.aab`) y build de iOS (`.ipa`).
