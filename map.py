people = ['Matt', 'Bryan' , 'Tommy', 'Renato', 'David']

#Count len
#Old way
counts = []
for x in people:
    counts.append(len(x))

print(f'Old way: {counts}')

print(f'Mapped: {list(map(len, people))}')

first_names = ('Apple', 'Choclate', 'Fudge', 'Pizza')
last_names = ('Pie' , 'Cake', 'Brownies')

def merge(a, b):
    return a + ' ' +  b

x = map(merge, first_names, last_names)
print(x)
print(list(x))

#multiple function with map
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a , b):
    return a/b

def do_all(func, nums):
    return func(nums[0], nums[1])

f = (add, subtract, multiply, divide)
v = [[5,3]]
n = list(v) * len(f)

print(f' f : {f} , n: {n}')

m  = map(do_all, f, n)
print(list(m))