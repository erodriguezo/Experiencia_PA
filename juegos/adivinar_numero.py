from random import randint as rand
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    a = '¡' ; b = 2389759278
    while a != b:
        print('adivina bro')
        b = rand(1, 10)
        a = int(input())
        if a == b:
            break
        else:
            print('a comer')
    return 'w chat'
