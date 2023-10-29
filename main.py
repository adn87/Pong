from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
paddle = Paddle()


screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()