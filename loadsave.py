import json
import os.path

class Inventory:
    pets = {}

    def __init__(self) -> None:
        self.load()

    def add(self, key , qty):
        q = 0
        if key in self.pets: # test to make sure key exist
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: total = {self.pets[key]}')
            

    def remove(self, key, qty):
        if key in self.pets: # test to make sure key exist
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: total = {self.pets[key]}')

    def display(self):
        for key, value in self.pets.items(): # For loop iterating the dictionary
            print(f'The key {key} = value {value}')

    def load(self):
        if not os.path.exists('inventory.txt'):
            print('Skipping , nothing to load')
            return
        print('Loading data from invnetory')
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('loaded')

    def save(self):
        print('Saving in Inventory')
        with open('inventory.txt', 'w') as f: # with is autoclosable
            json.dump(self.pets, f)
        print('Saved')

def main():
    inv = Inventory()
    while True:
        action = input('Actions: Add, remove, list, save ,exit')
        if action == 'add' or action == 'remove':
            key = input('Enter the animal: ')
            qty = int(input('Enter the qty:'))
            if action == 'add':
                inv.add(key, qty)
            if action == 'remove':
                inv.remove(key, qty)
        if action == 'exit':
            break
        if action == 'list':
            inv.display()
        if action == 'save':
           inv.save()
        inv.save()
if __name__ == '__main__':
    main()