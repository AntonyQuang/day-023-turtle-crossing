from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align = ALLIGNMENT, font=FONT)