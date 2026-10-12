# Reglas del Proyecto — Cómo Gasto

**Aplicación:** Cómo Gasto (`como_gasto`)  
**Ecosistema:** Telcotronics  
**Última actualización:** 11 de Octubre de 2026  

---

## 1. Reglas Globales y de Comportamiento del Asistente

> ### 🚨 DIRECTIVAS OBLIGATORIAS E INQUEBRANTABLES
>
> 1. **Comentar siempre cada cambio en el código:** Cuando se realice una adición o modificación en el código fuente, es obligatorio incluir un comentario claro y conciso que explique la razón técnica del cambio.
> 2. **Extrema cautela con Git y control de versiones:**
>    - ❌ **PROHIBIDO** ejecutar `git reset --hard`, `git push --force`, `git checkout .` destructivo o comandos que reescriban o destruyan ramas o historial de commits.
>    - Las acciones pasadas en este entorno causaron pérdidas sensibles de trabajo. Toda acción en Git debe ser transparente, consultada y no destructiva.
> 3. **Preservación de código "muerto" o no claro:**
>    - Ante cualquier fragmento de código que parezca en desuso, confuso o sin referencia evidente, asumir que puede tener una función oculta o ser síntoma de otro componente.
>    - Preguntar siempre a pablinux *"¿qué es esto?"* y *"¿para qué sirve?"* antes de proponer cambios o eliminaciones.
> 4. **No asumir decisiones arquitecturales sin consultar:** Mantener la comunicación fluida y llevar el hilo del desarrollo paso a paso.
> 5. **Manejo de secretos y credenciales:**
>    - Jamás incluir contraseñas reales, tokens de producción ni claves privadas en commits públicos o archivos de documentación abierta.
>    - Las credenciales de demostración (`demo@comogasto.com` / `123456`) son estrictamente para evaluación y pruebas locales aisladas.
> 6. **Rol de Sigma-robot y alcance exclusivo del chat MCP:**
>    - **Sigma-robot** es el **Gateway de comunicaciones global para todo el ecosistema** (para todos: usuarios, clientes, servicios y canales como WhatsApp, CRM y web).
>    - Dentro de este Gateway, el **chat basado en MCP** es el componente diseñado y reservado **exclusivamente para agentes de IA**.
>    - La aplicación móvil Flutter **Cómo Gasto** no utiliza el chat MCP, operando de forma autónoma con su arquitectura nativa.

---

## 2. Reglas Específicas de Publicación en Tiendas

1. **Credenciales Demo Inmutables:** El acceso con `demo@comogasto.com` y PIN `123456` debe mantenerse operativo e independiente de la conectividad de red para evitar rechazos por parte de los evaluadores de Google Play y App Store.
2. **Textos de Tienda Estrictos:** Respetar los límites duros de caracteres de las consolas:
   - Nombre de la app: Máximo 30 caracteres.
   - Descripción breve: Máximo 80 caracteres.
   - Descripción completa: Máximo 4,000 caracteres.
   - Novedades (What's New): Máximo 500 caracteres.
3. **Formatos Gráficos de Tienda:**
   - Ícono de Google Play: 512×512 PNG en formato RGB, **100% opaco y sin canales alfa ni transparencias**.
   - Gráfico destacado: 1024×500 PNG/JPG en formato RGB.
   - Capturas de pantalla: Relación de aspecto 1:2 o 2:1 (ej. 1344×2688) con recorte simétrico matemático para evitar bandas negras y notificaciones de sistema.
4. **Política de Privacidad:** El archivo `store_listing/politica_privacidad.html` debe mantenerse estático, sin dependencias de CDN externas y accesible vía HTTPS.
