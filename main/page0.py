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
        global backgroundColor
        if event.count < 0:
            if backgroundColor <=30: backgroundColor += 3
        else:
            if backgroundColor >=3: backgroundColor -= 3
