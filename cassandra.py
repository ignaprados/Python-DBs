import uuid
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

# Start Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.execute('use empleados')

# Funciones de Cargar datos

# Q1
def cargar_empleados_por_habilidad_y_deporte():
    nombre_empleado= input('Nombre Empleado: ')
    apellido_empleado= input('Apellido Empleado: ')
    descripcion_habilidad= input('Descripcion Habilidad: ')
    nombre_deporte= input('Nombre Deporte: ')

    session.execute("""INSERT INTO empleados_por_habilidad_y_deporte (id_empleado, nombre_empleado, apellido_empleado, descripcion_habilidad, nombre_deporte) VALUES (%s, %s, %s, %s, %s)""", (uuid(), nombre_empleado, apellido_empleado, descripcion_habilidad, nombre_deporte))

# Funciones de Mostrar datos

# Q1
def mostrar_empleados_por_habilidad_y_deporte():
    rows = session.execute("""SELECT * FROM empleados_por_habilidad_y_deporte;""")

    for row in rows:
        print(row)

# Funciones de Queries

# Q1
def empleados_por_habilidad_y_deporte():
    rows = session.execute("""SELECT * FROM empleados_por_habilidad_y_deporte WHERE descripcion_habilidad='Liderazgo' AND nombre_deporte='Futbol';""")
    for row in rows:
        print(row)



# App ----------------------------------------------------------
def menu():

    print('Bienvenido, eliga una opcion')
    print('--------------------------------------')
    print('1. Cargar datos')
    print('2. Mostrar contendo')
    print('--------------------------------------')
    print('3. Ejecutar Q1')
    print('4. Ejecutar Q2')
    print('5. Ejecutar Q3')
    print('6. Ejecutar Q4')
    print('7. Ejecutar Q5')
    print('8. Ejecutar Q6')
    print('9. Ejecutar Q7')
    print('10. Ejecutar Q8')
    print()
    opcion = input('opcion: ')
    if opcion == '1' :

        print("Seleccione la estructura")
        print('--------------------------------------')
        print('1. empleados_por_habilidad_y_deporte')
        print('2. trabajos_previos_por_habilidad')
        print('3. deportes_por_trabajos_previos_entre_fechas')
        print('4. empleados_por_deporte_de_riesgo_desde_fecha')
        print('5. habilidades_por_empleado')
        print('6. deportes_por_trabajo')
        print('7. empleados_por_trabajo_deporte_federado')
        print('8. empleados_por_habilidad_y_trabajo_previo_entre_fechas')
        print()

        opcion = input('opcion: ')

        if opcion == '1' :
            cargar_empleados_por_habilidad_y_deporte()
            print('Carga realizada.')
            time.sleep(5)
            menu()

        elif opcion == '2' :
            cargar_trabajos_previos_por_habilidad()

        elif opcion == '3' :
            cargar_deportes_por_trabajos_previos_entre_fechas()

        elif opcion == '4' :
            cargar_empleados_por_deporte_de_riesgo_desde_fecha()

        elif opcion == '5' :
            cargar_habilidades_por_empleado()

        elif opcion == '6' :
            cargar_deportes_por_trabajo()

        elif opcion == '7' :
            cargar_empleados_por_trabajo_deporte_federado()

        elif opcion == '8' :
            cargar_empleados_por_habilidad_y_trabajo_previo_entre_fechas()

        else:
            print("opcion incorrecta")
            time.sleep(5)
            menu()

    elif opcion == '2' :

        print("Seleccione la estructura")
        print('--------------------------------------')
        print('1. empleados_por_habilidad_y_deporte')
        print('2. trabajos_previos_por_habilidad')
        print('3. deportes_por_trabajos_previos_entre_fechas')
        print('4. empleados_por_deporte_de_riesgo_desde_fecha')
        print('5. habilidades_por_empleado')
        print('6. deportes_por_trabajo')
        print('7. empleados_por_trabajo_deporte_federado')
        print('8. empleados_por_habilidad_y_trabajo_previo_entre_fechas')
        print()

        opcion = input('opcion: ')

        if opcion == '1' :
            mostrar_empleados_por_habilidad_y_deporte()
            time.sleep(5)
            menu()

        elif opcion == '2' :
            mostrar_trabajos_previos_por_habilidad()

        elif opcion == '3' :
            mostrar_deportes_por_trabajos_previos_entre_fechas()

        elif opcion == '4' :
            mostrar_empleados_por_deporte_de_riesgo_desde_fecha()

        elif opcion == '5' :
            mostrar_habilidades_por_empleado()

        elif opcion == '6' :
            mostrar_deportes_por_trabajo()

        elif opcion == '7' :
            mostrar_empleados_por_trabajo_deporte_federado()

        elif opcion == '8' :
            mostrar_empleados_por_habilidad_y_trabajo_previo_entre_fechas()

        else:
            print("opcion incorrecta")
            menu()

    elif opcion == '3' :
        empleados_por_habilidad_y_deporte()
        time.sleep(5)
        menu()

    elif opcion == '4' :
        trabajos_previos_por_habilidad()

    elif opcion == '5' :
        deportes_por_trabajos_previos_entre_fechas()

    elif opcion == '6' :
        empleados_por_deporte_de_riesgo_desde_fecha()

    elif opcion == '7' :
        habilidades_por_empleado()

    elif opcion == '8' :
        deportes_por_trabajo()

    elif opcion == '9' :
        empleados_por_trabajo_deporte_federado()

    elif opcion == '10' :
        empleados_por_habilidad_y_trabajo_previo_entre_fechas()



# Run program
menu()