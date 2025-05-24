# game_engine.py
class GameEngine:
    def __init__(self, component_manager, systems, renderer, max_frames=10):
        self.component_manager = component_manager
        self.systems = systems
        self.renderer = renderer
        self.max_frames = max_frames

    def run(self):
        #self.renderer.initialize(20, 10)  # O toma el tamaño desde fuera si prefieres
        try:
            for tick in range(self.max_frames):
                for system in self.systems:
                    system.update()
        finally:
            self.renderer.shutdown()
