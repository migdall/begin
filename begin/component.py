# Components, just data no code here to act on the data
# Jesus Noland
# 6/28/2015


class Component:
    ''' Base Component class '''

    def __init__(self, class_name):
        self.__className = class_name

    def get_class(self):
        return self.__className


class RenderComponent(Component):
    '''
    Inherits from the base class Component, takes care of an Entity's rendering on whatever device 
    view parameter is a string-based representation like 'x' or 'o' or '!'
    '''

    def __init__(self, view=None, visible=False):
        super().__init__('Render')
        self.visible = visible
        if view and isinstance(view, str):
            self.view = view
        else:
            self.view = 'x'

    def __repr__(self):
        return self.view


class HealthComponent(Component):
    ''' Inherits from the base class Component, takes care of an Entity's health stats '''

    def __init__(self, curHP=0.0, maxHP=0.0, alive=False):
        super().__init__('Health')
        self.currentHealthPoints = curHP
        self.maxHealthPoints = maxHP
        self.alive = alive
