#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import SAMLLSmilHandler

if __name__ == "__main__":
    """
    Programa principal
    nos haremos servir del main de samallamilshandler, que tiene ya todo creado,
    asi solo tendremos que coger el archivo para leerlo
    """
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(File)) ###tendrá que abrir cualquier archivo

    cHandler.get_tags()
    # hago cosas con mis datos (los imprimo por pantalla, mediante el metodo)
