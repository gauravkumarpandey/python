t = (1, 2, 3, 4)
for x in t:
    print(x)

people = ('Bryan', 'Gaurav', 'Rango')
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) Stop Iteration

#Iterable class
import random
class RandomGenerator:
    def __init__(self) -> None:
        self._max = 5
    
    def __iter__(self):
        for _ in range(self._max):
            yield(random.randrange(0,100))
    
    def set_max(self, max):
        self._max = max

print('~' * 20)
rand = RandomGenerator()
rand.set_max(10)
for x in rand:
     print(x)
print('~' * 20)