import tkinter as tk
from .MainMenuPage import MainMenuPage
from .InputsPage import InputsPage
from .ResultsPage import ResultsPage

# Background parent page of every concrete page
class ContainerPage():
    def __init__(self, master):
        container = tk.Frame(master)

        # background elements
        container["bg"] = "tan"
        container.pack(side="top", fill="both", expand=True)
        container.pack(padx=10, pady=10, fill='both', expand=1)

        # list that creates ands hold the concrete pages
        self.pages_list = []
        self.pages_list.append(MainMenuPage(container, self))
        self.pages_list.append(InputsPage(container))
        self.pages_list.append(ResultsPage(container))
        self.pages_list[1].forget()
        self.pages_list[2].forget()

        #sets current visible concrete page
        self.current_page = 0
        self.pages_list[self.current_page].tkraise()
        self.pages_list[self.current_page].pack(padx = 10, pady = 10)


    # switches the visible page to the page at index new_page in pages_list
    def switch_to_page(self, new_page):
        self.pages_list[self.current_page].forget()
        self.current_page = new_page
        self.pages_list[new_page].tkraise()
        self.pages_list[new_page].pack(padx = 10, pady = 10)

    # # TODO: overload switch_to_page to allow dictionary variable
    # def switch_to_page(self, new_page, dict):
    #     self.pages_list[self.current_page].forget()
    #     self.current_page = new_page
    #     self.pages_list[new_page].tkraise()
    #     self.pages_list[new_page].pack(padx = 10, pady = 10)

