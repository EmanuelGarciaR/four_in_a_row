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
        # Ajustar el índice de la columna para que sea 0 basado
        column -= 1
        self._validate_column(column)
        row = self._find_empty_row(column)
        if row is not None:
            if self.matriz[row][column] != '-':
                raise ValueError("La posición ya está ocupada.")
            self.matriz[row][column] = player
        else:
            raise ValueError("La columna está llena. No se puede colocar la ficha.")

    def _validate_column(self, column: int):
        """Valida si la columna está dentro de los límites del tablero."""
        if not (0 <= column < self.dimensions):
            raise ValueError("Posición fuera de los límites del tablero")

    def _find_empty_row(self, column: int):
        """Encuentra la primera fila vacía en la columna especificada."""
        for row in range(self.dimensions - 1, -1, -1):
            if self.matriz[row][column] == '-':
                return row
        return None

    def check_winner(self, player: str):
        if not self._enough_token():
            raise ValueError("No hay suficientes fichas en el tablero para verificar la victoria.")

        # Verificar horizontalmente
        for row in range(self.dimensions):
            for col in range(self.dimensions - 3):  # Verificar hasta la columna - 3
                if all(self.matriz[row][col + i] == player for i in range(4)):
                    return True

        # Verificar verticalmente
        for col in range(self.dimensions):
            for row in range(self.dimensions - 3):  # Verificar hasta la fila - 3
                if all(self.matriz[row + i][col] == player for i in range(4)):
                    return True

        # Verificar diagonal de arriba a abajo
        for row in range(self.dimensions - 3):
            for col in range(self.dimensions - 3):
                if all(self.matriz[row + i][col + i] == player for i in range(4)):
                    return True

        # Verificar diagonal de abajo a arriba
        for row in range(3, self.dimensions):
            for col in range(self.dimensions - 3):
                if all(self.matriz[row - i][col + i] == player for i in range(4)):
                    return True

        return False

    def _enough_token(self):
        #Verificar si hay almenos 4 fichas
        total_token = np.sum(self.matriz != '-')
        return total_token >= 4

    def check_draw(self):
        if (self.check_winner('X') and self.check_winner('O')) and np.all(self.matriz != '-'):
            return "El juego ha terminado en empate."

        # Si el tablero no está lleno, el juego no ha terminado en empate
        return "El juego no ha terminado en empate."
