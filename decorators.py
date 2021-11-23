#A decorators takes in a function , add some functionality and return it

#Basic Decorator 
#An example we will change the execution order
from typing import List


def test_decorator(func):
    print('Before')
    func()
    print('after')


@test_decorator
def do_stuff():
    print('Doing stuff')

#Real Decorator
#In this example we will change the functionality

def make_bold(func):
    def inner():
        print('<b>')
        print(func())
        print('</b>')
    return inner #return the inner function

@make_bold
def print_name():
    print('Gaurav Pandey')

print_name()

#Decorator with parameter
#This will have a defined number of parameters
def num_check(func):
    def check_int(o):
        if isinstance(o,int):
            if o==0:
                print('Can Not divide by Zero')
                return False
            return True
        print(f'{o} is not a number')
        return False
    def inner(x,y):
        if not check_int(x) or not check_int(y): 
            return
        return func(x,y)
    return inner

@num_check
def divide(a,b):
    print(a/b)

divide(100,3)
divide(100,0)
divide(100,'Cat')

#decorators with unknown number of arguments
# will show decorator chaining
def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        func(*args, **kwargs)
        print('-' * 20)
    return inner

def listItem(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        for x in args:
            print(f'arg: {x}')
        for k,v in kwargs.items():
            print(f' key : {k} , value : {v}')
        #print(f'kwargs= {kwargs}')
    return inner

@outline
@listItem
def display(msg):
    print(msg)

display('Hello World')

@outline
@listItem
def greeting_birthday(name='', age=0):
    print(f'happy birthday {name} you are {age} years old')

greeting_birthday(name='Gaurav', age=37)