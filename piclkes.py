#Pickle

import pickle

def outline(func):
    def inner(*agrs, **kwargs):
        print('~' * 20)
        print(f'Function: {func.__name__}')
        func(*agrs, **kwargs)
        print('~' * 20)
    return inner

#simple class
class Cat:
    def __init__(self, name, age , info) -> None:
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self, msg = ''):
        print(msg)
        print(f'{self._name} is a {self._age} years old cat')
        for k,v in self._info.items():
            print(f'{k} : {v}')

othelo = Cat('Othelo', 4, dict(color = 'black', weight = 15, loves = 'eating'))

othelo.display('Test')

#Serialize
sc = pickle.dumps(othelo)
print(sc)

with open('cat.txt', 'wb') as f:
    pickle.dump(othelo, f)

#Deserialize
my_cat = pickle.loads(sc)
print('from String')
my_cat.display('From String')

with open('cat.txt', 'rb') as f:
    disk_cat = pickle.load(f)
disk_cat.display('From Disk')
