from random import randint
def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    number = randint(1,10)
    print('Elige, par o impar...')
    eleccion = str(input())
    if eleccion == 'par':
        if number % 2 == 0:
            print('ADIVINASTE!!')
        else:
            print('Es impar :(')
    elif eleccion == 'impar':
        if number % 2 != 0:
            print('ADIVINASTE!!')
        else:
            print('Era par ;(')
