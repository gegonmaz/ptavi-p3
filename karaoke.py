#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler import SmallSMILHandler
import sys
import csv
import json


def lista_etiquetas(misdatos):
   
    for sublista in misdatos:
        etiquetas = sublista[0]
        atributos = sublista[1]
        resultado = str(etiquetas + '\t')        
        for clave in atributos:
            if atributos[clave]:
                  resultado = resultado + (str(clave + '="' + atributos[clave] 
+ '"' + '\n'))
        print(resultado)
def to_json(My_List, fich_name=""):

    if not fich_name:
        fich_name = "local.json"
    else:
        fich_name = fich_name.replace(".smil", ".json")
    with open(fich_name, 'w') as archivo_json:
        json.dump(My_List, archivo_json, indent=4,
                  separators=(' ', ': '), sort_keys=True)    

if __name__ == "__main__":

    
    """
    Programa principal
    nos haremos servir del main de samallamilshandler, que tiene ya todo creado,
    asi solo tendremos que coger el archivo para leerlo-->para ello tendremos
    que tener en cuenta el importar sys
    """
    
    #Tratamos de leer el archivo que se nos pase
    try:
        """
        Para ello crearemos un variable de tipo archivo, que guardara el archivo
        se le pase, para realizar esto, tendremos que utilizar el metodo sys
        que importamos anteriormente.y como hicimos en el programa de calcplus,
        fichero = sys.argv[1] utilizaremos el mismo metodo.
        """
        Archivo = open(sys.argv[1])
        """
        Ahora el programa nos dice que tenemos que tener en cuenta que hay 
        que especificar el fichero, asi que tendra que saltar un mensaje de
        error --> "Usege: python3 karaoke.py file.smil".
        """
    except IndexError:
        sys.exit("Usege: python3 karaoke.py file.smil")
        #return 'Usege: python3 karaoke.py file.smil'   
 
    parser = make_parser()
    sHandler =SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(Archivo)
    sHandler.get_tags()
    My_List = sHandler.get_tags()
    List = lista_etiquetas(My_List)
    to_json(My_List, fich.name)
    
    
