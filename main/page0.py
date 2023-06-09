from Page import Page
from CustomImage import CustomImage

class Page0:
    def __init__(self):
        pass
        
    def render(self):
        CustomImage().setX(0).setY(0).setW(width).setH(height).setImage("intro").render()
    
    #####################
    #event Function Area#
    #####################
    
    def keyPressed(self):
        pass
        
    def mousePressed(self):
        if mouseX > 446 and mouseX < 770 and mouseY > 520 and mouseY < 680:
            noCursor()
            Page.next()
        
    def mouseWheel(self, event):
        if event.count < 0:
            if Page.backgroundColor <=30: Page.backgroundColor += 3
        else:
            if Page.backgroundColor >=3: Page.backgroundColor -= 3
