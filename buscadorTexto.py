import urllib.request
from win10toast import ToastNotifier
webPage = urllib.request.urlopen("https://www.as.com")
frase = webPage.read()
frase = str(frase)
print(type(frase))
veces = frase.count("Baloncesto")
texto = ("Se han encontrado" + str(veces) + "la palabra baloncesto en la web del AS")
toaster = ToastNotifier()
toaster.show_toast("Juanra aviso", texto)
