import turtle
from random import randint
turtle.speed(1)   # 设置turtle速度到最慢
# 画一个16*16的网格
turtle.color("gray")
x = -80
for y in range(-80, 80+1, 10):
    turtle.penup()
    turtle.goto(x, y)  # 画一条水平线
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80,80+1,10):
    turtle.penup()
    turtle.goto(x, y) # 画一条竖直线
    turtle.pendown()
    turtle.forward(160)

turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
x = y = 0
while abs(x) < 80 and abs(y) < 80:
    r = randint(0,3)
    if r == 0:
        x += 10 # 向右走
        turtle.setheading(0)
        turtle.forward(10)
    elif r == 1:
        y -= 10 # 向下走
        turtle.setheading(270)
        turtle.forward(10)
    elif r == 2:
        x -= 10 # 向左走
        turtle.setheading(180)
        turtle.forward(10)
    elif r == 3:
        y += 10 # 向上走
        turtle.setheading(90)
        turtle.forward(10)

turtle.done()