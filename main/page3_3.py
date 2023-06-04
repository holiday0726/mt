from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page
from firework import Firework

class Page3_3:
    def __init__(self):
        self.stars = []
        self.fireworks = []
        self.fireworksCnt = 0
        self.zoom = 150
        self.logoImage = loadImage("logo.png")
        
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
            
    def appendFireWork(self):
        self.fireworks.append(Firework())
        
    def drawMangOne(self):
        rectMode(CENTER)
        fill(0)
        
        beginShape()
        noStroke()
        vertex(0, 0)
        vertex(width, 0)
        vertex(width, height)
        vertex(0, height)
        
        beginContour()
        for i in range(360, -1, -1):
            rad = radians(i)
            x = width/2 + self.zoom/2 * cos(rad)
            y = height/2 + self.zoom/2 * sin(rad)
            vertex(x, y)
        endContour()
        
        endShape(CLOSE)
        
        noFill()
        stroke(125)
        strokeWeight(10)
        ellipse(width/2, height/2, self.zoom, self.zoom)
        
        self.zoom = self.zoom + 5
    
    def render(self):
        
        colorMode(HSB)
        # Draw gradient sky
        #setGradient(0, 0, width, height, color(0, 0, 0), color(0, 0, 64))
        background(0)
        
        image(self.logoImage, 250, 350, 500, 100)
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
        
        # Draw fireworks
        if self.fireworksCnt <= 15:
            if random(1) < 0.1:
                self.fireworks.append(Firework())
                self.fireworksCnt = self.fireworksCnt +1
    
        for firework in self.fireworks[:]:
            firework.update()
            firework.show()
    
            if firework.done():
                self.fireworks.remove(firework)
        if self.zoom < width + 300:
            self.drawMangOne()
