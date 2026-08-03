import tkinter as tk
import random
import time


class Shape:
#Base class for every shape
    def __init__(self, canvas, x, y, size, reward, lifetime):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.reward = reward
        self.lifetime = lifetime
        self.id = None
        self.spawn_time = time.time()

    def label(self):
        return "Shape"
#Name of this shape (polymorphic)

class Circle(Shape):
    def __init__(self, canvas, x, y, size, reward, lifetime):
        super().__init__(canvas, x - size / 2, y - size / 2, size, reward, lifetime)
        self.id = self.canvas.create_oval(self.x, self.y, self.x + self.size, self.y + self.size, fill='blue', outline='black')

    def label(self):
        return "Circle"


class Polygon(Shape):
    """Base class for straight-edged shapes. Stores how many sides it has."""

    def __init__(self, canvas, x, y, size, reward, lifetime, sides):
        super().__init__(canvas, x, y, size, reward, lifetime)
        self.sides = sides


class Octagon(Polygon):
    def __init__(self, canvas, x, y, size, reward, lifetime):
        super().__init__(canvas, x, y, size, reward, lifetime, 8)
        self.proper_size = size / 2
        x1 = self.x - self.proper_size
        y1 = self.y - self.proper_size / 2
        x2 = self.x - self.proper_size / 2
        y2 = self.y - self.proper_size
        x3 = self.x + self.proper_size / 2
        y3 = self.y - self.proper_size
        x4 = self.x + self.proper_size
        y4 = self.y - self.proper_size / 2
        x5 = self.x + self.proper_size
        y5 = self.y + self.proper_size / 2
        x6 = self.x + self.proper_size / 2
        y6 = self.y + self.proper_size
        x7 = self.x - self.proper_size / 2
        y7 = self.y + self.proper_size
        x8 = self.x - self.proper_size
        y8 = self.y + self.proper_size / 2
        self.id = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, fill='red', outline='black')

    def label(self):
        return "Octagon"


class Triangle(Polygon):
    def __init__(self, canvas, x, y, size, reward, lifetime):
        super().__init__(canvas, x, y, size, reward, lifetime, 3)
        self.proper_size = size / 2
        x1 = self.x
        y1 = self.y - self.proper_size
        x2 = self.x + self.proper_size
        y2 = self.y + self.proper_size
        x3 = self.x - self.proper_size
        y3 = self.y + self.proper_size
        self.id = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill='purple', outline='black')

    def label(self):
        return "Triangle"


class Square(Polygon):
    def __init__(self, canvas, x, y, size, reward, lifetime):
        super().__init__(canvas, x, y, size, reward, lifetime, 4)
        self.proper_size = size / 2
        x1 = self.x - self.proper_size
        y1 = self.y - self.proper_size
        x2 = self.x + self.proper_size
        y2 = self.y + self.proper_size
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill='green', outline='black')

    def label(self):
        return "Square"


Shapes = [Circle, Square, Triangle, Octagon]


class Game:
#Is the game windowm canvas, and the list of currently-spawned shapes."""

    def __init__(self):
        self.win = None
        self.canvas = None
        self.shapes = []
        self.score = 0
        self.spawn_speed = 1100
        self.menu = None

    def mouse_click(self, event):
        #Checks if the click landed on a shape
        clicked_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for shape in self.shapes:
            if shape.id in clicked_items:
                reaction_time = time.time() - shape.spawn_time
                points = max(0, int(10 - reaction_time * 10)) * shape.reward
                self.score += points
                print(f"Hit a {shape.label()}! +{points} points") #(polymorphysm)
                self.canvas.delete(shape.id)

    def increase_difficulty(self):
        # Shortens the spawn time to increase diffuculty
        if self.spawn_speed > 350:
            self.spawn_speed = int(self.spawn_speed / 1.01)
        else:
            self.end_screen()

    def spawn_shape(self):
        # Spawns random shape at random position
        self.increase_difficulty()
        x = random.randint(100, 850)
        y = random.randint(100, 850)
        shapes_class = Shapes[random.randint(0, len(Shapes) - 1)]
        shape = shapes_class(self.canvas, x, y, 100, 1, 10)
        self.shapes.append(shape)
        self.win.after(self.spawn_speed, self.spawn_shape)

    def end_screen(self):
        self.win.destroy()
        self.menu = tk.Tk()
        self.menu.title('Game Complete!')
        canvas = tk.Canvas(self.menu, width=400, height=0, bg='white')
        heading_label = tk.Label(self.menu, text=f"Game Complete! Score: {self.score}", font=("Helvetica", 36, "bold"))
        heading_label.pack(pady=100)
        my_button = tk.Button(self.menu, text="Play Again", command=self.start)
        my_button.pack(pady=20)
        self.spawn_speed = 1100
        self.menu.mainloop()

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
