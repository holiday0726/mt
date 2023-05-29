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
    
    def render(self):
        cursor()
        
        colorMode(HSB)
        background(0)
        
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
            
        image(self.textImage, 100, 200, 500, 130)
        
        # Draw fireworks)
        self.firework.show()
                #self.fireworks.remove(firework)

            
        #Page.next()
