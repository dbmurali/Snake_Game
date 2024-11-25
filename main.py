from snake import Snake
from turtle import Screen
from  food import Food
from scoreboad import Scoreboad


import time
#SCREEN SETUP
screen=Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.listen()

#OBJECTS FOR SCORE,SNAKE,FOOD
score=Scoreboad()
snake=Snake()
food=Food()

#KEY CONTROLS
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")



# LOOPING GAME
game_on=True
while game_on:
    # HEAD POSITION
    x_pos = snake.head.xcor()
    y_pos = snake.head.ycor()

    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<30:
       food.refresh()
       score.increase_score()
       snake.extend()
    if x_pos>=280 or x_pos<= -280 or y_pos>=280 or y_pos<= -280:
        game_on=False
        score.game_over()

    for segment in snake.snake_tail[1:]:

       if snake.head.distance(segment)<15:
            game_on=False
            score.game_over()




screen.exitonclick()