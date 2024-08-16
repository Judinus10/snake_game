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
    head.direction="up"  #dont use ==, otherwise it can't move
def goDown():
    head.direction="down"
def goLeft():
    head.direction="left"
def goRight():
    head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        head.setx(head.xcor()+20) #you can use like that

# keyboard binding
wn.listen()
wn.onkeypress(goUp,"w")
wn.onkeypress(goDown,"s")
wn.onkeypress(goLeft,"a")
wn.onkeypress(goRight,"d")


# main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop() #to keep window open