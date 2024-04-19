import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math

class Casino:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, money):
        self.balance += money

    def subtract_money(self, money):
        self.balance -= money

class Player:
    def __init__(self, balance):
        self.balance = balance

    def add_money(self, money):
        self.balance += money

    def subtract_money(self, money):
        self.balance -= money

    def play_game(self, game):
        bet_amount = int(entry_bet_amount.get())
        if bet_amount == 0:
            return

        if bet_amount > self.balance:
            messagebox.showinfo("Ошибка", "Недостаточно средств для ставки.")
            return

        global guessed_number
        guessed_number = int(entry_guess.get())

        if guessed_number < 1 or guessed_number > 10:
            messagebox.showinfo("Ошибка", "Введенное число не входит в интервал.")
            return

        global random_number
        random_number = game.generate_random_number(1, 10)

        if guessed_number == random_number:
            self.add_money(bet_amount)
            casino.subtract_money(bet_amount)
        else:
            self.subtract_money(bet_amount)
            casino.add_money(bet_amount)

        if self.balance <= 0 or casino.balance <= 0:
            messagebox.showinfo("Игра окончена", "Один из счетов равен нулю, игра закончена")
            root.quit()

class Game:
    def generate_random_number(self, min_num, max_num):
        random_number = random.randint(min_num, max_num)
        return random_number

def start_game():
    player.play_game(game)
    update_text()
    highlight_number()

def highlight_number():
    # Очищаем предыдущую подсветку
    for circle_index in range(10):
        circle_color = "green" if circle_index + 1 == random_number else "red"
        circle_images[circle_index] = create_circle_image(circle_color, circle_index + 1)

    circle_images[random_number - 1] = create_circle_image("win", random_number)
    guessed_number = int(entry_guess.get())
    if 1 <= guessed_number <= 10:
        circle_images[guessed_number - 1] = create_circle_image("guess", guessed_number)
    update_circles()

def update_text():
    label_balance.config(text=f'Баланс Казино: {casino.balance}\nВаш Баланс: {player.balance}')

def update_circles():
    for i, image in enumerate(circle_images):
        center_x = 200 + 150 * math.cos(2 * math.pi * i / 10)
        center_y = 200 + 150 * math.sin(2 * math.pi * i / 10)
        canvas.itemconfig(circle_items[i], image=image)
        canvas.coords(circle_items[i], center_x, center_y)

def create_circle_image(color, number):
    circle_radius = 15
    image = Image.new("RGBA", (circle_radius*2, circle_radius*2), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 12)

    if color == "win":
        draw.ellipse((0, 0, circle_radius*2, circle_radius*2), fill="green")
    elif color == "guess":
        draw.ellipse((0, 0, circle_radius*2, circle_radius*2), fill="red")
    else:
        draw.ellipse((0, 0, circle_radius*2, circle_radius*2), fill=color)


    text_x = (circle_radius * 2 - 2) / 2
    text_y = (circle_radius * 2 - 4) / 2
    draw.text((text_x, text_y), str(number), fill="white", font=font)

    return ImageTk.PhotoImage(image)

casino = Casino(100000)
player = Player(5000)
game = Game()

root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 200
h = h - 200
root.geometry(f'400x450+{w}+{h}')
root.title("Казино")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

label_bet_amount = tk.Label(root, text="Введите ставку:")
label_bet_amount.config(font='Georgia, 12')
label_bet_amount.pack()

entry_bet_amount = tk.Entry(root, width=40)
entry_bet_amount.pack()

label_guess = tk.Label(root, text="Угадайте число (между 1 и 10):")
label_guess.pack()

entry_guess = tk.Entry(root, width=40)
entry_guess.pack()

button_play = tk.Button(root, width=30, height= 3, text="Играть", command=start_game)
button_play.pack()

label_balance = tk.Label(root, text=f'Баланс Казино: {casino.balance}\nВаш Баланс: {player.balance}')
label_balance.pack()

circle_images = []
circle_items = []

for i in range(10):
    circle_images.append(create_circle_image("red", i + 1))
    center_x = 200 + 150 * math.cos(2 * math.pi * i / 10)
    center_y = 200 + 150 * math.sin(2 * math.pi * i / 10)
    circle_items.append(canvas.create_image(center_x, center_y, image=circle_images[-1], anchor=tk.CENTER))

root.mainloop()
