"""A traves de tuplas o lista me van a calcular el promedio de 10 personas respecto a sus edades que se piden por teclado"""
# edades= []
# for i in range(10):
#     edad= int(input("¿Cual es tu edad?: "))
#     edades += [edad]
# print(sum(edades)/10)

"""3 listas:
- nombres
- precios
- cantidades
calcular el valor de descuento de aquellos productos cuya compra supere los 50.000 si el descuento aplicado es del 2% """
nombres= ["Chocolates", "Perfumes", "Usb", "bombones", "paquetes de gomitas"]
precios= []
cantidades= []
for i in nombres:
    cantidad= int(input(f"Cuantos {i} llevas?: "))
    cantidades += [cantidad]
    precio= int(input(f"Cual es el precio de los {i}: "))
    precios+=[precio]
    precioTotal= precio*cantidad
    if precioTotal > 50000:
        descuento= precioTotal*0.02
        print(f"Su producto obtuvo un descuento su precio final es de: ${descuento} ")
    else:
        print(f"El precio final de su producto es: {precioTotal}")
