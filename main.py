import pygame
from ecs import EntityManager, ComponentManager
from systems import MovementSystem, RenderSystem
from components import Position, Velocity, Sprite
from render import Renderer, PygameRenderer

def main():
    # Setup
    entity_manager = EntityManager()
    component_manager = ComponentManager()    
    renderer = PygameRenderer()
    renderer.initialize(800, 600)
    pygame.display.set_caption("ECS Game Example")
    
    # Systems
    render_system = RenderSystem(component_manager, renderer)
    movement_system = MovementSystem(component_manager)

    # Crear entidades
    e1 = entity_manager.create_entity()
    component_manager.add_component(e1, Position(100, 40))
    component_manager.add_component(e1, Velocity(1, 2))
    component_manager.add_component(e1, Sprite(pygame.Surface((50, 50), pygame.SRCALPHA)))
    component_manager.get_component(e1, Sprite).image.fill((255, 0, 0))  # Fill with red color

    e2 = entity_manager.create_entity()
    component_manager.add_component(e2, Position(100, 200))
    component_manager.add_component(e2, Velocity(-2, 3))
    component_manager.add_component(e2, Sprite(pygame.Surface((50, 50), pygame.SRCALPHA)))
    component_manager.get_component(e2, Sprite).image.fill((255, 0, 255))  # Fill with magenta color

    # Game loop
    running  = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update systems
        movement_system.update()
        render_system.update()

if __name__ == "__main__":
    main()