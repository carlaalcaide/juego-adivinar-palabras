#Trabajo realizado por Carla y Julia Alcaide Martínez.
import random
print("Te damos la bienvenida al juego de adivinar palabras")
print("Este juego consistira en que debes adivinar una palabra relacionada con casa y que contenga 6 letras")
print("Para superar el juego tendrás 7 intentos")
print("Para que la solución sea correcta debes escribir la primera letra en mayúscula")
print("Para que el juego te resulte más fácil te digo entre que palabras está la solución:Balcon,Casita,Cocina,Espejo,Tejado,Placas,Estufa,Toalla,Colcha,Mueble,Sabana,Lavabo,Platos,Alarma,Bañera,Mesita,Sartén,Cuarto,Plantas,Timbre,Puerta,Jardin,Cuadro,Cables,Escoba,Mantel,Butaca,Jarrón,Percha,Suelos,Baúles,Ropero,Basura,Hornos,Grifos,Vasija,Alcoba,Mantas,Garage,Tetera.")
print("¡Que comience la diversión!")
#crear una lista
lista=["Balcon", "Casita", "Cocina", "Espejo", "Tejado", "Placas", "Estufa", "Toalla", "Colcha", "Mueble", "Sabana", "Lavabo", "Platos", "Alarma", "Bañera", "Mesita", "Sarten", "Cuarto", "Plantas", "Timbre","Puerta", "Jardin", "Cuadro", "Cables", "Escoba", "Mantel", "Butaca", "Jarrón", "Percha", "Suelos", "Baúles", "Ropero", "Basura", "Hornos", "Grifos", "Vasija", "Alcoba", "Mantas", "Garage", "Tetera"]
palabra = random.choice(lista)
#print("DEPURACION: " + palabra)
ganar = False
#volver a repetir
for i in range(1, 7):
        #decir que introduzca una palabra
        intento = input("Introduce una palabra:")
        #sirve para una condición
        if (palabra == intento):
                ganar = True 
                #print, sirve para imprimir 
                print(f"{intento}, es la solucion correcta")
                #break, sirve para saltar a otra linea
                break
        #si no haz....
        else: 
                print("Has fallado, intentalo de nuevo")
if(ganar == True):
        print("Enhorabuena, has ganado")
else:
        print("Has agotado todos tus intentos")