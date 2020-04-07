import turtle
import time
import random

delay = 0.1

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game By MJA")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"


# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segments = []





# functions
def got_up():
    head.direction = "up"
def got_down():
    head.direction = "down"
def got_left():
    head.direction = "left"
def got_right():
    head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard binding
wn.listen()
wn.onkeypress(got_up, "Up")
wn.onkeypress(got_down, "Down")
wn.onkeypress(got_left, "Left")
wn.onkeypress(got_right, "Right")

# main game loop
while True:
    wn.update()
    # check for collision  with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction ="stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the segments list
        segments.clear()


    # check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

    # move the end segment first in reverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move the segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)

wn.mainloop()