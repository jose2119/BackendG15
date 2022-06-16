"""
Crear un programa que convierta monedas a solas
"""
#entrada
monedaOrigen = input("ingrese moneda Origen:")
montoDestino=0
#proceso
if(monedaOrigen == "soles"):
    montoOrigen = input("ingrese el monto en " + monedaOrigen + " :")
    monedaDestino = "dolares"
    montoDestino = float(montoOrigen) / 3.778
elif(monedaOrigen == "dolares"):
    montoOrigen = input("ingrese el monto en " + monedaOrigen + " :")
    monedaDestino="soles"
    montoDestino = float(montoOrigen) * 3.778
else:
  print("no se puede convertir a la moneda ingresada")
#salida
if(montoDestino != 0):
    print("el monto en dolares es :" + str(montoDestino))