import flet as ft
from conexion_mongodb import get_collections

# Conectarse a la colección 'medicamento'
_, medicamento_col = get_collections()

def main(page: ft.Page):
    page.title = "Alta de Medicamentos UJAT"
    page.theme_mode = "light"
    page.window_width = 500
    page.window_height = 850
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.appbar = ft.AppBar(
        leading=ft.Icon("medical_services"),
        title=ft.Text("Alta de Medicamentos UJAT"),
        bgcolor="green",
        color="white"
    )

    # Campos del formulario
    txt_id = ft.TextField(label="ID (número entero)", width=400)
    txt_clave = ft.TextField(label="Clave", width=400)
    txt_nombre_farmaco = ft.TextField(label="Nombre del Fármaco", width=400)
    txt_descripcion = ft.TextField(label="Descripción", width=400)
    txt_presentacion = ft.TextField(label="Presentación", width=400)

    lista_clasificacion = [
        ft.dropdown.Option("Analgésico"),
        ft.dropdown.Option("Antibiótico"),
        ft.dropdown.Option("Antiinflamatorio"),
        ft.dropdown.Option("Antipirético"),
    ]
    drp_clasificacion = ft.Dropdown(
        options=lista_clasificacion, width=400, label="Clasificación"
    )

    lista_nivel_atencion = [
        ft.dropdown.Option("1er Nivel"),
        ft.dropdown.Option("2do Nivel"),
        ft.dropdown.Option("3er Nivel"),
        ft.dropdown.Option("2do y 3er Nivel"),
    ]
    drp_nivel_atencion = ft.Dropdown(
        options=lista_nivel_atencion, width=400, label="Nivel de Atención"
    )

    mensaje = ft.Text("", color="green")

    def guardar_medicamento(e):
        campos = [
            txt_id.value, txt_clave.value, txt_nombre_farmaco.value,
            txt_descripcion.value, txt_presentacion.value,
            drp_clasificacion.value, drp_nivel_atencion.value
        ]
        if any(c is None or c.strip() == "" for c in campos):
            mensaje.value = "⚠️ Todos los campos son obligatorios."
            mensaje.color = "red"
        else:
            try:
                doc = {
                    "id": int(txt_id.value),
                    "clave": txt_clave.value,
                    "nombre_farmaco": txt_nombre_farmaco.value,
                    "descripcion": txt_descripcion.value,
                    "presentacion": txt_presentacion.value,
                    "clasificacion": drp_clasificacion.value,
                    "nivel_atencion": drp_nivel_atencion.value
                }
                medicamento_col.insert_one(doc)
                mensaje.value = "✅ Medicamento guardado exitosamente."
                mensaje.color = "green"
                limpiar_campos()
            except ValueError:
                mensaje.value = "⚠️ El ID debe ser un número entero válido."
                mensaje.color = "red"
        page.update()

    def limpiar_campos():
        txt_id.value = ""
        txt_clave.value = ""
        txt_nombre_farmaco.value = ""
        txt_descripcion.value = ""
        txt_presentacion.value = ""
        drp_clasificacion.value = None
        drp_nivel_atencion.value = None

    btn_Guardar = ft.ElevatedButton(
        text="Guardar",
        bgcolor="blue",
        color="white",
        width=150,
        on_click=guardar_medicamento
    )

    btn_Cancelar = ft.ElevatedButton(
        text="Cancelar",
        bgcolor="red",
        color="white",
        width=150,
        on_click=lambda e: limpiar_campos()
    )

    page.add(
        ft.Column(
            controls=[
                txt_id,
                txt_clave,
                txt_nombre_farmaco,
                txt_descripcion,
                txt_presentacion,
                drp_clasificacion,
                drp_nivel_atencion,
                ft.Row(
                    controls=[btn_Guardar, btn_Cancelar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)