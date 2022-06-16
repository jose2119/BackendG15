import os
import time
"""Aplicacion Crud
C- Create
R - READ
U - UPDATE
D - DELETE
PARA ESTE CASO USAREMOS ALUMNOS

[

  {'nombre':'','email':'','celular':''},
  {'nombre:'','email':'','celular':''}

]"""

alumnos = [{
          'nombre': 'joseph Peñafiel',
          'email':'josephpenafielloayza28@gmail.com',
          'celular':'961259746'
}]

opcion = 0
while(opcion != 5):
    if(opcion != 0):
        time.sleep(2)
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
    """)
    opcion = int(input("INGRESE LA OPCIÓN A EJECUTAR : "))
    os.system("clear")
    if(opcion == 1):
        print(
        """
        ============================
        [1] REGISTRO DE NUEVO ALUMNO
        ============================
        """)
        nombre = input("Nombre :")
        email = input("Email: ")
        celular = input("Celular : ")
        dictNuevoAlumno = {
          'nombre' : nombre,
          'email': email,
          'celular' : celular
        }
        alumnos.append(dictNuevoAlumno)
        print(
          """
          ========================
              Alumno Registrado !!
          ========================
          """
        )
    elif(opcion == 2):
        print(
        """
        ===========================================================
                        [2]  LISTADO DE ALUMNOS
        -----------------------------------------------------------
        |       NOMBRE        |       EMAIL   |       CELULAR     |
        -----------------------------------------------------------
        """)
        for alumno in alumnos:
            print("       ",end=' ')
            for values in alumno.values():
                print("|    " + values,end='    ')
            print()
        print('        ===========================================================')

        input("presione un tecla para continuar ...")
    elif(opcion == 3):
        print(
        """
        ========================
        [3]  ACTUALIZAR UN ALUMNO
        ========================
        """)
        valorBusqueda = input("Ingrese el elmail del alumno a actualizar")
        indiceAlumno = -1
    elif(opcion == 4):
        print(
        """
        ========================
        [4]  ELIMINAR ALUMNO
        ========================
        """)
    elif(opcion == 5):
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