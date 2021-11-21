"""
    comprobar que no haya numeros repetidos en las filas
"""

from checkFilas import checkFilas


def checkColumnas(matriz):
    matrizInvertida = [[] for _ in matriz]
    for fila in matriz:
        for columna, num in enumerate(fila):
            matrizInvertida[columna].append(num)
    return checkFilas(matrizInvertida)

if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkColumnas(CASO))