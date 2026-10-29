# productos.py

def obtener_catalogo_inicial():
    """Retorna una lista inicial de productos con ID, nombre, precio e IVA (porcentaje)."""
    return [
        {"id": 1, "nombre": "Cuaderno 100 Hojas", "precio": 4500.0, "iva": 19},
        {"id": 2, "nombre": "Lápiz Mirado N°2", "precio": 1200.0, "iva": 0},
        {"id": 3, "nombre": "Mochila Escolar", "precio": 85000.0, "iva": 19},
        {"id": 4, "nombre": "Caja de Colores x24", "precio": 18000.0, "iva": 19}
    ]

def buscar_producto_por_id(catalogo, id_producto):
    """Busca y retorna un producto según su ID."""
    for prod in catalogo:
        if prod["id"] == id_producto:
            return prod
    return None

def agregar_producto_catalogo(catalogo, nombre, precio, porcentaje_iva):
    """Crea un nuevo producto y lo añade al catálogo."""
    nuevo_id = len(catalogo) + 1
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "precio": float(precio),
        "iva": float(porcentaje_iva)
    }
    catalogo.append(nuevo_producto)
    return nuevo_producto