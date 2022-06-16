"""
Ejercicios 01:
Ingrese un texto y un divisor y luego
muestre el mismo texto pero divido
por el divisor
ejemplo:ingreso 
texto=abcdefg
divisor=2
resultado:
ab
cd
ef
g
"""
texto=input("ingrese un texto: ")
divisor= int(input("Ingrese el divisor: "))
for contador in range(0,len(texto),divisor):
    print(texto[contador:divisor+contador])


