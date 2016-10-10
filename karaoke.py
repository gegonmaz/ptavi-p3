#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import csv
import json
import urllib.request


def lista_etiquetas(misdatos):

    listado = ""
    for etiqueta in misdatos:
        listado = listado + etiqueta[0]
        atribs = etiqueta[1].items()
        for atrib, contenido in atribs:
            if contenido != "":
                listado = listado + "\t" + atrib + "=" + '"' + contenido + '"'
        listado = listado + "\n"
    return listado


def to_json(misdatos):
    with open('karaoke.json', 'w') as outfile_json:
            json.dump(misdatos, outfile_json, sort_keys=True, indent=3, 
            separators=(' ', ': '))


def url_local(misdatos):

    list_url = []
    for etiqueta in misdatos:
        atribs = etiqueta[1].items()
        for atrib, contenido in atribs:
            if atrib == "src":
                url = contenido
                list_url = url.split("/")
                remoto = list_url[0]
                if remoto == "http:":
                    arch_web = urllib.request.urlopen(url)
                    filename = list_url[-1]
                    print("Descargado..." + filename)
                    f = open(filename, "wb")
                    f.write(arch_web.read())
                else:
                    filename = contenido
                print("Este contenido ya está en local... " + filename)


if __name__ == "__main__":

    fich = sys.argv[1]
    try:
        Archivo = open(fich)

    except IndexError:
        sys.exit("Usege: python3 karaoke.py file.smil")

    parser = make_parser()
    ssHandler = SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(Archivo)
    tags = ssHandler.get_tags()    
    result = lista_etiquetas(misdatos)

    print(result)
    to_json(tags)
    url_local(tags)   
