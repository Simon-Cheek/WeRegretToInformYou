import tkinter as tk

class ResultsPage(tk.Frame):
    def __init__(self, parent):
            super().__init__(parent)
            tk.Label(self, text = "Results Page").pack(padx = 10, pady = 10)
            self.pack(padx = 10, pady = 10)