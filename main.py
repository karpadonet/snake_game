from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# creating a new screen of size 600*600
screen = Screen()
screen.setup(width = 600, height = 600)
# setting the screen to black color and adding a title
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)# turns off turtle animatiom

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


while game_is_on:
    screen.update()# screen update so we will the movement as one unit
    time.sleep(0.1)# 1 second delay after each segment moves

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()



    # detect collision with tail
    # if head collides with any segment in the tail the game is over
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()











screen.exitonclick()