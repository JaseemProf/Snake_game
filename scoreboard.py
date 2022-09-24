from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 14, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("Highscore.txt") as data:
            score = data.read()
            self.high_score = int(score)
        self.current_score = 0
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", "w") as data:
                score = str(self.high_score)
                data.write(score)
        self.current_score = 0
        self.updated_score()

    def increase_level(self):
        self.current_score += 1
        self.updated_score()
