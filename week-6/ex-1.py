# always use a capital for objects / class names
# one class per file
# car.num_wheels, num_wheels is an attribute 
# car.speed(), speed is a method
# init = initialiser function or conductor 

class Vehicle:

    def __init__(self,num_wheels, max_speed, colour)
        self.num_wheels = num_wheels
        self.max_speed = max_speed
        self.colour = colour

    def start(self):
        print(self.action)

class Car(Vehicle):

    def __init__ (self, num_wheels, max_speed, num_doors, colour):
        super().__init__(num_wheels,max_speed,colour)
        self.num_doors = num_doors

    def start(self):
        print('brrrm brrrm')

# python method overrides
    def __str__(self):
        return 'My car is '+ self.colour

my_car = Car(4,160,5,'silver')

second_car = Car(2,200,2,'red')

print(my_car)

# print(my_car.num_doors)

# my_car.start()

class Bicycle:

    def __init__(self, num_wheels, max_speed, colour):
        super().__init__(num_wheels,max_speed,colour)
        self.has_bell = True

    def start(self):
        print('I am pedalling')

my_bike = Bicycle()
print(my_bike.num_wheels)