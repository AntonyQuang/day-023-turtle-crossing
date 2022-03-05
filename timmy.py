from turtle import Turtle

POSITION = (0, -280)


class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(POSITION)

    def move(self):
        self.forward(20)

    def return_to_start(self):
        self.goto(POSITION)

    def dead_timmy(self):
        self.color("red")
