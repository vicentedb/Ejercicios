#Pida al usuario un texto
#Busque cuantas veces aparece independientemente si está en mayúsculas o minúsculas.


frase = "EN UN LUGAR DE LA MANCHA, LA MANCHA ES UNA REGION"
textoABuscar = input("Introduce un texto a buscar:")
textoABuscar = textoABuscar.upper()
numeroOcurrencias = frase.count(textoABuscar)
print("El texto buscado ha aparecido",numeroOcurrencias,"veces")
