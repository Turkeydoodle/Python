#A text based adventure game
from math import *
class Car():
    def __init__(self):
        self.top_speed = 70
        self.x = 0
        self.y = 0
    def move(self, x, y):
        x_dist = x - self.x
        y_dist = y - self.y
        dist = sqrt(x_dist**2 + y_dist**2)
        self.x = x
        self.y = y
        time = dist / self.top_speed
        print(f"Moved to ({self.x}, {self.y}) in {time} hours")
car = Car()
car.move(10,10)