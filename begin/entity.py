# Entity class

# Need unique identifier an Entity's id property if not given
import uuid

class Entity:
    ''' An Entity is literally just an integer ID '''
    
    def __init__(self, id=None):
        ''' Initialize a new Entity with an id number or it will randomly choose a number between 0 and one million '''
        if id:
            self.id = id
        else:
            self.id = uuid.uuid4().hex
        
    def get_id(self):
        ''' Return the id of the Entity object '''
        return self.id
