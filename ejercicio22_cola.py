# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre
# del personaje, el nombre del superhéroes y su género (Masculino M y Femenino F) -por ejemplo 
#{Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombres de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S.
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from colas import Cola

class Superheroe:
    def __init__(self, persona, personaje, genero):
        self.persona = persona
        self.personaje = personaje
        self.genero = genero

cola = Cola()

superheroe1 = Superheroe("Tony Stark", "Iron Man", "M")
superheroe2 = Superheroe("Steve Rogers", "Capitán América", "M")
superheroe3 = Superheroe("Natasha Romanoff", "Black Widow", "F")
superheroe4 = Superheroe("Thor Odinson", "Thor", "M")
superheroe5 = Superheroe("Bruce Banner", "Hulk", "M")
superheroe6 = Superheroe("Peter Parker", "Spider-Man", "M")
superheroe7 = Superheroe("Carol Danvers", "Capitana Marvel", "F")
superheroe8 = Superheroe("T'Challa", "Black Panther", "M")
superheroe9 = Superheroe("Scott Lang", "Ant-Man", "M")
superheroe10 = Superheroe("Wanda Maximoff", "Bruja Escarlata", "F")
superheroe11 = Superheroe("Stephen Strange", "Doctor Strange", "M")
superheroe12 = Superheroe("Loki Laufeyson", "Loki", "M")

superheroes = [superheroe1, superheroe2, superheroe3, superheroe4, superheroe5, superheroe6, superheroe7, superheroe8, superheroe9, superheroe10, superheroe11, superheroe12]

for i in superheroes:
    cola.arrive(i)

def barrido(): # Realiza barrido:
    contador = 0
    while cola.size() > contador:
        valor = cola.on_front()
        print(valor.personaje)
        cola.move_to_end()
        contador += 1

def info(dato): # Devuelve alter-ego
    contador = 0
    while cola.size() > contador:
        valor = cola.on_front()
        if valor.personaje == dato: 
            return valor.persona
        if valor.persona == dato:
            return valor.personaje
        cola.move_to_end()
        contador += 1
    return False

def bloque1(): # Bloque de ejecución consignas a, d y f.
    print("Ingrese nombre del personaje o de la persona para saber su alter-ego: ")
    name = input()
    result = info(name)
    if result:
        print(f"{name} es:", end=" ")
        print(info(name))
    else:
        print("El personaje no se encuentra en la lista.") 

def personajes_genero(g): # Devuelve personajes por género
    contador = 0
    while cola.size() > contador:
        valor = cola.on_front()
        if valor.genero == g:
            print(valor.persona, "es", valor.personaje)
        cola.move_to_end()
        contador += 1

def bloque2(): # Bloque consigna b y c
    print("Presione F si desea ver los personajes femeninos y M si desea ver los masculinos: ")
    genero = input()
    print(f"Los nombres de los personajes de género {genero} son: ")
    personajes_genero(genero)

def letra_s(): # Personas y Personajes que comiencen con la letra S.
    contador = 0
    while cola.size() > contador:
        valor = cola.on_front()
        if valor.personaje[0] == "S":
            print("Personaje:", valor.personaje)
        if valor.persona[0] == "S":
            print("Persona:", valor.persona)
        cola.move_to_end()
        contador = contador + 1

def bloque3(): # Consigna e.
    print("Personajes y personas de Marvel que comienzan con la letra S: ")
    letra_s()


#bloque1()
#bloque2()
#bloque3()


