import numpy as np


class Dimension:
    def __init__(self, dimension: int):
        if dimension not in [4, 5, 6]:  # Verificar dimensión en el rango permitido
            raise ValueError("Dimensión no permitida. Debe ser 4, 5 o 6.")
        self.dimension = dimension


class Board:

    def __init__(self, dimensions: Dimension):
        self.dimensions = dimensions.dimension
        self.matriz = np.full((self.dimensions, self.dimensions), '-')

    def __str__(self):
        return f"///BOARD///\n{self.matriz}\n(Dimension = {self.dimensions})"

    def show_board(self):
        if self.matriz is None:
            raise ValueError("El tablero está vacío.")
        print("///BOARD///")
        for fila in self.matriz:
            print(' '.join(fila))

    def put_token(self, player: str, row: int, column: int):
        if not (0 <= row <= self.dimensions and 0 <= column <= self.dimensions):
            raise ValueError("Posición fuera de los límites del tablero")
        if self.matriz[row-1][column-1] != '-':
            raise ValueError("La posición ya está ocupada.")
        self.matriz[row-1][column-1] = player


dimension = Dimension(4)
board = Board(dimension)

#====TESTS=====
#Mostrar el tablero inicial:
board.show_board()

# Colocar una ficha en una posición válida
print("\nColocando ficha en (2, 2):")
board.put_token('X', 2, 2)
board.show_board()

# Intentar colocar una ficha en una posición fuera de los límites
try:
    print("\nIntentando colocar ficha en posición inválida (5, 3):")
    board.put_token('O', 5, 3)
except ValueError as e:
    print(f"Error: {e}")

# Intentar colocar una ficha en una posición ya ocupada
try:
    print("\nIntentando colocar ficha en posición ocupada (2, 2):")
    board.put_token('O', 2, 2)
except ValueError as e:
    print(f"Error: {e}")
