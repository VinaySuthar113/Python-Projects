from pdb import Restart
from customtkinter import *
import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 400
DELAY = 100
SIZE = 20
FOOD_SIZE = 30

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.foods_eaten = 0
        self.body_color = "green"
        self.head_color = "red"
        self.tail_color = "blue"

    def move(self):
        head = self.body[0]
        x, y = head

        if self.direction == "Up":
            y -= SIZE
        elif self.direction == "Down":
            y += SIZE
        elif self.direction == "Left":
            x -= SIZE
        elif self.direction == "Right":
            x += SIZE

        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, new_direction):
        if new_direction in ["Up", "Down", "Left", "Right"]:
            if new_direction == "Up" and self.direction != "Down":
                self.direction = new_direction
            elif new_direction == "Down" and self.direction != "Up":
                self.direction = new_direction
            elif new_direction == "Left" and self.direction != "Right":
                self.direction = new_direction
            elif new_direction == "Right" and self.direction != "Left":
                self.direction = new_direction

    def draw(self, canvas):
        for index, (x, y) in enumerate(self.body):
            if index == 0:  # Snake's head
                canvas.create_oval(x, y, x + SIZE, y + SIZE, fill=self.head_color)
            elif index == len(self.body) - 1:  # Snake's tail
                if self.direction == "Up":
                    points = [x + SIZE // 2, y + SIZE, x, y, x + SIZE, y]
                elif self.direction == "Down":
                    points = [x + SIZE // 2, y, x, y + SIZE, x + SIZE, y + SIZE]
                elif self.direction == "Left":
                    points = [x + SIZE, y + SIZE // 2, x, y, x, y + SIZE]
                elif self.direction == "Right":
                    points = [x, y + SIZE // 2, x + SIZE, y, x + SIZE, y + SIZE]
                canvas.create_polygon(points, fill=self.tail_color)
            else:  # Snake's body
                canvas.create_oval(x, y, x + SIZE, y + SIZE, fill=self.body_color)

# Game class
class Game:
    def __init__(self):
        self.window = CTk()
        self.window.title("Snake Game")
        self.canvas = CTkCanvas(self.window, width=WIDTH, height=HEIGHT, bg="#272B30")
        self.canvas.pack()
        self.snake = Snake()
        self.food = self.create_food()
        self.player_name = self.get_player_name()
        self.food_color = "yellow"  # Default color for food
        self.window.bind("<Key>", self.on_key_press)
        self.window.after(0, self.update)
        
    def get_player_name(self):
        self.player_name = tk.StringVar()
        player_name_window = CTkToplevel(self.window)
        player_name_window.title("Enter Player Name")
        player_name_window.geometry("300x150")
        
        CTkLabel(player_name_window, text="Player Name:").pack(pady=10)
        name_entry = CTkEntry(player_name_window, textvariable=self.player_name)
        name_entry.pack(pady=10)
        
        submit_button = CTkButton(player_name_window, text="Submit", command=player_name_window.destroy)
        submit_button.pack(pady=10)
        
        self.window.wait_window(player_name_window)
        return self.player_name.get()

    def create_food(self):
        x = random.randint(1, (WIDTH - FOOD_SIZE) // FOOD_SIZE) * SIZE
        y = random.randint(1, (HEIGHT - FOOD_SIZE) // FOOD_SIZE) * SIZE
        return x, y

    def check_collision(self):
        if self.snake.body[0] == self.food:
            self.snake.body.append((0, 0))
            self.food = self.create_food()
            self.snake.foods_eaten += 1
            self.change_colors()

    def change_colors(self):
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan"]
        self.snake.body_color = random.choice(colors)
        self.snake.head_color = random.choice(colors)
        self.snake.tail_color = random.choice(colors)
        self.food_color = random.choice(colors)

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over", font=("Arial", 20), fill="red")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 30, text=f"Foods eaten: {self.snake.foods_eaten}", font=("Arial", 15), fill="white")
        Restart_Button = CTkButton(master = self.window,text = "restart",command = self.restart)
        Restart_Button.place(x = 130,y = 250)
        
    def restart(self):
        global game
        self.window.destroy()
        game = Game()
        game.window.mainloop()
    
    def update(self):
        self.snake.move()
        self.check_collision()

        if self.is_collision():
            self.game_over()
        else:
            self.canvas.delete("all")
            self.snake.draw(self.canvas)
            self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + FOOD_SIZE, self.food[1] + FOOD_SIZE, fill=self.food_color)
            self.canvas.create_text(10, 10, anchor="nw", text=f"Player: {self.player_name}", font=("Arial", 10), fill="white")
            self.canvas.create_text(10, 30, anchor="nw", text=f"Foods eaten: {self.snake.foods_eaten}", font=("Arial", 10), fill="white")

        self.window.after(DELAY, self.update)

    def is_collision(self):
        x, y = self.snake.body[0]
        return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in self.snake.body[1:]

    def on_key_press(self, event):
        if event.keysym == "Up":
            self.snake.change_direction("Up")
        elif event.keysym == "Down":
            self.snake.change_direction("Down")
        elif event.keysym == "Left":
            self.snake.change_direction("Left")
        elif event.keysym == "Right":
            self.snake.change_direction("Right")

# Main function
def main():
    game = Game()
    game.window.mainloop()

if __name__ == "__main__":
    main()
