import json 
import importar.impordata as imp
general = "data/peliculas.json"
genero= "data/genero.json"
def NewFile(**param):
    with open(general,"w")as wf :
        json.dump(param,wf)
def NewFileG(**param):
    with open(genero,"w")as wfT :
        json.dump(param,wfT)
