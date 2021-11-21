""" 
Problema:
    el numero de las casillas horizontal o 
    casillas verticales no puede der mayor al num de casillas
"""
# from <modulo/archivo(.py)> import <variables/funciones/constantes>
# desde el modulo importame: ...
from CheckColumnas import checkColumnas
from checkCuadrado import esCuadrado
from checkFilas import checkFilas
from checkNumerosValidos import checkNumerosValidos

def checkSudoku (sudoku):
    """
    Comprueba si un sudoku (matriz) sigue las normas del juego
    """
    # comprueba "checkCuadrado", "checkNumerosValidos", "checkFilas" y "checkColumnas"
    return esCuadrado(sudoku) and checkNumerosValidos(sudoku) and checkFilas(sudoku) and checkColumnas(sudoku)


if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkSudoku(CASO))