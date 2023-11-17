from cola_prioridad import ColaPrioridad

# 16_ Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

cola= ColaPrioridad()

def ejercicio_a():
    empleados=[{'nombre':'Aolo','prioridad': 1},
            {'nombre':'Patroclo','prioridad': 1},
            {'nombre':'Neon','prioridad': 1}]

    for i in empleados:
        cola.arrive(i['nombre'],i['prioridad'])

def ejercicio_b():
    print(cola.atention()[1])

def ejercicio_c():
    empleados=[{'nombre':'Gabril Jesus','prioridad':2},
            {'nombre':'Firminho','prioridad':2}]

    for i in empleados:
        cola.arrive(i['nombre'],i['prioridad'])

def ejercicio_d():
    empleados=[{'nombre':'Tiago Alcántara','prioridad':3}]

    for i in empleados:
        cola.arrive(i['nombre'],i['prioridad'])

def ejercicio_e():
    for i in range(2):
        print(cola.atention()[1])

def ejercicio_f():
    empleados=[{'nombre':'Teo','prioridad':1},
            {'nombre':'Yoda','prioridad':1},
            {'nombre':'Obi','prioridad':3}]

    for i in empleados:
        cola.arrive(i['nombre'],i['prioridad'])

def ejercicio_g():
    while cola.size()>0:
        print(cola.atention()[1])

ejercicio_a()
print()
ejercicio_b()
print()
ejercicio_c()
print()
ejercicio_d()
print()
ejercicio_e()
print()
ejercicio_f()
print()
ejercicio_g()