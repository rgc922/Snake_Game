from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.turtles = []
        self.create_snake() ### llama la funcion una vez instanciada
                            ### y la ejecuta la primera vez
        self.head = self.turtles[0]


    def create_snake(self):
        x = 0
        y = 0
        for turtle in range(0, 3):
            position = (x, y)
            self.add_segment(position)
            x -= 20
            
        

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        
        self.turtles.append(new_turtle)
    
    def extend(self):
        ### extends the snake each time gets food
        self.add_segment(self.turtles[-1].position())


    def move(self):  
    
        for seg_num in range(len(self.turtles) -1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)  

    

    def up(self):     
        if self.head.heading() != DOWN and abs(self.turtles[0].xcor() - self.turtles[1].xcor()) > 2:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP and abs(self.turtles[0].xcor() - self.turtles[1].xcor()) > 2:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT and abs(self.turtles[0].ycor() - self.turtles[1].ycor()) > 2:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT and abs(self.turtles[0].ycor() - self.turtles[1].ycor()) > 2:
            self.head.setheading(RIGHT)
