# Project Report

This is my project report on the python game: Aim Trainer, a simple reaction-based game where you have to click shapes. This project report will include the programming practises that I took in this project and the OOP principles utilised in my code.

### Programming Practices

---
 
## Clear and uncluttered mainline

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
## One logical task per subroutine

In my original code, the `spawn_shape()` sub-routine was responsible for both increasing the game's difficulty and spawning a new shape. This meant the function was performing two separate logical tasks, making it longer and less organised.

#### Old Code:

```python
def spawn_shape(self):
    if self.spawn_speed > 350: # Spawn speed increase
        self.spawn_speed = int(self.spawn_speed / 1.01)
    else:
        self.end_screen()

    x = random.randint(100, 850) # Spawning Shape
    y = random.randint(100, 850)
    shapes_class = Shapes[random.randint(0, len(Shapes) - 1)]
    shape = shapes_class(self.canvas, x, y, 100, 1, 10)
    self.shapes.append(shape)
    self.win.after(self.spawn_speed, self.spawn_shape)
```
#### New Code:

```python
def increase_difficulty(self): # Spawn speed increase
    # Shortens the spawn time to increase difficulty
    if self.spawn_speed > 350:
        self.spawn_speed = int(self.spawn_speed / 1.01)
    else:
        self.end_screen()

def spawn_shape(self): # Spawning Shape
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
## Use of control structures and data structures

```python
Shapes = [Circle, Square, Triangle, Octagon]

shape_class = Shapes[random.randint(0, len(Shapes) - 1)]
```

This code demonstrates the use of a data structure and a control structure in my program. The Shapes list is a data structure that stores all possible shape classes that can appear in the game. The random selection acts as a control structure by deciding which shape will be created when spawn_shape() is called.

---
## Ease of maintenance

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

 
# OOP principles:

## Classes

I used classes as blueprints for the objects in my game. For example, `Shape` is a base class and `Circle`, `Square`, `Triangle` and `Octagon` are shape classes. I also used a `Game` class to control the overall program.

#### Code Example:

```python
class Shape:
    # Base class for every shape
    def __init__(self, canvas, x, y, size, reward, lifetime):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.reward = reward
        self.lifetime = lifetime
```
---
## Constructors

Every class has a constructor `__init__` which is used to create and initialise objects. For example, in `Circle`, the constructor sets up the circle’s position and draws it on the canvas.

#### Code Example:

```python
class Circle(Shape):
    def __init__(self, canvas, x, y, size, reward, lifetime):
        super().__init__(canvas, x - size / 2, y - size / 2, size, reward, lifetime)
        self.id = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill='blue', outline='black')
```

---
## Methods
Methods are functions that belong to an object and describe what that object can do. My shape classes have methods like `label()`, and my Game class has methods like `mouse_click()`, `spawn_shape()` and `start()`.

#### Code Example:

```python
def label(self):
    return "Circle"
```
---
## Objects
An object is an instance of a class. In my game, I create shape objects by calling a class from the `Shapes` list, and I create a `Game` object with `Game()`.



#### Code Example:

```python
game = Game()

shape = shapes_class(self.canvas, x, y, 100, 1, 10)
```
---
## Inheritance

Inheritance lets one class use the attributes and methods of another class. In my code, `Circle` inherits from `Shape`, and `Triangle`, `Square` and `Octagon` inherit from `Polygon`, which also inherits from `Shape`.

#### Code Example:

```python
class Polygon(Shape):
    def __init__(self, canvas, x, y, size, reward, lifetime, sides):
        super().__init__(canvas, x, y, size, reward, lifetime)
        self.sides = sides
```
---

## Polymorphism

Polymorphism means that the same method name can behave differently depending on the object it is called on. Each shape class overrides the `label()` method to return its own name. In `mouse_click()`, I can call `shape.label()` without needing to know the exact shape type.

#### Code Example:

```python
print(f"Hit a {shape.label()}! +{points} points")
```
---
## Generalisation
Generalisation is when common attributes and methods are put into a general base class. The `Shape` class contains the common data used by all shapes: position, size, reward, lifetime and spawn time. The `Polygon` class then adds `sides`, which is shared by `Square`, `Triangle` and `Octagon`.
#### Code Example:

```python
class Shape:
    def __init__(self, canvas, x, y, size, reward, lifetime):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.reward = reward
        self.lifetime = lifetime
        self.id = None
        self.spawn_time = time.time()
```
---
## Composition

Composition is when a class contains other objects as part of itself. My `Game` class has a canvas, a window, a menu and a list of shape objects. These are all other objects stored inside the `Game` object.

#### Code Example:

```python
class Game:
    def __init__(self):
        self.win = None
        self.canvas = None
        self.shapes = []
        self.score = 0
        self.spawn_speed = 1100
        self.menu = None
```
---
## Façade pattern
The `Game` class is a façade patern, to the more complicated tkinter system. Instead of the user needing to create windows to start the game they can simply call `game.start()`
#### Code Example:

```python
def start(self):
    self.score = 0
    self.spawn_speed = 1100
    self.menu.destroy()
    self.win = tk.Tk()
    self.win.title('Aim Trainer')
    self.canvas = tk.Canvas(self.win, width=1000, height=1000, bg='white', cursor='target')
    self.canvas.pack()
    self.canvas.bind("<Button-1>", self.mouse_click)
    self.win.after(self.spawn_speed, self.spawn_shape)
    self.win.mainloop()
```
---
