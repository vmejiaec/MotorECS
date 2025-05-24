import pygame
from ecs import EntityManager, ComponentManager
from systems import MovementSystem, RenderSystem
from components import Position, Velocity, Sprite
from render import Renderer, PygameRenderer, ConsoleRenderer
from game_engine import GameEngine

def main():
    # Setup
    entity_manager = EntityManager()
    component_manager = ComponentManager()    
    renderer = ConsoleRenderer()
    renderer.initialize(80, 30)
    
    # Systems
    systems = [
        MovementSystem(component_manager),
        RenderSystem(component_manager, renderer)
    ]

    # Crear entidades
    e1 = entity_manager.create_entity()
    component_manager.add_component(e1, Position(1, 4))
    component_manager.add_component(e1, Velocity(0.01, 0.002))
    component_manager.add_component(e1, Sprite(char='X'))

    e2 = entity_manager.create_entity()
    component_manager.add_component(e2, Position(70, 2))
    component_manager.add_component(e2, Velocity(-0.01, 0.003))
    component_manager.add_component(e2, Sprite(char='O'))

    engine = GameEngine(component_manager, systems, renderer, max_frames=7000)
    engine.run()

if __name__ == "__main__":
    main()