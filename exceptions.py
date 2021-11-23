#Simple Decorator
from typing import final


def outline(func):
    def inner(*args, **kwargs):
        print('~' * 20)
        print(f'function: {func.__name__}')
        func(*args, **kwargs)
        print('~' * 20)
    return inner

@outline
def test_one(x, y):
    try:
        z = x/y
        print(f'Result: {z}')
    except:
        #catch
        print(f'Something Bad happend x: {x} y: {y}')
    finally:
        #moving along
        print('Complete')

test_one(5,0)
test_one(5,'cat')
test_one(5,2)

@outline
def test_two(x, y):
    try:
        #attempt
        assert(x > 0)
        assert(y > 0)
    except AssertionError:
        print(f'Failed to assert x: {x} and y: {y}')
    except Exception as e:
        print(f'Something Bad happend x: {x} y: {y} issue: {e}')
    else:
        #trusted code
        result = x/y
        print(f'Result : {result}')
    finally:
        print('Complete')

test_two(5,0)
test_two(5,'cat')
test_two(5,2)

#User defined excpetion and raising
class CatError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.args = args

@outline
def test_cat(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty< 9:
            raise CatError('Must own more then 9 Cats')
    except Exception as e:
        print(f'Opps: {e.args}')
    finally:
        print('Complete')

test_cat(3)
test_cat(12.3)
test_cat(11)
test_cat('ABC')

