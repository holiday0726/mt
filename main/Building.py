from customImage import CustomImage

class Building:
    def __init__(self, x, y, w, h):
        self.buildingList = ["building1","building2","building3","building4"]
        self.current = 0
        self.customImage = CustomImage().setX(x).setY(y).setW(w).setH(h).setImage("building1")
    
    def render(self):
        self.customImage.render()
        
    def next(self):
        self.current = self.current+1
        if self.current == len(self.buildingList): self.current = 0
        self.customImage.setImage(self.buildingList[self.current])
