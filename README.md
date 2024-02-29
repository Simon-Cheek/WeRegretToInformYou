Welcome to *We Regret to Inform You*!

Code Infrastucture:

**Main.py**
-Initializes the game
~-LATER: Gathers any Save Data~

**Director.py**
-Initializes tkinter
-Runs the Game Loop:
  -Generates 5 random jobs
  -Calls Turn.py to collect player input
  -Calls apply.py on all jobs players applied to
  -Displays Result if Jobs applied to
