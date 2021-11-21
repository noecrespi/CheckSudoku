def esCuadrado(matriz):
    """
    Devuelve True o False

    Comprueba si la matriz es cuadrada (n x n)

    matriz:
    __c1__c2__c3_
    | 1 | 2 | 3 | fila 1
    | 2 | 3 | 1 | fila 2
    | 3 | 1 | 2 | fila 3
    -------------

    sudoku:
    aqui empieza la matriz[
        esto es una fila [f1c1, f1c2, f1c3],
        esto es una fila [f2c1, f2c2, f2c3],
        esto es una fila [f3c1, f3c2, f3c3]
    aqui acaba la matriz]
    """
    numFilas = len(matriz)             # tamaño de la matriz

    # para cada fila dentro de la matriz
    for fila in matriz:
        #si el num de filas NO es igual al num de columnas 
        numColumnas = len(fila)
        if numFilas != numColumnas:
            return False

    return True



if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, esCuadrado(CASO))