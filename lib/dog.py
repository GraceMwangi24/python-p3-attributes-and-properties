#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
class Dog:
    def __init__(self, name="Default", breed = None):
        self.name=name  
        self.breed = breed

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value  
        else:
            print("Name must be string between 1 and 25 characters.")  # Print error
            self._name = "Default"  
    def get_name(self):
        return self._name  

    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None

    def get_breed(self):
        return self._breed       


    name = property(get_name, set_name)
    #breed = property (get_breed , set_breed)
