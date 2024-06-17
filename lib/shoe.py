#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        """The size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        """Size must be an integer"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")


    def cobble(self):
        """Marks the shoe as repaired"""
        self.condition = "New"
        print("Your shoe is as good as new!")

    def repair(self):
        """Another method to mark the shoe as good as new"""
        self.cobble()