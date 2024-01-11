import ui.titulos as title
import  funciones.menus as submenu
import funciones.corefile as core
import funciones.crear as crear
import importar.impordata as agregar
import os 
# import  importar.editardta as edita

core.NewFile()
core.NewFileG()
def inicio():
    title.menu_principal()
    op_menu = submenu.v_menuPrin()
    if op_menu ==1:
            os.system("cls")
            op_submenu=submenu.v_generos()
            os.system("pause & cls")
            if op_submenu ==1:
                crear.nuevo_genero()
                agregar.data_genero()
                os.system("pause & cls")
                inicio()
            elif op_submenu ==2:
                title.generos_listar()
                os.system("pause & cls")
                inicio() 
            else: 
                os.system("pause & cls")
                inicio()
    elif op_menu ==2:
        os.system("cls")
        sub_menu =submenu.v_actores()
        os.system("pause & cls")
        if sub_menu ==1:
            agregar.data_actor()
            os.system("pause & cls")
            inicio()
        elif sub_menu ==2:
            title.actores_listar()
            os.system("pause & cls")
            inicio()
        else:
            inicio()
    elif op_menu ==3:
        sub_menu = submenu.v_formato()
        os.system("cls & pause")
        if sub_menu ==1:
            agregar.data_formato()
            os.system("cls & pause")
            inicio()
        elif sub_menu ==2:
            title.formatos_listar()
            os.system("cls & pause")
            inicio()
        elif sub_menu ==3:
            inicio()
    elif op_menu ==4:
        op_menu = submenu.v_peliculas()
        os.system("cls & pause")
        if op_menu ==1:
            agregar.data_peliculas()
            inicio()
        elif op_menu ==2:
            pass
    
            
inicio()
# __init_ == "__name__":
#optinee los valoes[vkey]=varlor