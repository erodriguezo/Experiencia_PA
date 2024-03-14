from random import randint
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    print('Elige: piedra, papel o tijera')
    winner = ''
    while winner == '':
        maquina = randint(1, 3)
        eleccion = str(input())
        if eleccion == 'piedra':
            if maquina == 2:
                winner = 'maquina'
                print('Perdiste, la maquina sacó papel')
            elif maquina == 3:
                winner = 'usuario'
                print('Ganaste!! La maquina sacó tijera')
        elif eleccion == 'papel':
            if maquina == 1:
                winner = 'usuario'
                print('Ganaste!! La maquina sacó piedra')
            elif maquina == 3:
                winner = 'maquina'
                print('Perdiste, la maquina sacó tijera')
        elif eleccion == 'tijera':
            if maquina == 1:
                winner = 'maquina'
                print('Perdiste, la maquina sacó piedra')
            elif maquina == 2:
                winner = 'usuario'
                print('Ganaste!! La maquina sacó tijera')
        if winner == '':
            print('Es un empate, elige de nuevo: piedra, papel o tijera')

