# Entity Manager, acts as the “database” where you can look up entities and get their list of components, entity management
# Jesus Noland
# 7/6/2015

from entity import Entity

class EntityManager():
    def __init__(self, ENTITY_MAX=100):
        self._entities = []
        self._componentsByClass = {}
        self._lowestUnassignedEid = 0
        self._ENTITY_MAX = ENTITY_MAX

    def generateNewEid(self):
        if self._lowestUnassignedEid < self._ENTITY_MAX:
            self._lowestUnassignedEid = self._lowestUnassignedEid + 1
            return self._lowestUnassignedEid
        # Since the MAX has been reached no more entities can be created
        return -1

    def createEntity(self):
        eid = self.generateNewEid()
        self._entities.append(eid)
        return Entity(eid)
    
    def addComponentToEntity(self, component, entity):
        components = self._componentsByClass[component]
        if not components:
            components = {}
        components[entity.get_id()] = component
        self._componentsByClass[component] = components
