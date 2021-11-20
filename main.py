#import the class
from cat import Cat
from inheritance import Feline, Lion, Tiger

def show():
    c = Cat('Kitty',1,'Tebby')
    b = Cat('Othelo', 6, 'Black')

    print(c)
    print(b)
    c.description()
    c.meow()
    c.sleep()

    b.description()
    b.meow()
    b.hungry()

if __name__ == '__main__':
    x = Cat('Test')
    print(x)
    show()

    print('Inheritance....')
    f = Feline('Kitty')
    print(f)
    f.meow()

    l = Lion('Leo')
    print(l)
    l.meow()
    l.roar()
    
    t = Tiger()
    print(t)
    t.rename('Tony')
    t.meow()
    t.stalk()