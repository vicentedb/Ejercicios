'''Mayor de edad
NACIONALIDAD: Frances o Aleman, y no Ruso
IDIOMAS 1 y 2: Ingles y Chino

Un sistema que pida al usuario información para determinar si lo contrata o no
PRIMERO TODAS LAS PREGUNTAS Y DESPUES SE DECIDE'''

'''edad = int(input("Dame tu edad:"))
if edad < 17:
    print ("Edad insuficiente")
else:
    nacionalidad = input("Dame tu nacionalidad:")
    if nacionalidad =="Frances" or nacionalidad =="Aleman"
        print("Nacionalidad correcta.")
        idioma = input("Introduce el idioma:")
        if idioma =="Ingles" or idioma=="Chino":
            print("CONTRATADO!!!!")
        else:
            print("NO CONTRATADO")
    else:
        print("NO CONTRATADO")'''


MAYORIA_EDAD=18
edad = int(input("Introduzca su edad:"))
nacionalidad = input("Introduzca su nacionalidad:")
idioma1 = input("Introduzca su primer idioma:")
idioma2 = input("Introduzca su segundo idioma:")
mayor_edad = edad>=MAYORIA_EDAD
nacionalidad_ok = (nacionalidad=="Frances" or nacionalidad=="Aleman") and nacionalidad !="Ruso"
idiomas_ok = idioma1=="Ingles" and idioma2=="Chino"

if (mayor_edad and nacionalidad_ok and idiomas_ok):
    print("Contratado")
else:
    print("Lo siento, no cumple con el perfil")