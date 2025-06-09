import flet as ft
import consulta_mongo as interacciones
import consultas_mongo as consultas
import alta_medicamentomongo as alta  # Nombre corregido y correcto

def main(page: ft.Page):
    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True,
        bgcolor="blue"
    )

    def mostrar_interacciones(e):
        page.clean()
        interacciones.main(page)

    def mostrar_consultas(e):
        page.clean()
        consultas.main(page)

    def mostrar_alta_medicamento(e):
        page.clean()
        alta.main(page)

    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        bgcolor="orange100",
        color="black",
        width=250,
        on_click=mostrar_interacciones
    )

    btn_consultas = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("search", size=40, color="black"),
                    ft.Text("Consultas de Fármacos", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        bgcolor="green100",
        color="black",
        width=250,
        on_click=mostrar_consultas
    )

    btn_alta = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add_circle", size=40, color="black"),
                    ft.Text("Alta Medicamento", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        bgcolor="blue100",
        color="black",
        width=250,
        on_click=mostrar_alta_medicamento
    )

    page.add(
        ft.Column(
            controls=[
                ft.Divider(color="black"),
                btn_interacciones,
                btn_consultas,
                btn_alta
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
