class Entity:
    def __init__(self, entity_id):
        self.entity_id = entity_id
    
    def __repr__(self):
        return f"Entity(id={self.entity_id})"
    