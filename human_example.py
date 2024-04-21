import tkinter as tk
import math


class Figure:
    def __init__(self, a):
        self.a = a


class Color:
    def __init__(self, color='green'):
        self.color = color


class Rectangle(Figure, Color):
    def __init__(self, a, b, color):
        Figure.__init__(self, a)
        Color.__init__(self, color)
        self.b = b

    def area(self):
        s = self.a * self.b
        return s

    def perimeter(self):
        p = (self.a + self.b) * 2
        return p

    def draw(self, canvas):
        canvas.create_rectangle(0, 0, self.a, self.b, fill=self.color)
        canvas.create_text(self.a / 2, self.b / 2, text=f"S={self.area()}\nP={self.perimeter()}", fill="white")


class Triangle(Figure, Color):
    def __init__(self, a, b, c, color):
        if a < (b + c) and b < (a + c) and c < (a + b):
            Figure.__init__(self, a)
            Color.__init__(self, color)
            self.b = b
            self.c = c
        else:
            print("You have entered sides which is impossible to create")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return s

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def draw(self, canvas):
        canvas.create_polygon(0, self.c, self.a, self.c, self.a / 2, 0, fill=self.color)
        canvas.create_text(self.a / 2, self.c / 2, text=f"S={self.area()}\nS={self.perimeter()}", fill="white")


class Circle(Figure, Color):
    def __init__(self, a, color):
        Figure.__init__(self, a)
        Color.__init__(self, color)

    def area(self):
        s = math.pi * self.a * self.a
        return s

    def perimeter(self):
        p = 2 * math.pi * self.a
        return p

    def draw(self, canvas):
        canvas.create_oval(0, 0, self.a, self.a, fill=self.color)
        canvas.create_text(self.a / 2, self.a / 2, text=f"S={self.area()}\nP={self.perimeter()}", fill="white")


def draw_figure():
    canvas.delete("all")
    if var.get() == "Rectangle":
        rec1 = Rectangle(int(entry_a.get()), int(entry_b.get()), var2.get())
        rec1.draw(canvas)
    elif var.get() == "Triangle":
        tri1 = Triangle(int(entry_a.get()), int(entry_b.get()), int(entry_c.get()), var2.get())
        tri1.draw(canvas)
    elif var.get() == "Circle":
        cir1 = Circle(int(entry_a.get()), var2.get())
        cir1.draw(canvas)


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

var = tk.StringVar(root)
figures = ["Rectangle", "Triangle", "Circle"]
var.set(figures[0])
figure_menu = tk.OptionMenu(root, var, *figures)
figure_menu.pack()

label_a = tk.Label(root, text="Enter a:")
label_a.pack()
entry_a = tk.Entry(root, width=20)
entry_a.pack()

label_b = tk.Label(root, text="Enter b:")
label_b.pack()
entry_b = tk.Entry(root, width=20)
entry_b.pack()

label_c = tk.Label(root, text="Enter c:")
label_c.pack()
entry_c = tk.Entry(root, width=20)
entry_c.pack()

var2 = tk.StringVar(root)
colors = ["green", "blue", "black", "red", "yellow", "purple"]
var2.set(colors[0])
color_menu = tk.OptionMenu(root, var2, *colors)
color_menu.pack()

button = tk.Button(root, text="Draw", command=draw_figure)
button.pack()

root.mainloop()
