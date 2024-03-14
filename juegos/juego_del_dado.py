def juego_del_dado():
    from random import randint as ibai
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    yo = 0 ; gpt = 0
    while True:
        temp0 = input()


        temp1 = ibai(1, 6)
        yo += temp1
        print('llevas', yo)
        if yo >= 30:
            print('AAAAAAAAAAAAAAAAAA')
            print('winner winner chicken dinner')
            break


        temp1 = ibai(1, 6)
        gpt += temp1
        print('lleva', gpt)
        if gpt >= 30:
            print('NOOOOOOOOOOOOOOOOOOO')
            print('como pierdes contra chat gpt wn')
            break
    pass