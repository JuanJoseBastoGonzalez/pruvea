import funciones.menus as menu
import json
blockbuster={    
              "peliculas":{
        "id":"",
        "nombre":"",
        "duraicon":"",
        "sinopsis":"",
        "generos":{
            # "g01":{
                # "id":"g01",
                # "nombre":"",
            },
        "actores":{},
        "formato":{}
                }
        #}
 }
generos={}
genero= "data/genero.json"
general = "data/peliculas.json"

#por si da tiempo 
# def data_peliculas():
#     nombre= input("ingrse el nombre de la pelicula")
#     time = input("imngrese la duracion de la pelucila")
#     texto = input("ingrese la sinopsis de la pelicula")
#     key = blockbuster.keys()
#     if key:
#         contador = str(int(max(key))+1).zfill(2)
#     else:
#         contador= "01"
#     blockbuster["peliculas"]={contador:{
#         "id":"",
#         "nombre":nombre,
#         "duraicon":time,
#         "sinopsis":texto,
#         "generos":{
            
#             },
#         "actores":{},
#         "formato":{}
#                 }
#     }
    
#     with open(general,"w")as cam:
#         json.dump(blockbuster,cam,indent=4)
#     print(blockbuster)


def data_actor():
    nombre = input("ingrese el nombre del actor")
    add = blockbuster.get("peliculas").get("actores")
    key = add.keys()
    if key:
        contador = str(int(max(key))+1).zfill(2)
    else:
      contador= "01"#falta lag
    add[contador]= {"id":contador,"nombre":nombre}
    with open(general,"w")as cam:
        json.dump(blockbuster,cam,indent=4)
    print(blockbuster)

def data_formato():
    id = ("ingrese el ide  la pelicula")
    valida= blockbuster.get("peliculas")
    if id not in valida:
        print("el id no existe")
    else:
        precio =  menu.v_precio
        nombre = input("ingrese el nombre del formato")
        copias = input(f"ingrese el numero de copias del formato {nombre}")
        add = blockbuster.get("peliculas").get("actores")
        key = add.keys()
        if key:
            contador = str(int(max(key))+1).zfill(2)
        else:
            contador= "01"#falta lag
        add[contador]= {"id":contador,"nombre":nombre,"copias":copias,"precio":precio}
        with open(general,"w")as cam:
            json.dump(blockbuster,cam,indent=4)
        print(blockbuster)

def data_peli():
    nombre = input("ingrese el nombre de la pelicula")
    add = blockbuster.get("peliculas")
    key = add.keys()
    if key:
        contador = str(int(max(key))+1).zfill(2)
    else:
      contador= "01"#falta lag
    add[contador]= {"id":contador,"nombre":nombre}
    with open(general,"w")as cam:
        json.dump(blockbuster,cam,indent=4)
    print(blockbuster)
  
def data_genero():
    nombre = input("ingrese el genero de la pelicula")
    add = blockbuster.get("peliculas").get("generos")
    key = add.keys()
    if key:
        contador = str(int(max(key))+1).zfill(2)
    else:
      contador= "01"#falta lag
    add[contador]= {"id":contador,"nombre":nombre}
    with open(general,"w")as cam:
        json.dump(blockbuster,cam,indent=4)
    with open(genero,"w")as cam:
        json.dump(generos,cam,indent=4)   
    print(blockbuster)

