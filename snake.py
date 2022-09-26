from turtle import Turtle


STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.body_part = Turtle(shape='circle')
            self.body_part.penup()
            self.body_part.color('white')
            self.body_part.goto(position)
            self.body_parts.append(self.body_part)

    def move_snake(self):
        for part_num in range(len(self.body_parts)-1, 0, -1):
            x = self.body_parts[part_num - 1].xcor()
            y = self.body_parts[part_num - 1].ycor()
            self.body_parts[part_num].goto(x,y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)
               
            



    
        