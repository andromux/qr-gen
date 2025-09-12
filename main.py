import flet as ft
import qrcode
import os
from datetime import datetime

# 🎨 Paleta inspirada en Instagram
class ColoresApp:
    # Gradiente principal (Instagram style)
    GRADIENTE = ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors=["#F58529", "#DD2A7B", "#8134AF", "#515BD4"],
    )

    # Colores sólidos complementarios
    PRIMARIO = "#DD2A7B"   # Rosa Instagram
    SECUNDARIO = "#8134AF" # Morado Instagram
    FONDO_CLARO = "#FFFFFF"
    FONDO_OSCURO = "#121212"
    TEXTO_CLARO = "#000000"
    TEXTO_OSCURO = "#FFFFFF"

def crear_tema():
    """Devuelve tema claro y oscuro personalizados"""
    tema_claro = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ColoresApp.PRIMARIO,
            on_primary=ColoresApp.TEXTO_OSCURO,
            secondary=ColoresApp.SECUNDARIO,
            on_secondary=ColoresApp.TEXTO_OSCURO,
            surface=ColoresApp.FONDO_CLARO,
            on_surface=ColoresApp.TEXTO_CLARO,
            background=ColoresApp.FONDO_CLARO,
            on_background=ColoresApp.TEXTO_CLARO,
            error=ft.Colors.RED,
            on_error=ft.Colors.WHITE,
        ),
        use_material3=True,
    )

    tema_oscuro = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ColoresApp.PRIMARIO,
            on_primary=ColoresApp.TEXTO_OSCURO,
            secondary=ColoresApp.SECUNDARIO,
            on_secondary=ColoresApp.TEXTO_OSCURO,
            surface=ColoresApp.FONDO_OSCURO,
            on_surface=ColoresApp.TEXTO_OSCURO,
            background=ColoresApp.FONDO_OSCURO,
            on_background=ColoresApp.TEXTO_OSCURO,
            error=ft.Colors.RED_300,
            on_error=ft.Colors.BLACK,
        ),
        use_material3=True,
    )

    return tema_claro, tema_oscuro

