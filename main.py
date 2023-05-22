import tkinter as tk
from square import Square


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("El tres en raya")

        # Crear los cuadrados del tres en raya
        self.squares = [[Square() for _ in range(3)] for _ in range(3)]

        # Variable para rastrear el turno del jugador
        self.current_player = "X"

        # Variable para contar el número de movimientos
        self.move_count = 0

        # Mostrar la ventana
        self.create_board()
        self.root.mainloop()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                square = self.squares[row][col]
                button = tk.Button(self.root, text=square.get_value(), width=10, height=5,
                                   font=("Helvetica", 20),
                                   fg="red",
                                   bg="white",
                                   command=lambda r=row, c=col: self.square_click(r, c))
                button.grid(row=row, column=col)

    def square_click(self, row, col):
        square = self.squares[row][col]
        if not square.get_value():  # Verificar si el cuadrado está vacío
            # Establecer el valor del cuadrado al jugador actual
            square.set_value(self.current_player)
            button = self.root.grid_slaves(row=row, column=col)[0]
            button.config(text=square.get_value())
            self.move_count += 1
            self.check_winner()
            self.change_player()

    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        # Comprobar todas las posibles combinaciones ganadoras
        winning_combinations = [
            [[0, 0], [0, 1], [0, 2]],  # Fila 1
            [[1, 0], [1, 1], [1, 2]],  # Fila 2
            [[2, 0], [2, 1], [2, 2]],  # Fila 3
            [[0, 0], [1, 0], [2, 0]],  # Columna 1
            [[0, 1], [1, 1], [2, 1]],  # Columna 2
            [[0, 2], [1, 2], [2, 2]],  # Columna 3
            [[0, 0], [1, 1], [2, 2]],  # Diagonal principal
            [[0, 2], [1, 1], [2, 0]]   # Diagonal secundaria
        ]

        for combination in winning_combinations:
            values = [self.squares[row][col].get_value()
                      for row, col in combination]
            if all(value == "X" for value in values):
                self.game_over("X")
                return
            elif all(value == "O" for value in values):
                self.game_over("O")
                return

        if self.move_count == 9:
            self.game_over("Empate")

    def game_over(self, winner):
        self.root.destroy()
        message = ""
        if winner == "Empate":
            message = "¡Empate! No hay ganadores."
        else:
            message = f"¡Fin del juego! El jugador {winner} ha ganado."

        # Crear una nueva ventana para mostrar el mensaje
        result_window = tk.Tk()
        result_window.title("Resultado")
        result_label = tk.Label(
            result_window, text=message, font=("Helvetica", 18))
        result_label.pack(padx=20, pady=20)
        result_window.mainloop()


game = TicTacToe()
