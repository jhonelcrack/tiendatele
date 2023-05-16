productos = [
    {"nombre": "Apple X", "almacenamiento": "256gb", "colores": ["negro", "blanco"], "precio": 1600000},
    {"nombre": "Apple 12 Pro", "almacenamiento": "1tb", "colores": ["negro"], "precio": 2600000},
]

print("Seleccione un producto:")
for i, producto in enumerate(productos):
    print(f"{i + 1}: {producto['nombre']} ({producto['almacenamiento']}) - {producto['precio']}")

opcion = int(input("usted selecciono: "))

producto = productos[opcion - 1]

if len(producto['colores']) > 1:
    print("Seleccione un color:")
    for i, color in enumerate(producto['colores']):
        print(f"{i + 1}: {color}")
    color_opcion = int(input("usted selecciono: "))
    color = producto['colores'][color_opcion - 1]
else:
    color = producto['colores'][0]

nombre = input("Nombre: ")
apellido = input("Apellido: ")
cedula = input("Número de cédula: ")
metodo_pago = input("Método de pago: ")
direccion = input("Dirección: ")
telefono = input("Teléfono: ")

print(f"Resumen de la compra:\n{producto['nombre']} ({producto['almacenamiento']}) - {color} - {producto['precio']}")
print(f"Comprador: {nombre} {apellido} ({cedula})")
print(f"Método de pago: {metodo_pago}")
print(f"Dirección de entrega: {direccion}")
print(f"Teléfono de contacto: {telefono}")