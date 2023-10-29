from turtle import Turtle

X_POS = 350
Y_POS = 0


class Paddle:
    def __init__(self):
        self.paddle = Turtle()
        self.create_paddle()

    def create_paddle(self):
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x=X_POS, y=Y_POS)

    def up(self):
        y_cor = self.paddle.ycor() + 20
        self.paddle.goto(y=y_cor,x=self.paddle.xcor())

    def down(self):
        y_cor = self.paddle.ycor() - 20
        self.paddle.goto(y=y_cor, x=self.paddle.xcor())
