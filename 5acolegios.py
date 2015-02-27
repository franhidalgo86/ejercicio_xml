# _*_ coding: utf-8 _*_
from lxml import etree
arbol=etree.parse("/home/franhidalgo/Documentos/LM/XML/colegios.xml")
directorios=arbol.getroot()
ident=directorios.findall("directorio/identificador")
for ide in ident:
	print ide.text
idcole=raw_input("Mete algun ID para saber el Colegio que es: ")
for iden in directorios:
	if iden.find("identificador").text==idcole:
		print iden.find("nombre").text
