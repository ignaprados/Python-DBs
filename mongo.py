from pymongo import MongoClient
import time
from datetime import datetime


# Iniciar Mongo -------------------------------------------

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["final"]
collection = db["viajes"]


# App ----------------------------------------------------------

def menu():

    print('Bienvenido, eliga una opcion')
    print('--------------------------------------')
    print('1.	¿Cuántos viajes hizo el usuario Bunny?')
    print('2.	¿Quiénes hicieron un viaje redondo (es decir salieron y llegaron al mismo destino)?')
    print('3.	¿Cuál fue el usuario con más viajes (puede ser más de uno)?')
    print('4.	¿Cuál fue el origen y destino del viaje más largo (en tiempo)?')
    print('5.	¿Qué orígenes y destinos son los más populares?')
    print('6.	¿En qué días de la semana se realizan la mayoría de los viajes?')
    print('--------------------------------------')
    print('8.   Insertar Viaje')
    print('9.   Modificar Viaje')

    opcion = input('opcion: ')
    if opcion == '1' :

        rows = collection.count_documents({"usuario.nombre":"Bunny", "usuario.nacimiento": 2003})
        for row in rows:
            print(row)

        time.sleep(5)
        menu()

    elif opcion == '2' :

        rows = collection.find({ "$expr": { "$eq": ["$lugarOrigen", "$lugarDestino"] }})
        for row in rows:
            print(row)

        time.sleep(5)
        menu()

    elif opcion == '3' :

        rows = collection.aggregate([ { "$group": { "_id": {"usuario.nombre":"$usuario.nombre", "usuario.nacimiento":"$usuario.nacimiento" }, "viajes": { "$count": "$numero" } } },])
        for row in rows:
            print(row)

        time.sleep(5)
        menu()

    elif opcion == '4' :

        rows = collection.aggregate( [ { "$group": { "_id": "$numero", "largo": { "$substract": ["fechaDestino","fechaOrigen"] } } }, { "$project": { "numero": 1, "fechaOrigen": 1, "fechaDestino": 1} }, { "$sort": { "largo": -1 } }, { "$limit": 1 } ])
        for row in rows:
            print(row)

        time.sleep(5)
        menu()

    elif opcion == '5' :

        print('Origen mas popular')
        rows = collection.aggregate([ { "$group": { "_id": "$lugarOrigen", "cant": { "$count": "$lugarOrigen"} } }, { "$project": {"lugarOrigen": 1} }, { "$sort": { "cant": -1 } }, { "$limit": 1 } ])
        for row in rows:
            print(row)

        print('--------------------------------------')

        print('Destino mas popular')
        rows = collection.aggregate([ { "$group": { "_id": "$lugarDestino", "cant": { "$count": "$lugarDestino"} } }, { "$project": {"lugarDestino": 1} }, { "$sort": { "cant": -1 } }, { "$limit": 1 } ])
        for row in rows:
            print(row)

        time.sleep(5)
        menu()

    elif opcion == '6' :

        collection.aggregate([ { "$group": { "dayOfWeek": { "$dayOfWeek": "$fechaOrigen"}, "cant": { "$count": "$numero"} } }, { "$project": {"dayOfWeek": 1} }, { "$sort": { "cant": -1 } }, { "$limit": 3 } ])
        time.sleep(5)
        menu()

    elif opcion == '7' :

        numero = input("numero: ")
        usuario_nombre = input("usuario nombre: ")
        usuario_nacimiento = input("usuario nacimiento: ")
        lugarOrigen = input("lugarOrigen: ")
        fechaOrigen = input("fechaOrigen (2020-04-12T09:28): ")
        lugarDestino = input("lugarDestino: ")
        fechaDestino = input("fechaDestino (2020-04-12T09:28): ")

        fechaOrigen = datetime.fromisoformat(fechaOrigen)
        fechaDestino = datetime.fromisoformat(fechaDestino)

        collection.insert_one({"numero": numero, "usario": { "nombre": usuario_nombre, "nacimiento": usuario_nacimiento }, "lugarOrigen": lugarOrigen, "fechaorigen": fechaOrigen, "lugarDestino": lugarDestino, "fechaDestino": fechaDestino})

        time.sleep(5)
        menu()

    elif opcion == '8' :

        numero = input("numero de viaje a modificar: ")
        opcion = input("Modificar Lugar Origen(1) o Destino?(2): ")

        if opcion == '1':

            lugarOrigen = input("nuevo lugarOrigen: ")
            collection.update_one({"numero": numero}, {"$set": {"lugarOrigen": lugarOrigen}})

        elif opcion == '2':

            lugarDestino = input("nuevo lugarDestino: ")
            collection.update_one({"numero": numero}, {"$set": {"lugarDestino": lugarDestino}})

        else:
            print("opcion incorrecta")
            time.sleep(2)
            menu()

        print("viaje modificado con exito")

        time.sleep(5)
        menu()

    else:
        print("opcion incorrecta")
        time.sleep(5)
        menu()




# Run program
menu()
