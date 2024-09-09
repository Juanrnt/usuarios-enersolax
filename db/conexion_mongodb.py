from pymongo import MongoClient

try:
    
    client = MongoClient("localhost",27017) #aqui se debe colocar la direcion del servidor, en este caso localhost

    #ahora seleccionamos la coleccion con la que vamos a trabajar, para eso accedemos a la data y posterior a la coleccion

    database = client["enersolax"]

    collection = database["users"] #para nuesto caso la colleccion es users debido a que contiene todos los usuarios

    documents = collection.find() #Para nuestro caso cada document es un usuario
    
    for document in documents:
        print(document)
        
except Exception as ex:
    print("Error duante la conexion: {}".format(ex))
finally:
    client.close()
    print("conexión finalizada")
    
