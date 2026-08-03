# Project Report

This is my project report on the python game: Aim Trainer, a simple reaction-based game where you have to click shapes. This project report will include the programming practises that I took in this project and the OOP principles utilised in my code.

### Programming Practices

---
 
#### Clear and uncluttered mainline

**Code Use:**

The mainline is kept short and focused on setting up the GUI. It creates the window and adds a heading and a start button. It then starts the Tkinter event loop. All the actual game mechanics – spawning shapes, handling clicks, scoring, difficulty – are hidden inside the Game class and its methods. The mainline only deals with UI setup. In my code, if the user clicks "Start Game", the Game.start() method takes over, keeping the mainline free from complex logic.

```python
menu = tk.Tk()
menu.title('Aim Trainer')
canvas = tk.Canvas(menu, width=400, height=0, bg='white')
heading_label = tk.Label(menu, text="Aim Trainer", font=("Helvetica", 36, "bold"))
heading_label.pack(pady=100)
game = Game()
game.menu = menu
my_button = tk.Button(
    menu,
    text="Start Game",
    command=game.start)
my_button.pack(pady=20)
menu.mainloop()

```

---
#### One logical task per subroutine
---
#### Use of stubs
---
#### Use of control structures and data structures
---
#### Ease of maintenance
---

 
OOP principles:
Describe and explain how you used a range of OOP principles in your project.  For each principle, include a very small code snippet that highlights the principle.  Include this in a section of your report titled ‘OOP principles’.
 
•	Classes
•	Constructors
•	Methods
•	Objects
•	Inheritance

•	Polymorphism
•	Generalisation
•	Composition
•	Façade pattern
