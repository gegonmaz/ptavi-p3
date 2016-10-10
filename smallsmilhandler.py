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

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if name == 'root_layout':            
            if self.width:
                self.width = self.width += char
            if self.height:
                self.height = self.height += char
            if self.background-color:
                self.background-color = self.background-color += char
        root_layout=['width','height','background-color']
        if name == 'region':
            if self.id:
                self.id= self.id += char
            if self.top:
                self.top = self.top += char
            if self.bottom:
                self.bottom= self.bottom += char
            if self.left:
                self.left = self.left += char
            if self.right:
                self.right= self.right += char
        region=['id','top','bottom','left','rigth']
        if name == 'img':
            if self.src:
                self.src = self.src += char
            if self.region:
                self.region=self.region += char
            if self.begin:
                self.begin = self.begin += char
            if self.dur:
                self.dur= self.dur += char
        img=['src','region','begin','dur']
        if name == 'audio':
            if self.src:
                self.src = self.src += char 
            if self.begin:
                self.begin = self.begin += char
            if self.dur:
                self.dur= self.dur += char
        audio=['src','begin','dur']
        if name == 'texstream':
            if self.src:
                self.src = self.src += char
            if self.region:
                self.region=self.region += char
        texstream = ['src','region']
  
    def get_tags(self):
        """
        Metodo para guardar los contenidos del texto e imprimirlos por pantalla
        """
        #Creamos un array que contenga los datos y los guarde.
        return self.misdatos
        # y luego los imprime.
