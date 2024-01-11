import ui.titulos as titulos
def v_menuPrin():
    titulos.menu_principal
    isActive=True
    while isActive:  
        try:      
            op_menu= int(input("ingrese una opcion "))
            while not (1<= op_menu <=6):
                print("Opcion no valida ")
                op_menu= int(input("ingrese una opcion "))
        except ValueError:
            print("Invalid opcion")
        except None:
            print("ingrese un valor")
        else: 
            isActive=False
    return int(op_menu) 
def v_generos():
    titulos.titulo_Generos()
    titulos.menu_generos()
    isActive=True
    while isActive: 
        try:
            op_menu = int(input(" Elija un aopcion"))
            while not (1<= op_menu <=3):
                print("opcion invlaida")
                op_menu = int(input(" Elija un aopcion"))
        except ValueError:
            print("Invalid option")
        else:
            isActive=False
    return int(op_menu)
def v_actores():
    titulos.titulo_actores()
    titulos.menu_actores()
    isActive=True
    while isActive: 
        try:
            op_menu = int(input(" Elija un aopcion"))
            while not (1<= op_menu <=3):
                print("opcion invlaida")
                op_menu = int(input(" Elija un aopcion"))
        except ValueError:
            print("Invalid option")
        else:
            isActive=False
    return int(op_menu)
def v_formato():
    titulos.titulo_formato() 
    titulos.menu_actores()
    isActive=True
    while isActive: 
        try:
            op_menu = int(input(" Elija un aopcion"))
            while not (1<= op_menu <=3):
                print("opcion invlaida")
                op_menu = int(input(" Elija un aopcion"))
        except ValueError:
            print("Invalid option")
        else:
            isActive=False
    return int(op_menu)
def v_precio():
    isActivbe = True
    while isActivbe:
        try:
            precio= float(input(" ingrese el valor del prestamo"))
            while precio <= 0:
                print("EL PRECIO NO PUEDE SER INFERIOR A 0 ")
                precio= float(input(" ingrese el valor del prestamo"))
        except ValueError:
            print("solo se permiten caracters numericos") 
        else: 
            isActivbe = False
    return float(precio)
def v_peliculas():
    titulos.titulo_principal()
    titulos.menu_pelicula()
    isActive=True
    while isActive: 
        try:
            op_menu = int(input(" Elija un aopcion"))
            while not (1<= op_menu <=7):
                print("opcion invlaida")
                op_menu = int(input(" Elija un aopcion"))
        except ValueError:
            print("Invalid option")
        else:
            isActive=False
    return int(op_menu)