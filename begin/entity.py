# Entity class

# Need random to generate an Entity's id property
import random

class Entity:
    ''' An Entity is literally just an integer ID '''
    
    def __init__(self, id):
        ''' Initialize a new Entity with an id number or it will randomly choose a number between 0 and one million '''
        self.id = id
        
    def get_id(self):
        ''' Return the id of the Entity object '''
        return self.id
