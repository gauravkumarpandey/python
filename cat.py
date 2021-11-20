class Cat:
    name = ''
    age = 0
    color = ''

    def __init__(self, name, age=0, color ='White'):
        self.name = name
        self.age = age
        self.color = color

    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f' {self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()

    def description(self):
        print(f'{self.name} is a {self.color} color Cat, who is {self.age} years old') 
        