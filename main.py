from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=610, height=625)
screen.bgcolor("black")
screen.title("My Snake game RGC")
screen.tracer(0)

### Uso la clase creada en snake()
snake = Snake()
food = Food()
score = Scoreboard()

level = screen.numinput("How fast are you?", "Enter the level 0 (Easy) - 3 (Hard): ", 2, 0, 3)



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



line = Turtle()
line.speed('fastest')
line.color("white")
line.hideturtle()
line.penup()
line.goto(x=285, y=285)
line.pendown()
line.goto(x=285, y=-285)
line.goto(x=-285, y=-285)
line.goto(x=-285, y=285)
line.goto(x=285, y=285)


game_is_on = True

while game_is_on:
    screen.update()
    
    snake.move()
    #time.sleep(0.1)
    if level == 0.0:
        time.sleep(0.5)
    elif level == 1.0:
        time.sleep(0.35)
    elif level == 2.0:
        time.sleep(0.25)
    else:
        time.sleep(0.1)

    #detectar colision con la comida
    if snake.head.distance(food) < 15:
        #print("Comida comida")
        food.refresh()
        snake.extend()
        score.increace_score()

    ## colision con la pared game over
    if (snake.head.xcor()) > 285 or (snake.head.ycor()) > 285 or \
        (snake.head.xcor()) < -285 or (snake.head.ycor()) < -285:
        ## game over
        game_is_on = False
        print((snake.head.xcor()) , (snake.head.ycor()) )
        score.game_over()
    
    ### collision with tail

    ### ahora con slice
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()