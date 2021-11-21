def checkNumerosEnteros(matriz):
    """ 
    Comprobar que todo sean numeros enteros

    [
        [kakdw]
        []
    ]
    """

    # para cada fila dentro matriz
    for fila in matriz:
        # fila = [1,2,3,4]
        # para cada numero dentro de fina
        for numero in fila:
            # si el numero NO es entero
            # isintance = comprueba que el primer argumento es intstacia (heredado, hijo de) el segundo argumento
            if not isinstance(numero, int):
                return False
            
    return True


if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkNumerosEnteros(CASO))