# _*_ coding: utf-8 _*_
from lxml import etree
arbol=etree.parse("/home/franhidalgo/Documentos/LM/XML/colegios.xml")
directorios=arbol.getroot()
direct=directorios.findall("directorio/nombre")
for nom in direct:
	print nom.text
cole=raw_input("Mete un colegio: ")
