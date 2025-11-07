# Manual de Uso – Generador de Códigos QR

### 📌 Introducción

El **Generador de Códigos QR** es una aplicación moderna y sencilla que permite crear códigos QR de manera rápida y personalizada.
Gracias a su interfaz inspirada en los colores de **Instagram**, la experiencia es atractiva y amigable, tanto en modo claro como en modo oscuro.

La aplicación está disponible en versión **AppImage** para Linux, lo que significa que no requiere instalación: basta con descargarla, darle permisos de ejecución y empezar a usarla.

---

## 🚀 Características principales

* ✅ **Generación rápida de códigos QR** a partir de texto, URLs, información de contacto u otros datos.
* ✅ **Vista previa inmediata** del código QR antes de usarlo.
* ✅ **Personalización del archivo de salida**, permitiendo elegir el nombre y la carpeta de destino.
* ✅ **Compatibilidad con temas claro y oscuro**, adaptándose al sistema del usuario.
* ✅ **Interfaz moderna y minimalista** con diseño inspirado en Instagram.
* ✅ **Notificaciones visuales** (snackbars) para confirmar acciones o mostrar errores.
* ✅ **Soporte multiplataforma** gracias a Flet (Windows, Linux y macOS).
* ✅ **Versión AppImage disponible**, portable y lista para usar sin instalación.

---

## 🖥️ Requisitos

* **Linux, Windows o macOS** con soporte para Python o AppImage.
* Si deseas usar la versión en código:

  * Python 3.10+
  * Dependencias: `flet[all]==0.28.3`, `qrcode`, `pillow`

Instalación de dependencias (si usas el código fuente):

```bash
pip install flet[all]==0.28.3 qrcode pillow
```

---

## 📂 Instalación y ejecución

### 🔹 Opción 1: Usar la versión AppImage (Linux recomendado)

1. Descarga el archivo **AppImage** desde la sección de releases.
2. Dale permisos de ejecución:

   ```bash
   chmod +x QR_GEN.AppImage
   ```
3. Ejecuta con doble clic o desde la terminal:

   ```bash
   ./QR_GEN.AppImage
   ```

> 📌 Ventaja: no requiere instalación ni dependencias, totalmente portable.

---

### 🔹 Opción 2: Usar el código fuente

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias requeridas.
3. Ejecuta:

   ```bash
   python main.py
   ```

---

## 🛠️ Uso de la aplicación

1. **Ingresar el texto o URL** en el campo principal.
   Ejemplo: `https://www.andromux.org/`
2. (Opcional) **Escribir un nombre de archivo** para el QR generado.

   * Si lo dejas vacío, se asignará uno automáticamente con la fecha y hora.
   * Siempre se guarda en formato `.png`.
3. **Seleccionar la carpeta de destino** donde se guardará el QR.
4. Hacer clic en **Generar Código QR**.

   * Se mostrará una notificación de éxito.
   * El QR aparecerá en la vista previa.
5. Puedes usar el botón **Limpiar** para reiniciar los campos y generar un nuevo QR.

---

## 📷 Vista previa

Cada vez que generes un QR, se mostrará automáticamente en la sección de vista previa para que confirmes su contenido antes de usarlo.

---

## ⭐ Beneficios y ventajas

* **Productividad**: Genera múltiples QR en segundos.
* **Accesibilidad**: Diseño moderno, textos grandes y claros.
* **Portabilidad**: Versión AppImage sin instalación.
* **Seguridad**: Todo el procesamiento ocurre en tu computadora, sin necesidad de conexión a internet o andar accediento a sitios llenos de publicidad.
* **Flexibilidad**: Guarda tus códigos en cualquier carpeta con nombres personalizados.

---

## 📥 Descarga

La última versión **AppImage** está disponible en la sección de **Releases** del proyecto.
Simplemente descárgala y ejecútala, sin preocuparte por dependencias.
