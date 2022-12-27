from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game RGC")
screen.tracer(0)

### Uso la clase creada en snake()
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    
    snake.move()
    time.sleep(0.4)

    #detectar colision con la comida
    if snake.head.distance(food) < 15:
        #print("Comida comida")
        food.refresh()
        snake.extend()
        score.increace_score()

    ## colision con la pared game over
    if abs(snake.head.xcor()) > 291 or abs(snake.head.ycor()) > 291:
        ## game over
        game_is_on = False
        score.game_over()
    
    ### collision with tail

    ### ahora con slice
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()