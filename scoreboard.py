from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__() 
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=285)
        self.string = "Score: " + str(self.current_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
    
    def increace_score(self):
        self.clear()
        self.current_score += 1    
        
        self.string = "Score: " + str(self.current_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)
        
