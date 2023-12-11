import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Minesweeper")


        self.label = tk.Label(self.root, text="Dim size", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox1 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox1.pack(padx=150, pady=10)

        self.label = tk.Label(self.root, text="Num Bomb", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox2 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox2.pack(padx=150, pady=10)

        self.clearbtn = tk.Button(self.root, text="GO", font=("Arial", 18), command=self.start_game)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def start_game(self):
        res1 = int((self.textbox1.get("1.0", tk.END)))
        res2 = int((self.textbox2.get("1.0", tk.END)))
        self.root.destroy()
        return res1, res2

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()



MyGUI()
print(res2)
print(res1)