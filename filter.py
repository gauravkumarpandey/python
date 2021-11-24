#Filter

#Sub range
import random
v = []
for x in range(10):
    v.append(random.randrange(100))

print(v)

def lower(value):
    if value < 50:
        return True
    return False

f = filter(lower, v)
print(f)
print(list(f))

#Filter types
class Animal:
    name = ''
    def __init__(self, name) -> None:
        self.name = name

class Cat(Animal):
     def __init__(self, name) -> None:
         super().__init__(name)

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

animals = []
for x in range(10):
    name = 'Animal ' + str(x)
    if x %2 == 0:
        animals.append(Cat(name))
    else:
        animals.append(Dog(name))

print(animals)

def cat_filter(value):
    return isinstance(value, Cat)

def dog_filter(value):
    return isinstance(value, Dog)

cats = list(filter(cat_filter, animals))
for c in cats:
    print(f'Cat: {c.name}')

dogs = list(filter(dog_filter, animals))
for d in dogs:
    print(f'Dog: {d.name}')