def main(page: ft.Page):
    page.title = "Generador de Códigos QR"
    page.window.width = 700
    page.window.height = 800
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Configuración de temas
    tema_claro, tema_oscuro = crear_tema()
    page.theme = tema_claro
    page.dark_theme = tema_oscuro
    page.theme_mode = ft.ThemeMode.SYSTEM

    # --- UI ---
    preview_image = ft.Image(width=250, height=250, fit=ft.ImageFit.CONTAIN, visible=False)

    def mostrar_notificacion(mensaje, es_error=False):
        snack_bar = ft.SnackBar(
            content=ft.Text(mensaje, color="white"),
            bgcolor="#DD2A7B" if not es_error else ft.Colors.RED,
            duration=3000,
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def generar_qr_gui(texto, nombre_archivo, carpeta_destino):
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(texto)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            if not nombre_archivo:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                nombre_archivo = f"qr_{timestamp}.png"
            elif not nombre_archivo.endswith(".png"):
                nombre_archivo += ".png"
            ruta_completa = os.path.join(carpeta_destino, nombre_archivo)
            img.save(ruta_completa)
            return True, ruta_completa
        except Exception as e:
            return False, str(e)

    def mostrar_preview(ruta_archivo):
        preview_image.src = ruta_archivo
        preview_image.visible = True
        preview_container.visible = True
        page.update()

    texto_input = ft.TextField(
        label="Texto o URL para el QR",
        hint_text="Ingresa texto, URL o datos",
        multiline=True,
        max_lines=4,
        width=600,
        expand=True,
    )

    nombre_archivo_input = ft.TextField(
        label="Nombre del archivo (opcional)",
        hint_text="Ej: mi_codigo.png",
        width=400,
        expand=True,
    )

    carpeta_destino = ft.TextField(
        label="Carpeta de destino",
        value=os.getcwd(),
        width=450,
        read_only=True,
        expand=True,
    )

    # --- FilePicker corregido ---
    def seleccionar_carpeta(e: ft.FilePickerResultEvent):
        if e.path:
            carpeta_destino.value = e.path
        else:
            carpeta_destino.value = carpeta_destino.value or os.getcwd()
        page.update()

    pick_folder_dialog = ft.FilePicker(on_result=seleccionar_carpeta)
    page.overlay.append(pick_folder_dialog)
    page.update()

    btn_carpeta = ft.ElevatedButton(
        "Seleccionar Carpeta",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: pick_folder_dialog.get_directory_path(),
        style=ft.ButtonStyle(
            color="white",
            bgcolor=ColoresApp.SECUNDARIO,
            overlay_color="#F58529"
        )
    )

    btn_cargar_archivo = ft.ElevatedButton(
        "Cargar archivo (demo)",
        icon=ft.Icons.UPLOAD_FILE,
        on_click=lambda _: mostrar_notificacion("📂 Función aún no implementada"),
        style=ft.ButtonStyle(color="white", bgcolor="#F58529")
    )

    def generar_qr_click(e):
        if not texto_input.value.strip():
            mostrar_notificacion("❌ El texto no puede estar vacío", True)
            return
        btn_generar.disabled, btn_generar.text = True, "Generando..."
        page.update()
        try:
            exito, resultado = generar_qr_gui(
                texto_input.value.strip(),
                nombre_archivo_input.value.strip(),
                carpeta_destino.value,
            )
            if exito:
                mostrar_notificacion(f"✅ QR generado: {os.path.basename(resultado)}")
                mostrar_preview(resultado)
            else:
                mostrar_notificacion(f"❌ Error: {resultado}", True)
        finally:
            btn_generar.disabled, btn_generar.text = False, "Generar Código QR"
            page.update()

    btn_generar = ft.ElevatedButton(
        "Generar Código QR",
        icon=ft.Icons.QR_CODE,
        on_click=generar_qr_click,
        style=ft.ButtonStyle(color="white", bgcolor=ColoresApp.PRIMARIO)
    )

    btn_limpiar = ft.ElevatedButton(
        "Limpiar",
        icon=ft.Icons.CLEAR,
        on_click=lambda e: (
            setattr(texto_input, "value", ""),
            setattr(nombre_archivo_input, "value", ""),
            setattr(preview_image, "visible", False),
            setattr(preview_container, "visible", False),
            page.update()
        ),
        style=ft.ButtonStyle(color="white", bgcolor="#515BD4")
    )

    preview_container = ft.Container(
        content=ft.Column([
            ft.Text("Vista previa del código QR:", size=16, weight=ft.FontWeight.BOLD),
            preview_image,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        visible=False,
        padding=20,
        margin=ft.margin.only(top=20),
        border_radius=15,
        bgcolor=ft.Colors.with_opacity(0.05, "black"),
    )

    # Layout con encabezado gradiente
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.QR_CODE, size=40, color="white"),
                    ft.Text("Generador de Códigos QR", size=26, weight=ft.FontWeight.BOLD, color="white"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                padding=20,
                border_radius=15,
                gradient=ColoresApp.GRADIENTE,
                margin=ft.margin.only(bottom=30),
            ),
            texto_input,
            ft.Container(content=btn_cargar_archivo, margin=ft.margin.only(bottom=20), alignment=ft.alignment.center),
            ft.Container(
                content=ft.Column([
                    ft.Text("Configuración de archivo:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Row([nombre_archivo_input], expand=True),
                    ft.Row([carpeta_destino, btn_carpeta], expand=True),
                ]),
                padding=20,
                margin=ft.margin.only(bottom=20),
                border_radius=15,
                bgcolor=ft.Colors.with_opacity(0.05, "black"),
            ),
            ft.Row([btn_generar, btn_limpiar], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            preview_container,
        ])
    )

if __name__ == "__main__":
    ft.app(target=main)
