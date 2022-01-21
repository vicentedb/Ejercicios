import urllib.request
webPage = urllib.request.urlopen("https://www.as.com")
frase = webPage.read()
for line in pagina:
    print(line)



textoABuscar = input("Introduce un texto a buscar:")
textoABuscarMayusculas = textoABuscar.upper()
numeroOcurrencias = fraseMayusculas.count(textoABuscarMayusculas)
print("El texto buscado ha aparecido",numeroOcurrencias,"veces")