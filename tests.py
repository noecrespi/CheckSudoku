#  \  =  salto de linea, añadimos ese simbolo para indicar que la line continua abajo
CASOS_TEST = \
[
    # CASO TEST 1 == CORRECTO
    [[ 1 , 2 , 3 ],
    [ 2 , 3 , 1 ],
    [ 3 , 1 , 2 ]],

    # CASO TEST 2 == INCORRECTO
    [[ 1 , 2 , 3 , 4 ],
    [ 2 , 3 , 1 , 3 ],
    [ 3 , 1 , 2 , 3 ],
    [ 4 , 4 , 4 , 4 ]],

    # CASO TEST 3 == INCORRECTO
    [[ 1 , 2 , 3 , 4 ],
    [ 2 , 3 , 1 , 4 ],
    [ 4 , 1 , 2 , 3 ],
    [ 3 , 4 , 1 , 2 ]],

    # CASO TEST 4 == INCORRECTO
    [[ 1 , 2 , 3 , 4 , 5 ],
    [ 2 , 3 , 1 , 5 , 6 ],
    [ 4 , 5 , 2 , 1 , 3 ],
    [ 3 , 4 , 5 , 2 , 1 ],
    [ 5 , 6 , 4 , 3 , 2 ]],

    # CASO TEST 5 == INCORRECTO
    [[ 'a' , 'b' , 'c' ],
    [ 'b' , 'c' , 'a' ],
    [ 'c' , 'a' , 'b' ]],

    # CASO TEST 6 == INCORRECTO
    [[ 1 , 1.5 ],
    [ 1,5 , 1 ]],

    # CASO TEST 7 == INCORRECTO
    [[ 1 , 0 , 0 , 0 ],
    [ 0 , 1 , 0 ],
    [ 0 , 0 , 0 , 1 ]]
]