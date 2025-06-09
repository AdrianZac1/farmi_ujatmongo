import flet as ft
from conexion_mongodb import get_collections  # Ahora usamos MongoDB Atlas

# Obtener la colección farmaco desde MongoDB
farmaco_col, _ = get_collections()

def obtener_farmacos(nombre=""):
    """Consulta los fármacos en MongoDB filtrando por nombre."""
    if nombre:
        query = {"nombre": {"$regex": nombre, "$options": "i"}}
    else:
        query = {}
    return list(farmaco_col.find(query))

def main(page: ft.Page):
    page.title = "Consulta de Fármacos"
    page.bgcolor = ft.Colors.WHITE

    search_box = ft.TextField(
        label="Ingrese el nombre del fármaco",
        color=ft.Colors.BLACK,
        on_change=lambda e: buscar_farmaco(e, data_table)
    )

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre", weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)),
            ft.DataColumn(ft.Text("Descripción", color=ft.Colors.BLACK)),
            ft.DataColumn(ft.Text("Categoría", color=ft.Colors.BLACK)),
            ft.DataColumn(ft.Text("Interacciones", color=ft.Colors.PINK)),
        ],
        rows=[],
    )

    def crear_celda(texto):
        return ft.DataCell(
            ft.Container(
                ft.Text(texto or "—", color=ft.Colors.BLACK, size=12),
                height=80,
                alignment=ft.alignment.center_left,
                padding=ft.padding.all(0)
            )
        )

    def buscar_farmaco(e, table):
        query = e.control.value.strip()
        table.rows.clear()
        resultados = obtener_farmacos(query)

        for farmaco in resultados:
            table.rows.append(ft.DataRow(cells=[
                crear_celda(farmaco.get("nombre")),
                crear_celda(farmaco.get("descripcion")),
                crear_celda(farmaco.get("categoria")),
                crear_celda(farmaco.get("interacciones")),
            ]))

        page.update()

    page.add(search_box, data_table)

if __name__ == "__main__":
    ft.app(target=main)
