# facturacion.py
from datetime import datetime

def calcular_cambio(total_pagar, efectivo_recibido):
    """Valida si el pago cubre el total y retorna el cambio sobrante."""
    if efectivo_recibido < total_pagar:
        return False, total_pagar - efectivo_recibido
    return True, efectivo_recibido - total_pagar

def generar_texto_factura(cliente, items_carrito, resumen_totales, efectivo, cambio):
    """Construye una cadena de texto formateada con la factura detallada."""
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lineas = []
    lineas.append("=" * 45)
    lineas.append(" COMPROBANTE DE COMPRA")
    lineas.append("=" * 45)
    lineas.append(f"Fecha: {fecha_hora}")
    lineas.append(f"Cliente: {cliente}")
    lineas.append("-" * 45)
    lineas.append(f"{'Cant':<5} {'Producto':<20} {'P.Unit':<10} {'Subtotal':<10}")
    lineas.append("-" * 45)

    for item in items_carrito:
        subtotal_item = item["precio"] * item["cantidad"]
        lineas.append(f"{item['cantidad']:<5} {item['nombre'][:18]:<20} ${item['precio']:<9.2f} ${subtotal_item:<9.2f}")

    lineas.append("-" * 45)
    lineas.append(f"Subtotal Neto: ${resumen_totales['subtotal_neto']:>12.2f}")
    lineas.append(f"IVA Total: ${resumen_totales['iva_total']:>12.2f}")
    if resumen_totales['descuento'] > 0:
        lineas.append(f"Descuento ({resumen_totales['porcentaje_descuento']:.0f}%): -${resumen_totales['descuento']:>12.2f}")
    lineas.append(f"TOTAL A PAGAR: ${resumen_totales['total_pagar']:>12.2f}")
    lineas.append("-" * 45)
    lineas.append(f"Efectivo Recibido: ${efectivo:>12.2f}")
    lineas.append(f"Cambio / Devueltas: ${cambio:>12.2f}")
    lineas.append("=" * 45)
    lineas.append(" ¡Gracias por su compra!")
    lineas.append("=" * 45)

    return "\n".join(lineas)

def guardar_factura_archivo(texto_factura, id_factura=1):
    """Exporta el texto de la factura a un archivo .txt."""
    nombre_archivo = f"factura_{id_factura}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(texto_factura)
    return nombre_archivo