import pytest
import numpy as np
from app.model import Dimension, Board


#Dimension
def test_valid_dimension():
    """Verifica que una dimensión válida se acepte correctamente."""
    dimension = Dimension(4)
    assert dimension.dimension == 4


def test_invalid_dimension():
    """Verifica que una dimensión no válida lance una excepción."""
    with pytest.raises(ValueError):
        Dimension(3)


#BOARD
@pytest.fixture
def board():
    """Instancia del tablero con dimensiones 4x4."""
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
        ['-', 'X', '-', '-']
    ])
    np.testing.assert_array_equal(board.matriz, expected)


def test_put_token_out_of_bounds(board):
    """Intenta colocar una ficha en una columna fuera de los límites y verifica que se lance una excepción."""
    with pytest.raises(ValueError):
        board.put_token('X', 5)


def test_put_token_column_full(board):
    """Llena una columna y verifica que no se pueda colocar una ficha adicional en una columna llena."""
    for _ in range(4):  # Rellenar la columna (ajustado a columna 1)
        board.put_token('X', 2)  # Aquí '2' se ajusta internamente a columna 1
    # Intentar colocar una ficha adicional en una columna llena
    with pytest.raises(ValueError):
        board.put_token('O', 2)  # Aquí '2' también se ajusta internamente a columna 1


def test_show_board_output(board):
    """Verifica la salida del método show_board."""
    import io
    import sys
    captured_output = io.StringIO()  # Crear un buffer para capturar la salida
    sys.stdout = captured_output  # Redirigir stdout al buffer
    board.show_board()  # Llamar al método que genera la salida
    sys.stdout = sys.__stdout__  # Restaurar stdout a su estado original
    expected_output = "///BOARD///\n- - - -\n- - - -\n- - - -\n- - - -\n"
    assert captured_output.getvalue() == expected_output


#WINNER AND EMPTY
@pytest.fixture
def board_4x4():
    """Fixture para un tablero 4x4 vacío."""
    dimension = Dimension(4)
    return Board(dimension)


def test_check_winner_horizontal(board_4x4):
    """Prueba que detecta una victoria horizontal."""
    board_4x4.matriz[2] = ['X', 'X', 'X', 'X']
    assert board_4x4.check_winner('X') == True


def test_check_winner_vertical(board_4x4):
    """Prueba que detecta una victoria vertical."""
    board_4x4.matriz[0][1] = 'O'
    board_4x4.matriz[1][1] = 'O'
    board_4x4.matriz[2][1] = 'O'
    board_4x4.matriz[3][1] = 'O'
    assert board_4x4.check_winner('O') == True


def test_check_winner_diagonal_ascending(board_4x4):
    """Prueba que detecta una victoria diagonal ascendente."""
    board_4x4.matriz[3][0] = 'X'
    board_4x4.matriz[2][1] = 'X'
    board_4x4.matriz[1][2] = 'X'
    board_4x4.matriz[0][3] = 'X'
    assert board_4x4.check_winner('X') == True


def test_check_winner_diagonal_descending(board_4x4):
    """Prueba que detecta una victoria diagonal descendente."""
    board_4x4.matriz[0][0] = 'O'
    board_4x4.matriz[1][1] = 'O'
    board_4x4.matriz[2][2] = 'O'
    board_4x4.matriz[3][3] = 'O'
    assert board_4x4.check_winner('O') == True


def test_check_draw_full_board_no_winner(board_4x4):
    """Prueba que el juego detecta un empate cuando el tablero está lleno y no hay ganador."""
    board_4x4.matriz = np.array([
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X']
    ])
    print(f"Ganador X = {board_4x4.check_winner('X')}")
    print(f"Ganador Y = {board_4x4.check_winner('Y')}")
    print("Tablero para test de empate:\n", board_4x4.matriz)  # Verifica el estado del tablero
    result = board_4x4.check_draw()
    print("Resultado del test de empate:", result)  # Verifica el resultado
    assert result == "El juego ha terminado en empate."


def test_check_draw_not_full(board_4x4):
    """Prueba que el juego no detecta un empate cuando el tablero no está completamente lleno."""
    board_4x4.matriz = np.array([
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', '-'],
        ['X', 'O', 'X', 'O'],
        ['O', 'X', 'O', 'X']
    ])
    assert board_4x4.check_draw() == "El juego no ha terminado en empate."
