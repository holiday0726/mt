class CustomImage:
    def __init__(self):
        self.image = None
        self.x = 0
        self.y = 0
        self.w = 130
        self.h = 190

    def render(self):
        image(self.image, self.x, self.y, self.w, self.h)
        return self
    
    def setImage(self, imageName):
        self.image = loadImage('./resource/'+imageName+".png")
        return self

    def setX(self, x):
        self.x = x
        return self

    def setY(self, y):
        self.y = y
        return self
    
    def setW(self, w):
        self.w = w
        return self

    def setH(self, h):
        self.h = h
        return self
