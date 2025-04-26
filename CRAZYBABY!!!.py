from turtle import *
def s():
    left(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
def cb():
    for i in range(360):
        s()
        right(1)
cb()
