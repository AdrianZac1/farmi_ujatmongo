import flet as ft
import conexion_mongodb as cm  # Cambiado el nombre del archivo correctamente

def main(page: ft.Page):
    page.title = "Interacciones de Fármacos"
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title=ft.Text("Recetas UJAT"),
        leading=ft.Icon("dashboard"),
        bgcolor="blue"
    )

    # Columnas de la tabla
    encabezado = [
        ft.DataColumn(ft.Text("Fármaco")),
        ft.DataColumn(ft.Text("Interacciones"))
    ]

    # Obtener las colecciones desde el módulo de conexión
    farmaco, _ = cm.get_collections()  # Solo usamos farmaco en esta vista

    # Consulta MongoDB y arma las filas
    filas = []
    datos = farmaco.find()  # Consulta todos los documentos de farmaco
    for d in datos:
        nombre = d.get("nombre", "Sin nombre")
        interacciones = d.get("interacciones", "Sin datos")
        fila = ft.DataRow([
            ft.DataCell(ft.Text(nombre)),
            ft.DataCell(ft.Text(interacciones))
        ])
        filas.append(fila)

    # Tabla con los datos
    tbl_farmacos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )

    page.add(tbl_farmacos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
