# Dada una cola con las notificaciones de las aplicaciones de un Smartphone,
# de la cual se cuenta con la hora de la notificación, la aplicación que la emitió 
# y el mensaje, resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook.
# b. escribir una funcion que muestre todas las notificaciones de Twitter, 
# cuyo mensaje incluya la palabra "Python", sin perder datos en la cola;
# c. utilizar una pila para almacenar temporareamente las notificaciones producidas
# entre las 11:43 y las 15:57, y determinar cuántas son

from colas import Cola
from stack import Stack

class Notificacion:
    def __init__(self, emite, hora, mensaje):
        self.emite = emite
        self.hora = hora
        self.mensaje = mensaje

cola = Cola()
pila = Stack()

notificacion1 = Notificacion("Facebook", 1340, "Sócrates te ha seguido")
notificacion2 = Notificacion("Twitter", 1431, "Elon Musk te ha retwitteado")
notificacion3 = Notificacion("Twitter", 1467, "Python vs JAVA")
notificacion4 = Notificacion("Duolingo", 501, "Es tiempo de practicar!" )
notificacion5 = Notificacion("Facebook", 1556, "Nietzsche te ha bloquado")
notificacion6 = Notificacion("Twitter", 1215, "Python: nueva actualización")


notificaciones = [notificacion1, notificacion2, notificacion3, notificacion4, notificacion5, notificacion6]

def cargar():
    for n in notificaciones:
        cola.arrive(n)

def barrido():
    contador = 0
    while cola.size() > contador:
        noti = cola.move_to_end()
        print(noti.emite, noti.hora, noti.mensaje)
        contador = contador + 1

def byebyefacebook():
    contador = 0
    tamanio = cola.size()
    while tamanio > contador:
        noti = cola.on_front()
        if noti.emite == "Facebook":
            cola.atention()
        else:
            cola.move_to_end()
        contador = contador + 1

def filtro_twitter():
    contador = 0
    while cola.size() > contador:
        noti = cola.on_front()
        if noti.emite == "Twitter" and "Python" in noti.mensaje:
            print(noti.emite, noti.hora, noti.mensaje)
            cola.move_to_end()
        cola.move_to_end()
        contador = contador + 1

def almacenar():
    contador = 0
    contadorh = 0
    tamanio = cola.size()
    while tamanio > contador:
        noti = cola.on_front()
        if noti.hora >= 1143 and noti.hora <= 1557:
            contadorh = contadorh + 1
            pila.push(noti)
            cola.atention()
        else: 
            cola.move_to_end()
        contador = contador + 1
    print(contadorh)

def barrido_pila():
    while pila.size() > 0:
        valor = pila.pop()
        print(valor.emite, valor.hora, valor.mensaje)

def bloque1():
    cargar()
    barrido()
    print()
    byebyefacebook()
    barrido()

def bloque2():
    cargar()
    barrido()
    print()
    print("Notificaciones de Twitter con la palabra Python:")
    filtro_twitter()
    print()

def bloque3():
    cargar()
    barrido()
    print()
    print("La cantidad de notificaciones que responden a ese horario es de: ")
    almacenar()
    print("No responden: ")
    barrido()
    print()
    print("Responden: ")
    barrido_pila()

bloque1()
bloque2()
bloque3()
