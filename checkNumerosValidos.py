from checkNumerosEnRango import checkNumerosEnRango
from checkNumerosEnteros import checkNumerosEnteros


def checkNumerosValidos(matriz):
    """
    Comprobaremos que son numeros enteros
    y que los numeros esten en el rango 1-n (n = numero de casillas). 
    """
    # comprobar "checkNumerosEnteros" y "checkNumerosEnRango"
    return checkNumerosEnteros(matriz) and checkNumerosEnRango(matriz)


if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkNumerosValidos(CASO))