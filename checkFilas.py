"""
    comprobar que no haya numeros repetidos en las filas
"""

def checkFilas(matriz):
    for fila in matriz:
        for numero in fila:
            if fila.count(numero) > 1:
                return False
            
    return True

if __name__ == '__main__': # solo se ejecuta, si este es el archivo principal
    from tests import CASOS_TEST # nos traemos del modulo 'tests.py' la variable 'CASOS_TEST'
    for CASO in CASOS_TEST:
        print(CASO, checkFilas(CASO))