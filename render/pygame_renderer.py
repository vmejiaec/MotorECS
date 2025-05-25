import pygame
from render.renderer import Renderer

class PygameRenderer(Renderer):
    def initialize(self, width, height):
        pygame.init()
        self.size = (width , height )
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pygame Renderer")
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        self.screen.fill((0, 0, 0))

    def draw_sprite(self, position, sprite):
        x, y = int(position.x ), int(position.y )
        pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 8)

    def present(self):
        pygame.display.flip()
        self.clock.tick(60)

    def shutdown(self):
        pygame.quit()
