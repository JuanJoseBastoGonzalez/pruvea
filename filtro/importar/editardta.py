import impordata as importa
def eliminar_peli():
    nombre = input("ingrese el id de la pelicula que sedesea editar")
    id = importa.blockbuster("peliculas")
    if nombre not in id:
        print("pelicula no encontrada")
    else:
        id.pop(nombre)
        print(importa.blockbuster)
def editar_peli():
    nombre = input("ingrese el id de la pelicula que sedesea editar")

    id = importa.blockbuster("peliculas")
    if nombre not in id:
        print("pelicula no encontrada")
    else:
        id[nombre]
        print(importa.blockbuster)
        