class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.score = 0

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
    
    def draw(self):
        header = " ".join(f"{i+1:^3}" for i in range(self.size))
        print(header)
        for row in self.board:
            print(" | ".join(row).center(len(header)))
            print("-" * len(header))

    def make_move(self, column, token):
        column -= 1
        if column < 0 or column >= self.size:
            return False, "Columna fuera de rango."
        for row in reversed(self.board):
            if row[column] == ' ':
                row[column] = token
                return True, None
        return False, "Columna llena."

    def check_winner(self, token):
        for row in range(self.size):
            if self.check_line([self.board[row][col] for col in range(self.size)], token):
                return True
        for col in range(self.size):
            if self.check_line([self.board[row][col] for row in range(self.size)], token):
                return True
        for row in range(self.size - 3):
            for col in range(self.size - 3):
                if (self.check_line([self.board[row + i][col + i] for i in range(4)], token) or
                    self.check_line([self.board[row + i][col + 3 - i] for i in range(4)], token)):
                    return True
        for row in range(3, self.size):
            for col in range(self.size - 3):
                if self.check_line([self.board[row - i][col + i] for i in range(4)], token):
                    return True
        return False

    def check_line(self, line, token):
        count = 0
        for cell in line:
            if cell == token:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def check_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

class Game:
    def __init__(self):
        self.players = []
        self.board_size = 0
        self.num_games = 0
    
    def valid_name(self, name):
        # Verifica si el nombre es válido
        invalid_names = ["None", "True", "False", ""]
        if name in invalid_names or not name.isalpha():
            return False
        return True
    
    def setup(self):
        # Configuración del juego, incluyendo nombres y parámetros
        while True:
            name1 = input("Ingrese el nombre del jugador 1: ")
            if self.valid_name(name1):
                break
            print("Nombre invalido. Por favor ingrese otro nombre.")
        
        while True:
            name2 = input("Ingrese el nombre del jugador 2: ")
            if self.valid_name(name2) and name2 != name1:
                break
            print("Nombre invalido. Por favor ingrese otro nombre.")
        
        self.players.append(Player(name1, 'X'))
        self.players.append(Player(name2, 'O'))
        
        while True:
            try:
                self.board_size = int(input("Ingrese el tamaño del tablero (4 o 6): "))
                if self.board_size not in [4, 6]:
                    raise ValueError
                break
            except ValueError:
                print("Tamaño invalido. ingrese 4 o 6.")
        
        while True:
            try:
                self.num_games = int(input("Al mejor de (1, 3, 5, 7, 9): "))
                if self.num_games not in [1, 3, 5, 7, 9]:
                    raise ValueError
                break
            except ValueError:
                print("Numero invalido. Por favor ingrese 1, 3, 5, 7, o 9.")
    
    def play_game(self):
        played_games = 0
        max_wins_needed = (self.num_games // 2) + 1

        while played_games < self.num_games:
            mesa = Board(self.board_size)
            current_player = 0
            while True:
                mesa.draw()
                move = input(f"Movimiento de {self.players[current_player].name} (1-{self.board_size}): ")
                
                # Verifica que el movimiento sea un número y dentro del rango
                if not move.isdigit():
                    print("Número inválido. Por favor ingrese otro número.")
                    continue
                move = int(move)
                valid, error = mesa.make_move(move, self.players[current_player].token)
                if not valid:
                    print(error)
                    continue
                if mesa.check_winner(self.players[current_player].token):
                    mesa.draw()
                    print(f"{self.players[current_player].name} Ganó!")
                    self.players[current_player].score += 1
                    played_games += 1
                    break
                if mesa.check_draw():
                    print("Empate!")
                    played_games += 1
                    break
                current_player = 1 - current_player
            
            # Comprobar ganador general
            if self.players[0].score >= max_wins_needed or self.players[1].score >= max_wins_needed:
                break
            # Mostrar puntajes después de cada juego
            self.show_scores()

        self.show_final_winner()

    def show_scores(self):
        print("\nPuntaje actual:")
        for player in self.players:
            print(f"{player.name}: {player.score}")
    
    def show_final_winner(self):
        print("\nPuntaje final:")
        for player in self.players:
            print(f"{player.name}: {player.score}")
        winner = max(self.players, key=lambda p: p.score)
        print(f"\n🎉🎈 ¡Felicitaciones {winner.name}! 🎈🎉\n")
        print("🎈🎉🎈🎉🎈🎉🎈🎉🎈🎉🎈🎉")
        print("🎉🎈 ¡Gracias por jugar! 🎈🎉")

if __name__ == "__main__":
    juego = Game()
    juego.setup()
    juego.play_game()