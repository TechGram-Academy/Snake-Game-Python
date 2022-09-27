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
screen.listen() 
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)

while True:
    time.sleep(0.1)
    snake.move_snake()
    screen.update()
    


screen.exitonclick()

