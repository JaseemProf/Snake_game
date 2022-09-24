from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A Snake Game")
screen.tracer(0)

score = Score()
food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_true = True

while is_true:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake()
        score.increase_level()
    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    # collision with tail
    for i in snake.tim_list[1:]:
        if snake.head.distance(i) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
