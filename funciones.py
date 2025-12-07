def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")

def fila_ganadora(tablero):
    for fila in tablero:
        cond = True
        pieza_1 = fila[0]
        for piezas in fila:
            if piezas == ' ' or pieza_1 != piezas:
                cond = False
        if cond:
            return True
    return False

def columna_ganadora(tablero):
    i = 0
    for fila in tablero:
        pieza_1 = fila[i]
        print(pieza_1 == tablero[1][1])
        i += 1
             




assert_equal(
    fila_ganadora(
        [
            ['A', 'A', 'B', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)
assert_equal(
    fila_ganadora(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
    ),
    True
)




assert_equal(
    columna_ganadora(
        [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['O', 'X', ' ']
        ]
    ),
    False
)
assert_equal(
    columna_ganadora(
        [
            ['X', 'O', ' ', 'X'],
            [' ', 'O', 'X', 'O'],
            ['O', 'O', 'X', 'X'],
            ['O', 'O', 'X', ' ']
        ]
    ),
    True
)