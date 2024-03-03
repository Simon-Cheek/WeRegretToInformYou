from Pages.ContainerPage import ContainerPage
import tkinter as tk


# Creates initial window for game
def start_pages():
    root = tk.Tk()
    root.title("We Regret to Inform You")
    root.minsize(980, 720)
    global container_page
    container_page = ContainerPage(root)
    output_main_menu()
    root.mainloop()

# Switches to given page
def output_main_menu():
        container_page.switch_to_page(0)

def output_inputs():
    container_page.switch_to_page(1)

def switch_to_results(messages):
         container_page.switch_to_page(2)

#