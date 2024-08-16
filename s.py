import turtle
import time

delay=0.1

# set up the screen 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #this turns off the screen update

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop" #use to move the head

#functions
def goUp():
    pass
def goDown():
    pass
def goLeft():
    pass
def goRight():
    pass
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="right":
        head.setx(head.xcor()+20) #you can use like that




# main game loop
while True:
    wn.update()

    move()
    time.sleep(delay)
wn.mainloop() #to keep window open