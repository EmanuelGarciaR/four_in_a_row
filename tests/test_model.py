import pytest
import numpy as np
from app.model import Dimension, Board  # Asegúrate de que la ruta sea correcta

@pytest.fixture
def board():
    """Crea una instancia del tablero con dimensiones 4x4."""
    dimension = Dimension(4)
    return Board(dimension)

def test_initial_board(board):
    """Verifica que el tablero inicial esté lleno de '-'."""
    expected = np.full((4, 4), '-')
    np.testing.assert_array_equal(board.matriz, expected)

def test_put_token_valid(board):
    """Coloca una ficha en una columna válida y verifica la colocación."""
    board.put_token('X', 2)
    expected = np.array([
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', 'X', '-']
    ])
    np.testing.assert_array_equal(board.matriz, expected)

def test_put_token_out_of_bounds(board):
    """Intenta colocar una ficha en una columna fuera de los límites y verifica que se lance una excepción."""
    with pytest.raises(ValueError):
        board.put_token('X', 5)

def test_put_token_column_full(board):
    """Llena una columna y verifica que no se pueda colocar una ficha adicional en una columna llena."""
    for _ in range(4):  # Rellenar la columna
        board.put_token('X', 2)
    # Intentar colocar una ficha adicional en una columna llena
    with pytest.raises(ValueError):
        board.put_token('O', 2)

def test_put_token_on_occupied(board):
    """Intenta colocar una ficha en una posición ya ocupada y verifica que se maneje correctamente."""
    board.put_token('X', 2)
    with pytest.raises(ValueError):
        board.put_token('O', 2)

def test_show_board_output(board):
    """Verifica la salida del método show_board."""
    import io
    import sys
    captured_output = io.StringIO()    # Crear un buffer para capturar la salida
    sys.stdout = captured_output        # Redirigir stdout al buffer
    board.show_board()                # Llamar al método que genera la salida
    sys.stdout = sys.__stdout__         # Restaurar stdout a su estado original
    expected_output = "///BOARD///\n- - - -\n- - - -\n- - - -\n- - - -\n"
    assert captured_output.getvalue() == expected_output
