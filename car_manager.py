from turtle import Turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle(shape="square")
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            color = self.color_generator()
            new_car.color(color)
            new_car.penup()
            x_start = 320
            y_start = random.randint(-230, 230)
            new_car.goto(x_start, y_start)
            self.all_cars.append(new_car)

    def drive(self):
        for driver in range(len(self.all_cars) - 1):
            new_x = self.all_cars[driver].xcor() - self.move_distance
            new_y = self.all_cars[driver].ycor()
            self.all_cars[driver].goto(new_x, new_y)

    def color_generator(self):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        random_color = (r, g, b)
        return random_color

    def reset_cars(self):
        self.move_distance += MOVE_INCREMENT






