import tkinter as tk

class InputsPage(tk.Frame):
    def __init__(self, parent):
            super().__init__(parent)
            tk.Label(self, text = "Inputs Page").pack(padx = 10, pady = 10)
            self.pack(padx = 10, pady = 10)