class EntityManager:
    def __init__(self):
        self.next_id=0
    
    def create_entity(self):
        #entity = Entity(self.next_id)
        entity_id = self.next_id
        self.next_id += 1
        return entity_id