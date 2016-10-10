#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler.py import SAMLLSmilHandler
import sys
import csv

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
        Archivo = sys.argv[1]
        """
        Ahora el programa nos dice que tenemos que tener en cuenta que hay 
        que especificar el fichero, asi que tendra que saltar un mensaje de
        error --> "Usege: python3 karaoke.py file.smil".
        """
    except KeyError:
        return Usege: python3 karaoke.py file.smil
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(Archivo)) #tendrá que abrir cualquier archivo

    cHandler.get_tags()
    # hago cosas con mis datos (los imprimo por pantalla, mediante el metodo)
