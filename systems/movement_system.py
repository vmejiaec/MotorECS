from components import Position, Velocity

class MovementSystem:
    def __init__(self, component_manager):
        self.component_manager = component_manager

    def update(self):
        # Iterate over all entities with Position and Velocity components
        entity_ids = self.component_manager.get_entities_ids_with(Position, Velocity)
        for entity_id in entity_ids:
            position = self.component_manager.get_component(entity_id, Position)
            velocity = self.component_manager.get_component(entity_id, Velocity)

            # Update the position based on the velocity and delta time
            position.x += velocity.x 
            position.y += velocity.y 
