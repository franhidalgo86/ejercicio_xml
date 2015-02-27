# -*- coding: utf-8 -*-
from lxml import etree
arbol=etree.parse("/home/franhidalgo/Documentos/LM/XML/colegios.xml")
directorios=arbol.getroot()
direct=directorios.findall("directorio")
contador=0
for astu in direct:
	if "Asturiano: S" or "Asturiano: s" in astu.find("descripcion").text:
		contador=contador+1
print "Hay: ", contador, "colegios que dan Asturiano"
