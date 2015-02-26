# _*_ coding: utf-8 _*_
from lxml import etree
arbol=etree.parse("/home/franhidalgo/Documentos/LM/XML/colegios.xml")
directorios=arbol.getroot()
ident=directorios.findall("directorio")