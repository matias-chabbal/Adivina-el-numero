from random import *
import os


"""cramos una funcion y le pasamos como parametro el numero que el sistema elijio
y el nombre del usuario."""
def jugar(numero, user):
    vidas = 8
    oportunidades = 0
    #establecemos la variable ganaste en falso como primer indicador para que el juego finalice.
    ganaste = False
    print('ingresar numero...')
    print(numero)
    #bucle que se ejecuta siempre que las vidas no se acaben o que la variable ganaste cambie.
    while (vidas > 0) and (ganaste == False):
        #obtenemos un valor del usuario
        intento = int(input(f'{user}: '))
        """
        pueden pasar 3 cosas.
        1- si el numero que se ingreso esta fuera de la condicion establecida el bucle continua.
        2- si el numero es menor o mayor al numero que elijio el sistema se le hace saber al usuario y se resta una vida.
        3- la tercera opcion es si el numero coincide, se le avisa al usuario que gano y termina el bucle.
        """
        if intento > 10 or intento < 1:
            print('numero no valido, debe ser un numero entre el 1 y el 10.')
        elif intento < numero:
            print('mi numero es mas alto.')
            vidas -= 1
            oportunidades += 1
            print(f'te quedan {vidas} vidas.')
        elif intento > numero:
            print('mi numero es mas bajo.')
            vidas -= 1
            oportunidades += 1
            print(f'te quedan {vidas} vidas.')
        else:
            print('GANASTE!!!')
            print(f'el numero que elegi era el {numero}, lo adivinaste en {oportunidades + 1} intentos.')
            ganaste = True
            input('presiona enter para volver al menu...')
            os.system('cls')
    #si el numero de vidas queda en cero el usuario perdio y termina el bucle.
    if vidas == 0:
        print('te quedaste sin vidas. PERDISTE!!!')


"""en esta funcion nos ayudamos de la libreria random para que el sistema obtenga un numero aleatorio."""
def elegir_numero(user):
    #obtenemos un numero aleatorio del 1 al 10.
    numero = randint(1,10)
    #llamamos a la funcion de jugar para comenzar el juego.
    jugar(numero, user)

"""funcion para obtener el nombre del usuario y le hacemos saber al usuario las reglas."""
def nombre():
    user = input('ingresar nombre: ')
    print(f'{user} tienes 8 intentos para adivinar el numero que elegi del 1 al 10.')
    input('presionar enter para continuar...')
    #borramos la consola.
    os.system('cls')
    #llamamos a la funcion para obtener un numero aleatorio del sistema.
    elegir_numero(user)

#menu principal para iniciar el juego o salir del programa.
salir = False
while not salir:
    print('1- iniciar juego.')
    print('2- salir.')
    opcion = int(input('ingresar opcion: '))
    
    match opcion:
        case 1:
            nombre()
        case 2:
            salir = not salir
