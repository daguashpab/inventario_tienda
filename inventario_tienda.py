"""
Inventario de Tienda
Autor: Daniel Guashpa Bonilla

dict inventario: producto -> {precio, stock, categoria}
set categorias: categorias sin repetir
list stock_bajo: productos con poco stock (generada al recorrer)
"""

STOCK_MINIMO = 5

inventario = {}
categorias = set()


def agregar_producto(nombre, precio, stock, categoria):
    """Agrega un producto al diccionario y su categoria al set."""
    nombre = nombre.strip().title()
    if nombre in inventario:
        print(f"'{nombre}' ya existe.")
        return
    try:
        precio, stock = float(precio), int(stock)
    except ValueError:
        print("Precio y stock deben ser numericos.")
        return

    categoria = categoria.strip().title()
    inventario[nombre] = {"precio": precio, "stock": stock, "categoria": categoria}
    categorias.add(categoria)
    print(f"'{nombre}' agregado.")


def mostrar_inventario():
    """Muestra todos los productos registrados."""
    if not inventario:
        print("Inventario vacio.")
        return
    for nombre, d in inventario.items():
        print(f"{nombre}: ${d['precio']:.2f} | stock {d['stock']} | {d['categoria']}")


def buscar_producto(nombre):
    """Busca un producto por nombre."""
    nombre = nombre.strip().title()
    if nombre in inventario:
        print(inventario[nombre])
    else:
        print(f"'{nombre}' no encontrado.")


def eliminar_producto(nombre):
    """Elimina un producto del inventario."""
    nombre = nombre.strip().title()
    if inventario.pop(nombre, None) is not None:
        print(f"'{nombre}' eliminado.")
    else:
        print(f"'{nombre}' no existe.")


def reporte_stock_bajo():
    """Recorre el inventario y lista productos bajo el minimo."""
    bajos = [n for n, d in inventario.items() if d["stock"] < STOCK_MINIMO]
    print(bajos if bajos else "Sin productos con stock bajo.")


def menu():
    print("\n1)Agregar 2)Mostrar 3)Buscar 4)Eliminar 5)Categorias 6)Stock bajo 7)Salir")


def main():
    op = ""
    while op != "7":
        menu()
        op = input("Opcion: ").strip()
        if op == "1":
            agregar_producto(input("Nombre: "), input("Precio: "),
                              input("Stock: "), input("Categoria: "))
        elif op == "2":
            mostrar_inventario()
        elif op == "3":
            buscar_producto(input("Nombre: "))
        elif op == "4":
            eliminar_producto(input("Nombre: "))
        elif op == "5":
            print(categorias if categorias else "Sin categorias.")
        elif op == "6":
            reporte_stock_bajo()
        elif op == "7":
            print("Fin.")
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
