from components import Position, Sprite

class RenderSystem:
    def __init__(self, component_manager, renderer):
        self.components = component_manager
        self.renderer = renderer
    
    def update(self):
        # Clear the screen
        self.renderer.clear()

        # Iterate over all entities with Position and Sprite components
        for entity_id in self.components.get_entities_ids_with(Position, Sprite):
            pos = self.components.get_component(entity_id, Position)
            sprite = self.components.get_component(entity_id, Sprite)
            # Draw the sprite at the position
            self.renderer.draw_sprite(pos, sprite)

        # Present the rendered frame
        self.renderer.present()