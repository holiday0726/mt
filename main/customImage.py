class CustomImage:
    def __init__(self):
        self.image = None
        self.x = 0
        self.y = 0
        self.w = 130
        self.h = 190

    def load_image(self, imageName):
        self.image = loadImage(imageName+".png")
        return self

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self
    
    def set_w(self, w):
        self.w = w
        return self

    def set_h(self, h):
        self.h = h
        return self

    def render(self):
        image(self.image, self.x, self.y, self.w, self.h)
        return self
