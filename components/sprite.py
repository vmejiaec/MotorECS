class Sprite:
    def __init__(self, image):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()