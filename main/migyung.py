class Migyung:
    def __init__(self):
        self.image = None
        self.x = 0
        self.y = 0
        self.w = 66
        self.h = 106

    def load_image(self):
        self.image = loadImage("migyung.png")
        return self

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self

    def render(self):
        image(self.image, self.x, self.y, self.w, self.h)
        return self
