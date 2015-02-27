# -*- coding: utf-8 -*-
from lxml import etree
arbol=etree.parse("/home/franhidalgo/Documentos/LM/XML/colegios.xml")
directorios=arbol.getroot()
direct=directorios.findall("directorio")
for cole in direct:
	if "Comedor: S" in cole.find("descripcion").text:	
		print "Tiene comedor: " ,cole.find("nombre").text