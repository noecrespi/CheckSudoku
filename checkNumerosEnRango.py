def checkNumerosEnRango(matriz):
    """ 
    comprovar que los numeros en la matriz esten del 1 a n (al número de columnas o o filas, 
    tamaño de la matriz)
    """

    n = len(matriz)
    for fila in matriz:
        for numero in fila:
            if not (1 <= numero and numero <= n):
                return False
    
    return True


if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkNumerosEnRango(CASO))