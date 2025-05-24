import pygame
from .renderer import Renderer

class PygameRenderer(Renderer):
    def initialize(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def clear(self):
        self.screen.fill((0, 0, 0))

    def draw_sprite(self, position, sprite):        
        self.screen.blit(sprite.image,(position.x, position.y) )

    def present(self):
        pygame.display.flip()
        self.clock.tick(60)

    def shutdown(self):
        pygame.quit()