from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

high_score = 0

def snake_game():

    global high_score

    screen = Screen()
    screen.reset()
    screen.setup(width=650, height=655)
    screen.bgcolor("black")
    screen.title("My Snake game RGC")
    screen.tracer(0)

    ### Uso la clase creada en snake()
    snake = Snake()
    food = Food()
    score = Scoreboard(high_score)

    
    level = screen.numinput("How fast are you?", "Enter the level 1 (Easy) - 3 (Hard): ", 2, 1, 3)


    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    ### draw the square game
    line = Turtle()
    line.speed('fastest')
    line.color("white")
    line.hideturtle()
    line.penup()
    line.goto(x=300, y=300)
    line.pendown()
    line.goto(x=300, y=-300)
    line.goto(x=-300, y=-300)
    line.goto(x=-300, y=300)
    line.goto(x=300, y=300)


    game_is_on = True

    while game_is_on:
        screen.update()
        
        if level == 1:
            time.sleep(0.3)
        elif level == 2:
            time.sleep(0.2)
        else:
            time.sleep(0.1)

        snake.move()

        #detectar colision con la comida
        if snake.head.distance(food) < 15:
            #print("Comida comida")
            food.refresh()
            snake.extend()
            score.increace_score()

        ## colision con la pared game over
        if (snake.head.xcor()) > 295 or (snake.head.ycor()) > 295 or \
            (snake.head.xcor()) < -295 or (snake.head.ycor()) < -295:
            ## game over
            game_is_on = False
            #print((snake.head.xcor()) , (snake.head.ycor()) )
            high_score_temp = score.game_over()
            if high_score_temp > high_score:
                    high_score = high_score_temp

            screen.listen()
            screen.onkey(snake_game, "y")
            screen.onkey(snake_game, "Y")
            screen.onkey(screen.bye, "n")
            screen.onkey(screen.bye, "N")
        
        ### collision with tail

        ### ahora con slice
        for segment in snake.turtles[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                high_score_temp = score.game_over()
                if high_score_temp > high_score:
                    high_score = high_score_temp

                screen.listen()
                screen.onkey(snake_game, "y")
                screen.onkey(snake_game, "Y")
                screen.onkey(screen.bye, "n")
                screen.onkey(screen.bye, "N")

    screen.exitonclick()

        
        




snake_game()
