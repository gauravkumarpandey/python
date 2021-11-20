#skipping
for _x in range(5):
    print('hello')

from person import *
p = Person()
p.setName('Gaurav')
p._name = 'Bryan'

p = Person()
p.work()
#p.__think()
#c = Child()
#c.testDouble()