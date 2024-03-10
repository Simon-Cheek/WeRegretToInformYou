import tkinter as tk
from tkinter import messagebox

from Jobs.BackEnd import BackEndJob
from Jobs.Generalist import GeneralistJob
from Jobs.Specialist import SpecialistJob
from Jobs.FrontEnd import FrontEndJob
from Jobs.FullStack import FullStackJob
from Jobs.GenerateJobs import generate_jobs
from apply import apply
from player import Player

import page_controller as p



# Game Initialized Variables and Conditions
user = Player()  # Player initialized
turn = 0  # Turn counter, ends when 11 or higher
win = False  # Win Condition


newJob = SpecialistJob()
print(newJob.skills)



# GUI
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your MEssage", font=("Arial", 18))
        self.label.pack(pady=10, padx=10)

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show MessageBox", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.show_message)
        self.button.pack(pady=10, padx=10)

        self.root.mainloop()

    def shortcut(self, event):
        # print(event)
        if event.keysym == 'Return':
            self.show_message()

    def show_message(self):
        if not self.check_state.get():
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))


MyGUI()



p.start_pages()


# GUI
# window = tk.Tk()
# window.geometry("980x720")
# window.title("We Regret to Inform You")
# window.mainloop()



# GUI Practice

# label = tk.Label(window, text="Hellow World!", font=('Arial', 18))
# label.pack(padx=20, pady=10)
#
# textbox = tk.Text(window, height=3, font=("Arial", 16))
# textbox.pack()
#
# my_entry = tk.Entry(window)
# my_entry.pack(padx=20, pady=20)
#
# button = tk.Button(window, text="Click ME!", font=("Arial", 18))
# button.pack(pady=50)
#
# button_frame = tk.Frame(window)
# button_frame.columnconfigure(0, weight=1)
# button_frame.columnconfigure(1, weight=1)
# button_frame.columnconfigure(2, weight=1)
#
# btn1 = tk.Button(button_frame, text="1", font=("Arial", 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
#
# btn2 = tk.Button(button_frame, text="2", font=("Arial", 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
#
# btn3 = tk.Button(button_frame, text="3", font=("Arial", 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
#
# btn4 = tk.Button(button_frame, text="4", font=("Arial", 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
#
# btn5 = tk.Button(button_frame, text="5", font=("Arial", 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
#
# btn6 = tk.Button(button_frame, text="6", font=("Arial", 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
#
# button_frame.pack(fill="x")
#
# anotherbtn = tk.Button(window, text="TEST")
# anotherbtn.place(x=200, y=200, height=100, width=100)


