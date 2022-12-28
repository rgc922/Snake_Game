from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__() ### ya tengo todo el modulo de turtle
        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = randint(-14, 14) * 20
        random_y = randint(-14, 14) * 20
        self.goto(random_x, random_y)