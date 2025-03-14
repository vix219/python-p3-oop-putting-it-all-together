#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand= "Adidas", size=9, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        self.set_size(value)

    def cobble(self):
        print("Your shoe is as good as new!")

