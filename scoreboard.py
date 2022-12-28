from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, high_score):
        super().__init__() 
        self.current_score = 0
        self.high_score = high_score
        
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=300)
        self.string = "Score: " + str(self.current_score) +\
                      "            High Score: " + str(self.high_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)

    def increace_high_score(self):
        self.clear()
        self.high_score = self.current_score
        self.string = "Score: " + str(self.current_score) +\
                      "            High Score: " + str(self.high_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)
        return self.high_score


    def game_over(self):
        self.increace_high_score()
        self.color("red")
        self.goto(x=0, y=0)
        self.write("           GAME OVER\nPlay another game? 'Y' or 'N'", font=FONT, align=ALIGNMENT)
        return self.high_score
        

    def increace_score(self):
        self.clear()
        self.current_score += 1    
        
        self.string = "Score: " + str(self.current_score) +\
                      "            High Score: " + str(self.high_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)
        
