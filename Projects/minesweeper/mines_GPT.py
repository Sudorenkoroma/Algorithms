import tkinter as tk
from tkinter import messagebox
import random


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.root.title("Minesweeper")
        self.dim_size = None
        self.num_bombs = None

        self.label = tk.Label(self.root, text="Dim size", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox1 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox1.pack(padx=100, pady=10)

        self.label = tk.Label(self.root, text="Num Bomb", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox2 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox2.pack(padx=100, pady=10)

        self.clearbtn = tk.Button(self.root, text="GO", font=("Arial", 18), command=self.start_game)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def start_game(self):
        self.dim_size = int((self.textbox1.get("1.0", tk.END)))
        self.num_bombs = int((self.textbox2.get("1.0", tk.END)))
        self.root.destroy()
        root = tk.Tk()
        root.title("Minesweeper")
        MinesweeperGUI(root, self.dim_size, self.num_bombs)
        root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()



class MinesweeperGUI(MyGUI):
    def __init__(self, master, dim_size=0, num_bombs=0):

        self.master = master
        # self.root = tk.Tk()
        #
        # self.root.title("Minesweeper")
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.buttons = [[None for _ in range(dim_size)] for _ in range(dim_size)]

        self.setup_gui()
        self.count = 0

        # self.menubar = tk.Menu(self.root)
        # self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.filemenu.add_command(label="Close", command=None)
        #
        # self.menubar.add_cascade(menu=self.filemenu, label="file")
        # self.root.mainloop()
    def make_new_board(self):
        board = [[0 for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = (random.randint(0, self.dim_size - 1), random.randint(0, self.dim_size - 1))
            if board[loc[0]][loc[1]] == -1:
                continue
            board[loc[0]][loc[1]] = -1
            bombs_planted += 1
            for r in range(max(0, loc[0] - 1), min(self.dim_size - 1, loc[0] + 1) + 1):
                for c in range(max(0, loc[1] - 1), min(self.dim_size - 1, loc[1] + 1) + 1):
                    if board[r][c] != -1:
                        board[r][c] += 1
        return board

    def setup_gui(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                btn = tk.Button(self.master, text="", width=2, height=1, command=lambda r=row, c=col: self.dig(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def dig(self, row, col):
        if self.board[row][col] == -1:
            messagebox.showinfo("Game Over", "You hit a bomb! Game over.")
            self.reveal_board()
        elif self.board[row][col] > 0:
            self.buttons[row][col].config(text=str(self.board[row][col]))
            self.count += 1
        else:
            self.clear_empty_cells(row, col)

        if self.dim_size**2 == self.count + self.num_bombs:
            messagebox.showinfo("Game Over", "You WIN")
            self.reveal_board()

    def clear_empty_cells(self, row, col):
        if 0 <= row < self.dim_size and 0 <= col < self.dim_size and self.buttons[row][col]['state'] == 'normal':
            self.buttons[row][col].config(state='disabled', text=str(self.board[row][col]))
            self.count += 1
            if self.board[row][col] == 0:
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        self.clear_empty_cells(r, c)

    def reveal_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="*", state='disabled')



MyGUI()

