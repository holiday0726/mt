from customImage import CustomImage

class Text:
    def __init__(self, x, y, w, h):
        self.texts = ["text4","text5","text2","text1","text3"]
        self.current = 0
        self.customImage = CustomImage().setX(x).setY(y).setW(w).setH(h)
        self.customImage.setImage("text4")
    
    def setX(self, x):
        self.customImage.setX(x)
        return self

    def setY(self, y):
        self.customImage.setY(y)
        return self
    
    def setW(self, w):
        self.customImage.setW(w)
        return self

    def setH(self, h):
        self.customImage.setH(h)
        return self
    
    def next(self):
        self.current = self.current+1
        if self.current == len(self.texts): self.current = 0
        self.customImage.setImage(self.texts[self.current])
    
    def render(self):
        self.customImage.render()
