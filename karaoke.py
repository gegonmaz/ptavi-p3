#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler import SmallSMILHandler
import sys
import csv
import json


def lista_etiquetas(misdatos):
    
    listado = ""
    for diccs in misdatos:
        atrib_line = ""
    for key in diccs.keys():
        if key != "name" and diccs[key] != "":
           atrib_line = atrib_line + key + "=" + diccs[key] + "\t"
           listado = listado + diccs["name"] + "\t" + atrib_line + "\n"
    return listado 

def to_json(ListaDatos, nombreArchivo=""):

    if not nombreArchivo:
        nombreArchivo = "local.json"
    else:
        nombreArchivo = nombreArchivo.replace(".smil", ".json")
    with open(fich_name, 'w') as archivo_json:
        json.dump(ListaDatos, archivo_json, indent=4,
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
    ssHandler = SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(Archivo)
  
    tags = ssHandler.get_tags()
    print(tags)
    result = lista_etiquetas(misdatos)
    print(result)  
    

    
