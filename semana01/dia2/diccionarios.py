capitales = {
  'Peru' : 'Lima',
  'Ecuador' : 'Quito',
  'Chile':'Santiago',
  'Uruguay':'Montevideo'
}

# print(capitales)
# nuevaCapital = {'Brasil':'Brasilia'}
# capitales.update(nuevaCapital)
# print(capitales)
# capitales.update({'Ecuador':'Guayaquil'})
# print(capitales.get('Ecuador'))

# pais = input("Ingrese el pais:")
# capital = capitales.get(pais, 'no existe')
# print("la capital de " + pais + " es " + capital)
# c = capitales.pop('Ecuador','no existe')
# print("eliminaste" + c)
# print(capitales)

#Iteracion de Diccionarios
for capital in capitales:
    print('la capital de ' + capital + " es " + capitales[capital])
    print(capitales.keys())
    print(capitales.values())
    print(capitales.items())

    for clave in capitales.keys():
        print(clave + " => " + capitales[clave])

    for clave,valor in capitales.items():
      print(clave + " -- " + valor)
