import importar.impordata as imp
def menu_principal():
    titulo_principal()
    menu=["1.Admiistador de Genros","2. Administrator de Actores","3. Administrator de Formatos","4. Gestor de pelicula","5. Gestor de informes","6. Salir"]
    for i in menu:
        print(i)
def titulo_principal():
    titul="""
    ***************************************
    *  Bienvenido al sistema de peliculas *
    ***************************************
    """
    print(titul)
def titulo_Generos():
    titul="""
    **********************************
    *   SISTEMA  GESTOR DE GENEROS   *
    ***********************************
    """
    print(titul)
def menu_generos():
    menu=["1. Crear generoo","2. Listar generos","3. Ir amenuprincipal"]
    for i in menu:
        print(i)
def generos_listar():
  gnero = imp.blockbuster.get("peliculas").get("generos")
  key = gnero.keys()
  print(key)
  
  
def titulo_actores():
    titul="""
    **********************************
    *   SISTEMA  GESTOR DE ACTORES   *
    **********************************
    """
    print(titul)
def menu_actores():
    menu=["1. Crear actores","2. Listar actores","3. Ir amenuprincipal"]
    for i in menu:
        print(i)
def actores_listar():
  try:
    gnero = imp.blockbuster.get("peliculas").get("actores")
  except UnboundLocalError:
      print("no hay actores registrados")
  key = gnero.keys()
  print(key)
  
def titulo_formato():
    titul="""
    ***********************************
    *   SISTEMA  GESTOR DE FORMATOS   *
    ***********************************
    """
    print(titul)
def menu_formato():
    menu=["1. Crear formato","2. Listar formatos","3. Ir amenuprincipal"]
    for i in menu:
        print(i)
def formatos_listar():
  gnero = imp.blockbuster.get("peliculas").get("formato")
  key = gnero.keys()
  print(key)
  


def titulo_pelicula():
    titul="""
    ************************************
    *   SISTEMA  GESTOR DE PELICULAS   *
    ************************************
    """
    print(titul)
def menu_pelicula():
    menu=["1. Agregar pelicula","2. Editar pelicula","3. Eliminar pelicula","4. Esliminar actor","5. Buscar pelicula","6. Listar peluculas","7. Menu principal"]
    for i in menu:
        print(i)
def pelicula_listar():
    try:
        gnero = imp.blockbuster.get("peliculas")
    except None:
        print("no hay pelicuals registras")   
        key = gnero.keys()
        print(key)    
