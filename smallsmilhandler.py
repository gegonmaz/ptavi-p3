#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__ (self):
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
        self.begin = ""
        self.dur = ""
        self.misdatos = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.root_layout = {}
            self.misdatos.append(name)
            # De esta manera tomamos los valores de los atributos
            self.widht = attrs.get('widht', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background-color', "")
            self.root_layout=['widht' + ' = ' + self.width, 'height' + ' = ' + 
self.height, 'backgroundcolor' + ' = ' + self.background_color]
            self.misdatos.append(self.root_layout)
           
        elif name == 'region':
            self.region = {}
            self.misdatos.append(name)
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottoms = attrs.get('bottoms', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.region=['id'+' = ' + self.id,'top' + ' = ' +  self.top, 
'bottom' + ' = ' + self.bottom, 'left' + ' = ' + self.left, 'right' + 
' = ' + self.right]
            self.misdatos.append(self.region)

        elif name == 'img':
            self.img = {}
            self.misdatos.append(name)
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.img = ['src' + ' = ' + self.src,'region' + ' = ' 
+ self.region, 'begin' + ' = ' + self.begin, 'dur' + ' = ' + self.dur]
            self.misdatos.append(self.img)

        elif name == 'audio':
            self.audio = {}
            self.misdatos.append(name)
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.audio=['src' + ' = ' + self.src,'begin' + ' = ' + self.begin,
'dur' + ' = ' + self.dur]
            self.misdatos.append(self.audio)
 
        elif name == 'textstream':
            self.texstream = {}
            self.misdatos.append(name)
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.texstream = ['srs' + ' = ' + self.src, ' region' + 
' = ' + self.region]
            self.misdatos.append(self.texstream)

    def get_tags(self):
       
        print (self.misdatos)
        return self.misdatos

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    sHandler.get_tags()
