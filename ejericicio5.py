#Pida al usuario un texto
#Busque cuantas veces aparece independientemente si está en mayúsculas o minúsculas.


frase = "En un lugar de la Mancha, la Mancha es una región"
fraseMayusculas = frase.upper()
textoABuscar = input("Introduce un texto a buscar:")
textoABuscarMayusculas = textoABuscar.upper()
numeroOcurrencias = fraseMayusculas.count(textoABuscarMayusculas)
print("El texto",textoABuscar, "ha aparecido",numeroOcurrencias,"veces")
