import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    if car.collusion(player):
        scoreboard.game_over()
        game_is_on = False
    if player.is_passed_finish_line():
        car.level_up()
        player.level_up()
        scoreboard.level_up()
        scoreboard.write_score()

screen.exitonclick()
