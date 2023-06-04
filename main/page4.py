from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page
from firework import Firework

class Page4:
    def __init__(self):
        self.stars = []
        self.fireworks = []

        self.logoImage = loadImage("logo.png")
        
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
        
    def render(self):
        
        colorMode(HSB)
        # Draw gradient sky
        #setGradient(0, 0, width, height, color(0, 0, 0), color(0, 0, 64))
        background(0)
        
        image(self.logoImage, 200, 350, 200, 50)
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
        
        # Draw fireworks
        if random(1) < 0.07:
            self.fireworks.append(Firework())
    
        for firework in self.fireworks[:]:
            firework.update()
            firework.show()
    
            if firework.done():
                self.fireworks.remove(firework)
