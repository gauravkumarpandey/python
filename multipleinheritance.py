class Vehicle:
    speed = 0
    
    def drive(self, speed):
        self.speed = speed
        print(f'Driving at {self.speed} speed')
    
    def stop(self):
        self.speed = 0
        print(f'Stopped ')

    def display(self):
        print(f'Driving at {self.speed} speed')

class Freezer:
    temp = 0

    def freeze(self, temp):
        self.temp = temp
        print(f'Freezing at {self.temp} temp')

    def display(self):
        print(f'Freezing at {self.temp} temp')

class FreezerTruck(Vehicle, Freezer): #Mehod resoltion error
    def display(self):
        print(f'Is a Freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'Is a Vehicle: {issubclass(FreezerTruck, Vehicle)}')

        #super(Vehicle, self).display()
        #super(Freezer, self).display()

        Freezer.display(self)
        Vehicle.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
t.display()

