import sys
from render.renderer import Renderer

class ConsoleRenderer(Renderer):
    def initialize(self, width, height):
        self.width = width
        self.height = height
        self.hide_cursor()
        self.clear()

    def clear(self):
        self.buffer = [["." for _ in range(self.width)] for _ in range(self.height)]

    def draw_sprite(self, position, sprite):
        x, y = int(position.x), int(position.y)
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = sprite.char if hasattr(sprite, 'char') else "#"

    def present(self):
        # Mover cursor al inicio de la pantalla
        sys.stdout.write('\033[H')
        sys.stdout.flush()

        # Dibujar el buffer
        for row in self.buffer:
            print("".join(row))

    def shutdown(self):
        self.show_cursor()
        print("ConsoleRenderer: shutdown")

    def hide_cursor(self):
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()

    def show_cursor(self):
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()
