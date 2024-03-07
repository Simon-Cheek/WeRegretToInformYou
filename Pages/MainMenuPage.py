import tkinter as tk

class MainMenuPage(tk.Frame):
    def __init__(self, parent,container_page):
            super().__init__(parent)
            # tk.Label(self, text = "Main Menu Page").pack(padx = 10, pady = 10)
            tk.Label(self, text = "Main Menu").pack(padx = 10, pady = 10)
            # tk.Button(self, text='to Inputs', width=25, command=container_page.switch_to_page(1)).pack(padx = 10, pady = 10)
            self.pack(padx = 10, pady = 10)