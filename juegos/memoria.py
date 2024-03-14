from random import randint
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    n1 = randint(1,100)
    n2 = randint(1,100)
    n3 = randint(1,100)
    n4 = randint(1,100)
    n5 = randint(1,100)
    print(f'Memoriza los siguientes numeros: {n1}/{n2}/{n3}/{n4}/{n5}\nCuando estes listo presiona enter')
    input()
    print('.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nEscribe los numeros en el orden en el que estaban:')
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    x5 = int(input())
    if n1==x1 and n2==x2 and n3==x3 and n4==x4 and n5==x5:
        print('BIENNNN!!!')
    else:
        print('Incorrecto:(((')


