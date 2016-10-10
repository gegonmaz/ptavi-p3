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
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin =""
        self.dur = ""
        self.misdatos=[]
        """
        No crearemos etiquetas de flag, porque el SMIL, no tiene informacion
        en los atributos
        """

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.root_layout = {}
            self.misdatos.append(name)
            # De esta manera tomamos los valores de los atributos
            self.widht = attrs.get('widht',"")
            self.height = attrs.get('height',"")
            self.background_color = attrs.get('background-color',"") 
            self.root_layout=[self.width,self.height,self.background_color]
            self.misdatos.append(self.root_layout)           
        elif name == 'region':
            self.misdatos.append(name)
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottoms = attrs.get('bottoms',"")  
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            self.region=[self.id,self.top,self.bottom,self.left,self.right]
            self.misdatos.append(self.region)
        elif name == 'img':
            self.img = {}
            self.misdatos.append(name)
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            self.img = [self.src,self.region]
            self.misdatos.append(self.img)
        elif name == 'audio':
            self.audio = {}
            self.misdatos.append(name)
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            self.audio=[self.src,self.begin,self.dur]
            self.misdatos.append(self.audio) 
        elif name == 'textstream':
            self.texstream = {}
            self.misdatos.append(name)
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.texstream = [self.src,self.region]
            self.misdatos.append(self.texstream)
        """
        Metodo para guardar los contenidos del texto e imprimirlos por pantalla
        """
        #Creamos un array que contenga los datos y los guarde.(metodo anterior)
    def get_tags(self):
       
        print (self.misdatos)
        return self.misdatos
        # y luego los imprime.
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))

    sHandler.get_tags()
    # hago cosas con mis datos(imprimo por pantalla con el metodo get_tags)
