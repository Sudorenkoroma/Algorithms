import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.menubar = tk.Menu(self.root)

        # self.root.geometry("500x500")
        # self.root.title("My first GUI")

        self.label = tk.Label(self.root, text="Num desk", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.textbox1 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox1.pack(padx=200, pady=10)

        self.label = tk.Label(self.root, text="Num bomb", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.textbox2 = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox2.pack(padx=200, pady=10)

        self.button = tk.Button(self.root, text="GO", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.root.mainloop()

    def show_message(self):
        pass



        self.buttonframe.pack(fill="x")


        # myentry = tk.Entry(root)
        # myentry.pack()

MyGUI()
