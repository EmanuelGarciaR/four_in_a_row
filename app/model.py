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

    def put_token(self, player: str, column: int):
        if not (0 <= column < self.dimensions):
            raise ValueError("Posición fuera de los límites del tablero")

        for row in range(self.dimensions - 1, -1, -1):
            if self.matriz[row][column] == '-':  # Encontrar la primera posición vacía
                self.matriz[row][column] = player
                return

            # Si llegamos aquí, la columna está llena
        raise ValueError("La columna está llena. No se puede colocar la ficha.")