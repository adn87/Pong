from turtle import Screen
from paddle import Paddle


R_PADDLE_COR = (350,0)
L_PADDLE_COR = (-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((R_PADDLE_COR))
l_paddle = Paddle((L_PADDLE_COR))


screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()