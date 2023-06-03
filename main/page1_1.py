from content import Content
from page import Page
from firstFirework import FirstFirework

class Page1_1:
    def __init__(self):
        self.stars = []
        self.firework = FirstFirework()

        self.textImage = loadImage("text1.png")
        
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
            
        frameRate(50000)
    
    def render(self):
        cursor()
        
        colorMode(HSB)
        background(0)
        
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
            
        # Draw fireworks)
        if self.firework.exploded:
            self.firework.update()
        self.firework.show()
        
        image(self.textImage, 100, 300, 300, 60)
        if self.firework.done():
            firework = None
            Page.next()
