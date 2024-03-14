from random import randint as rand
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    a = '¡'
    while a != b:
        b = rand(1,10)
        print('adivina bro')
        a = int(input())
        if a == b:
            print('w chat')
        else:
            print('a comer')
            print('el numero era', b)
    pass
