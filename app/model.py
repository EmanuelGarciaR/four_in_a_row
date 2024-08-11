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

dimension = Dimension(4)
board= Board(dimension)
print(board)
