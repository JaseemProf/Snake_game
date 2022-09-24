from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.tim_list = []
        self.create_snake()
        self.head = self.tim_list[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.new_snake(position)

    def reset(self):
        for tim in self.tim_list:
            tim.goto(1000, 1000)
        self.tim_list.clear()
        self.create_snake()
        self.head = self.tim_list[0]

    def new_snake(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.tim_list.append(tim)

    def add_snake(self):
        self.new_snake(self.tim_list[-1].position())

    def move(self):
        for index in range(len(self.tim_list) - 1, 0, -1):
            new_x = self.tim_list[index - 1].xcor()
            new_y = self.tim_list[index - 1].ycor()
            self.tim_list[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
