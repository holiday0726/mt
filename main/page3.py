from Page import Page
from CustomImage import CustomImage
from Star import Star
from Firework import Firework

class Page3:
    def __init__(self):
        self.star = Star(width, height)
        self.fireworks = []
        self.fireworksCnt = 0
        self.zoom = 300
        self.logoImage = CustomImage().setX(250).setY(350).setW(500).setH(100).setImage("logo")
        
        self.mangoneX = width / 2
        self.mangoneY = height / 2
    
    def makeFireWork(self):
        if self.fireworksCnt <= 15:
            if random(1) < 0.1:
                self.fireworks.append(Firework(random(width), height, PVector(0, 0.2)))
                self.fireworksCnt = self.fireworksCnt +1
            
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
            x = self.mangoneX + self.zoom/2 * cos(rad)
            y = self.mangoneY + self.zoom/2 * sin(rad)
            vertex(x, y)
        endContour()
        
        endShape(CLOSE)
        
        noFill()
        stroke(125)
        strokeWeight(30)
        ellipse(self.mangoneX, self.mangoneY, self.zoom, self.zoom)
        
        self.zoom = self.zoom + 10
    
    def render(self):
        
        # Draw stars
        self.star.render()
        self.logoImage.render()
        
        # Draw fireworks
        self.makeFireWork()
    
        for firework in self.fireworks[:]:
            isDone = firework.render()
            if isDone: self.fireworks.remove(firework)
            
        self.drawMangOne()
        
        
    def keyPressed(self):
        if keyCode == ALT:
            self.fireworks.append(Firework(random(width), height, PVector(0, 0.2)))
        if keyCode == LEFT:
            self.mangoneX -= 20
        elif keyCode == RIGHT:
            self.mangoneX += 20
        elif keyCode == UP:
            self.mangoneY -= 20
        elif keyCode == DOWN:
            self.mangoneY += 20

    def mousePressed(self):
        pass
