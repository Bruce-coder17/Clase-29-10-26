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

# calculos.py

def calcular_subtotal_item(precio_unitario, cantidad):
    """Calcula el subtotal básico sin impuestos."""
    return precio_unitario * cantidad

def calcular_monto_iva(subtotal_item, porcentaje_iva):
    """Calcula el valor del IVA para un ítem."""
    return subtotal_item * (porcentaje_iva / 100.0)

def calcular_descuento(subtotal_neto, cantidad_total_items):
    """
    Aplica regla de negocio para descuentos:
    - 5% si el subtotal supera $100.000
    - 10% si lleva más de 10 unidades acumuladas
    """
    porcentaje_desc = 0.0
    if cantidad_total_items >= 10:
        porcentaje_desc = 0.10
    elif subtotal_neto >= 100000:
        porcentaje_desc = 0.05
        
    monto_descuento = subtotal_neto * porcentaje_desc
    return monto_descuento, porcentaje_desc * 100

def procesar_totales_carrito(items_carrito):
    """
    Recibe la lista de ítems en el carrito y calcula el resumen completo:
    subtotal neto, IVA total, descuento aplicado y total a pagar.
    """
    subtotal_neto = 0.0
    iva_total = 0.0
    total_unidades = 0

    for item in items_carrito:
        subtotal_i = calcular_subtotal_item(item["precio"], item["cantidad"])
        iva_i = calcular_monto_iva(subtotal_i, item["iva"])
        
        subtotal_neto += subtotal_i
        iva_total += iva_i
        total_unidades += item["cantidad"]

    descuento, porc_desc = calcular_descuento(subtotal_neto, total_unidades)
    total_pagar = (subtotal_neto - descuento) + iva_total

    return {
        "subtotal_neto": subtotal_neto,
        "iva_total": iva_total,
        "descuento": descuento,
        "porcentaje_descuento": porc_desc,
        "total_pagar": total_pagar,
        "total_unidades": total_unidades
    }