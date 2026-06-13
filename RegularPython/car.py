class Car:
    def __init__(self, make, model, year, color, engine_running=False, direction="straight"):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_running = engine_running
        self.direction = direction
    def display_information(self):
        return f"{self.year} {self.color} {self.make} {self.model}"
    def start_engine(self):
        self.engine_running = True
        return "The engine has started."
    def stop_engine(self):
        self.engine_running = False
        return "The engine has stopped."
    def check_engine_status(self):
        if self.engine_running:
            return "The engine is running."
        else:
            return "The engine is not running."
    def steer_left(self):
        self.direction = "left"
        return "The car is steering left."
    def steer_right(self):
        self.direction = "right"
        return "The car is steering right."
    def steer_straight(self):
        self.direction = "straight"
        return "The car is steering straight."
car1 = Car("Toyota", "Camry", 2020, "Blue")
def user_input():
    while True:
        userinput = input("What would you like to do with your car? (display information/start/stop/engine status/steer left/steer right/steer straight/quit):")
        if userinput == "display information":
            print(car1.display_information())
        elif userinput == "start":
            print(car1.start_engine())
        elif userinput == "stop":
            print(car1.stop_engine())
        elif userinput == "engine status":
            print(car1.check_engine_status())
        elif userinput == "steer left":
            print(car1.steer_left())
        elif userinput == "steer right":
            print(car1.steer_right())
        elif userinput == "steer straight":
            print(car1.steer_straight())
        elif userinput == "quit":
            break
        else:
            print("Invalid input. Please try again.")
user_input()