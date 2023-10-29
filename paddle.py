from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y_cor = self.ycor() + 20
        self.goto(y=y_cor, x=self.xcor())

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(y=y_cor, x=self.xcor())
