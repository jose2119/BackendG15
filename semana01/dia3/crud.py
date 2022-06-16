import os
import time
from tabulate import tabulate
""" APLICACIÓN CRUD
C - CREATE
R - READ
U - UPDATE
D - DELETE
PARA ESTE CASO USAREMOS ALUMNOS
[
    {'nombre':'','email':'','celular':''},
    {'nombre':'','email':'','celular':''}
]
"""
alumnos = [
    {'nombre':'cesar mayta',
    'email':'cesarmayta@gmail.com',
    'celular':'956290589'}
    ]

############# FUNCIONES ###############
def buscarAlumno(valorBusqueda,listaAlumnos):
    indiceAlumno = -1
    for indice in range(len(listaAlumnos)):
        alumno = listaAlumnos[indice]
        for clave,valor in alumno.items():
            if(clave == "email" and valor == valorBusqueda):
                indiceAlumno = indice
                break
    return indiceAlumno

######################################

opcion = "0"
while(opcion != "5"):
    if(opcion != "0"):
        time.sleep(1)
        os.system("clear")
    print(
    """
    ===============================================================
                SISTEMA DE MATRICULA DE ALUMNOS
    ===============================================================
    [1] REGISTRAR ALUMNO
    [2] MOSTRAR ALUMNOS
    [3] ACTUALIZAR ALUMNO
    [4] ELIMINAR ALUMNO
    [5] SALIR DEL SISTEMA
    ===============================================================
    """)
    opcion = input("INGRESE LA OPCIÓN A EJECUTAR : ")
    os.system("clear")
    if(opcion == "1"):
        print(
        """
        ============================
        [1] REGISTRO DE NUEVO ALUMNO
        ============================
        """)
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        celular = input("CELULAR : ")
        dictNuevoAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictNuevoAlumno)
        print(
        """
        ================================
            ALUMNO REGISTRADO !!!
        ================================
        """)
    elif(opcion == "2"):
        columnas = ["nombre","email","celular"]
        tablaAlumnos = [alumno.values() for alumno in alumnos]
        print(tabulate(tablaAlumnos,headers=columnas,tablefmt="grid"))

        input("presione Enter para continuar ...")
        
    elif(opcion == "3"):
        print(
        """
        ========================
        [3]  ACTUALIZAR UN ALUMNO
        ========================
        """)
        valorBusqueda = input("ingrese el email del alumno a actualizar : ")
        
        indiceAlumno = buscarAlumno(valorBusqueda,alumnos)
        
        if(indiceAlumno == -1):
            print("No se encontro el alumno")
        else:
            print("alumno a editar : " + alumnos[indiceAlumno].get("nombre"))
            print("NUEVOS VALORES PARA EL ALUMNO : ")

            nombre = input("NOMBRE ("+ alumnos[indiceAlumno].get("nombre") +") : ")
            if(nombre == ''):
                nombre = alumnos[indiceAlumno].get("nombre")
            email = input("EMAIL ("+ alumnos[indiceAlumno].get("email") +") : ")
            if(email == ''):
                email = alumnos[indiceAlumno].get("email")
            celular = input("CELULAR ("+ alumnos[indiceAlumno].get("celular") +") : ")
            if(celular == ''):
                celular = alumnos[indiceAlumno].get("celular")
            dictAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            alumnos[indiceAlumno] = dictAlumnoEditar
            print("ALUMNO ACTUALIZADO!!!")
    elif(opcion == "4"):
        print(
        """
        ========================
        [4]  ELIMINAR ALUMNO
        ========================
        """)
        valorBusqueda = input("ingrese el email del alumno a eliminar : ")
        
        indiceAlumno = buscarAlumno(valorBusqueda,alumnos)

        if(indiceAlumno == -1):
            print("No se encontro el alumno")
        else:
            alumnos.pop(indiceAlumno)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == "5"):
        print(
        """
        ===========================
        EL SISTEMA SE ESTA CERRANDO
        ===========================
        """)
    else:
        print(
        """
        ===========================
            OPCIÓN INCORRECTA!!!
        ===========================
        """)