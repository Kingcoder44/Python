import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("White")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        food.locate()
        snake.body()
        score.increase()
    # detect collision with tail
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
