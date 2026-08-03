# Project Report

This is my project report on the python game: Aim Trainer, a simple reaction-based game where you have to click shapes. This project report will include the programming practises that I took in this project and the OOP principles utilised in my code.

### Programming Practices

---
 
#### Clear and uncluttered mainline

**Code Use:**

The mainline is kept short and focused on setting up the GUI. It creates the window and adds a heading and a start button. It then starts the Tkinter event loop. All the actual game mechanics – spawning shapes, handling clicks, scoring, difficulty are hidden inside the Game class and its methods. The mainline only deals with UI setup. In my code, if the user clicks `Start Game`, the `Game.start()` method takes over, keeping the mainline clean.

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

In my original code, the `spawn_shape()` sub-routine was responsible for both increasing the game's difficulty and spawning a new shape. This meant the function was performing two separate logical tasks, making it longer and less organised.

#### Old Code:

```python
def spawn_shape(self):
    if self.spawn_speed > 350:
        self.spawn_speed = int(self.spawn_speed / 1.01)
    else:
        self.end_screen()

    x = random.randint(100, 850)
    y = random.randint(100, 850)
    shapes_class = Shapes[random.randint(0, len(Shapes) - 1)]
    shape = shapes_class(self.canvas, x, y, 100, 1, 10)
    self.shapes.append(shape)
    self.win.after(self.spawn_speed, self.spawn_shape)
```
#### New Code:

```python
def increase_difficulty(self):
    # Shortens the spawn time to increase difficulty
    if self.spawn_speed > 350:
        self.spawn_speed = int(self.spawn_speed / 1.01)
    else:
        self.end_screen()

def spawn_shape(self):
    self.increase_difficulty()

    x = random.randint(100, 850)
    y = random.randint(100, 850)
    shapes_class = Shapes[random.randint(0, len(Shapes) - 1)]
    shape = shapes_class(self.canvas, x, y, 100, 1, 10)
    self.shapes.append(shape)
    self.win.after(self.spawn_speed, self.spawn_shape)
```
I improved the program by moving the difficulty code into its own sub-routine called `increase_difficulty()`. Now, `spawn_shape()` only focuses on creating and scheduling new shapes, while `increase_difficulty()` only manages how quickly shapes appear and determines when the game should end.

---
#### Use of control structures and data structures

```python
Shapes = [Circle, Square, Triangle, Octagon]

shape_class = Shapes[random.randint(0, len(Shapes) - 1)]
```

This code demonstrates the use of a data structure and a control structure in my program. The Shapes list is a data structure that stores all possible shape classes that can appear in the game. The random selection acts as a control structure by deciding which shape will be created when spawn_shape() is called.

---
#### Ease of maintenance

```python
class Shape:
    def __init__(self, canvas, x, y, size, reward, lifetime):
        self.canvas = canvas
        self.size = size

class Square(Polygon):
    def label(self):
        return "Square"
```
This code improves the ease of maintenance because common properties of all shapes are stored in the parent `Shape` class instead of being repeated in every individual shape class. For example, attributes such as `canvas` and `size` are inherited by `Square`, `Circle`, `Triangle`, and `Octagon`. If a feature needs to be changed, it only needs to be updated in the `Shape` class. 

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
