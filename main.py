# main.py
from productos import obtener_catalogo_inicial, buscar_producto_por_id, agregar_producto_catalogo
from calculos import procesar_totales_carrito
from facturacion import calcular_cambio, generar_texto_factura, guardar_factura_archivo

def leer_entero(mensaje):
    """Manejo de excepciones para lectura de números enteros."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def leer_flotante(mensaje):
    """Manejo de excepciones para lectura de números decimales."""
    while True:
        try:
            val = float(input(mensaje))
            if val < 0:
                print("El valor no puede ser negativo.")
                continue
            return val
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def mostrar_catalogo(catalogo):
    print("\n--- CATÁLOGO DE PRODUCTOS DISPONIBLES ---")
    print(f"{'ID':<4} {'Nombre':<25} {'Precio Base':<12} {'IVA (%)':<8}")
    print("-" * 50)
    for p in catalogo:
        print(f"{p['id']:<4} {p['nombre']:<25} ${p['precio']:<11.2f} {p['iva']}%")

def ejecutar_sistema():
    catalogo = obtener_catalogo_inicial()
    carrito = []
    
    while True:
        print("\n==========================================")
        print("     CALCULADORA Y SISTEMA DE VENTAS      ")
        print("==========================================")
        print("1. Ver catálogo de productos")
        print("2. Agregar producto al carrito")
        print("3. Registrar nuevo producto en catálogo")
        print("4. Ver resumen del carrito y procesar pago")
        print("5. Salir")
        
        opcion = leer_entero("Seleccione una opción (1-5): ")

        if opcion == 1:
            mostrar_catalogo(catalogo)

        elif opcion == 2:
            mostrar_catalogo(catalogo)
            id_prod = leer_entero("\nIngrese el ID del producto a comprar: ")
            producto = buscar_producto_por_id(catalogo, id_prod)
            
            if producto:
                cant = leer_entero(f"Ingrese la cantidad de '{producto['nombre']}': ")
                if cant > 0:
                    item_comprado = {
                        "id": producto["id"],
                        "nombre": producto["nombre"],
                        "precio": producto["precio"],
                        "iva": producto["iva"],
                        "cantidad": cant
                    }
                    carrito.append(item_comprado)
                    print(f"✓ {cant} unidad(es) agregadas al carrito.")
                else:
                    print("La cantidad debe ser mayor a 0.")
            else:
                print("Producto no encontrado.")

        elif opcion == 3:
            print("\n--- REGISTRO DE NUEVO PRODUCTO ---")
            nombre = input("Nombre del producto: ").strip()
            precio = leer_flotante("Precio base ($): ")
            porc_iva = leer_flotante("Porcentaje de IVA (ejemplo 19): ")
            
            nuevo_prod = agregar_producto_catalogo(catalogo, nombre, precio, porc_iva)
            print(f"✓ Producto '{nuevo_prod['nombre']}' registrado con exito con ID {nuevo_prod['id']}.")

        elif opcion == 4:
            if not carrito:
                print("El carrito está vacío. Agregue productos antes de cobrar.")
                continue

            resumen = procesar_totales_carrito(carrito)
            print("\n" + "="*30)
            print("RESUMEN DE PRE-VENTA")
            print("="*30)
            print(f"Subtotal Neto: ${resumen['subtotal_neto']:.2f}")
            print(f"IVA Total:     ${resumen['iva_total']:.2f}")
            print(f"Descuento:     -${resumen['descuento']:.2f}")
            print(f"TOTAL A PAGAR: ${resumen['total_pagar']:.2f}")

            cliente = input("\nIngrese nombre del cliente: ").strip()
            if not cliente:
                cliente = "Cliente General"

            pago_exitoso = False
            efectivo = 0.0
            devueltas = 0.0

            while not pago_exitoso:
                efectivo = leer_flotante("Ingrese el monto abonado por el cliente ($): ")
                valido, resultado = calcular_cambio(resumen['total_pagar'], efectivo)
                
                if valido:
                    pago_exitoso = True
                    devueltas = resultado
                else:
                    print(f"Faltan ${resultado:.2f} para completar el pago.")

            factura_txt = generar_texto_factura(cliente, carrito, resumen, efectivo, devueltas)
            print("\n" + factura_txt)
            
            archivo_generado = guardar_factura_archivo(factura_txt)
            print(f"\n✓ Factura guardada en el archivo: {archivo_generado}")
            
            carrito.clear() # Limpiar carrito tras finalizar compra

        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Elija un número entre 1 y 5.")

if __name__ == "__main__":
    ejecutar_sistema()