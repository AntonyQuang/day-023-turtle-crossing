from turtle import Screen
from timmy import Timmy
from scoreboard import Scoreboard
import time
from car_manager import CarManager

screen = Screen()
screen.setup(height=600, width=600)
screen.colormode(255)
screen.tracer(0)
screen.listen()

tim = Timmy()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=tim.move, key="Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()

    if tim.ycor() > 280:
        car_manager.reset_cars()
        tim.return_to_start()
        scoreboard.update_level()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            tim.dead_timmy()
            screen.update()
            game_is_on = False
            print("Game Over")

    car_manager.drive()


screen.exitonclick()


