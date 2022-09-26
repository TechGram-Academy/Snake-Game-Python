from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

screen.update()
while True:
    time.sleep(0.1)
    snake.move_snake()
    snake.up()
    screen.update()
    


screen.exitonclick()

