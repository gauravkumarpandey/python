class Feline:
    def __init__(self, name):
        print('Creating Feline')
        self.name = name

    def meow(self):
        print(f'{self.name} meow')

    def setName(self, name):
        self.name = name

class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')

class Tiger(Feline):
    #don't override constructor unless no other choice
    def __init__(self):
        super().__init__('No Name')
        print('Creating Tiger')

    def stalk(self):
        print(f'{self.name} stalking')

    def rename(self, name):
        super().setName(name)