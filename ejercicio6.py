import urllib.request
webpage = urllib.request.urlopen("https://as.com")
frase = webPage.read()
print(frase)



textoABuscar = input("Introduce un texto a buscar:")
textoABuscarMayusculas = textoABuscar.upper()
numeroOcurrencias = fraseMayusculas.count(textoABuscarMayusculas)
print("El texto buscado ha aparecido",numeroOcurrencias,"veces")