import turtle

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
head.direction="stop"

# main game loop
while True:
    wn.update()

wn.mainloop() #to keep window open