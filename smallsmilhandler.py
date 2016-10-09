#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para leer archivos multimedia
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables 
        (Atributos que hay que tener en cuenta)
        """
        self.width = ""
        self.height = ""
        self.background-color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin =""
        self.dur = ""

        """
        No crearemos etiquetas de flag, porque el SMIL, no tiene informacion
        en los atributos
        """

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root_layout':
            # De esta manera tomamos los valores de los atributos
            self.widht = attrs.get('widht',"")
            self.height = attrs.get('height',"")
            self.backgound-color = attrs.get('background-color',"")            
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottoms = attrs.get('bottoms',"")  
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
        elif name == 'img':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"") 
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")

