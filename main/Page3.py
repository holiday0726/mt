from Page import Page
from CustomImage import CustomImage
from Star import Star
from Firework import Firework
from ParticleSystem import ParticleSystem

class Page3:
    def __init__(self):
        self.star = Star(width, height)
        self.fireworks = []
        self.fireworksCnt = 0
        self.zoom = 300
        self.logoImage = CustomImage().setX(250).setY(350).setW(500).setH(100).setImage("logo")
        self.mangoneX = width / 2
        self.mangoneY = height / 2
        self.isWheelControl = False
        self.logoOpacity = 0

        self.particleSystem1 = ParticleSystem(PVector(150, 350))
        self.particleSystem2 = ParticleSystem(PVector(800, 300))
        self.particleSystem3 = ParticleSystem(PVector(0, height+30))
        self.particleSystem4 = ParticleSystem(PVector(250, height+30))
        self.particleSystem5 = ParticleSystem(PVector(500, height+30))
        self.particleSystem6 = ParticleSystem(PVector(750, height+30))
        self.particleSystem7 = ParticleSystem(PVector(1000, height+30))
        self.particleSystem8 = ParticleSystem(PVector(0, -30))
        self.particleSystem9 = ParticleSystem(PVector(250, -30))
        self.particleSystem10 = ParticleSystem(PVector(500, -30))
        self.particleSystem11 = ParticleSystem(PVector(750, -30))
        self.particleSystem12 = ParticleSystem(PVector(1000, -30))
        self.particleSystem13 = ParticleSystem(PVector(-30, 300))
        self.particleSystem14 = ParticleSystem(PVector(-30, 500))
        self.particleSystem15 = ParticleSystem(PVector(width+30, 300))
        self.particleSystem16 = ParticleSystem(PVector(width+30, 500))
        
    def render(self):
        # Draw stars
        frameRate(30)
        self.star.render()

        # Draw fireworks
        #self.makeFireWork()
    
        #for firework in self.fireworks[:]:
        #    isDone = firework.render()
        #    if isDone: self.fireworks.remove(firework)
        
        #self.particleSystem1.addParticle(PVector(0.1, 0.1), PVector(random(-15, 25), random(-10, 20)))
        #self.particleSystem1.addParticle(PVector(0.1, 0.1), PVector(random(-15, 25), random(-10, 20)))
        #self.particleSystem1.run(255,120,153)
        #self.particleSystem1.run(255,255,255)

        #self.particleSystem2.addParticle(PVector(-0.05, 0.05), PVector(random(-30, 20), random(-10, 20)))
        #self.particleSystem2.addParticle(PVector(-0.05, 0.05), PVector(random(-30, 20), random(-10, 20)))
        #self.particleSystem2.addParticle(PVector(-0.05, 0.05), PVector(random(-30, 20), random(-10, 20)))
        #self.particleSystem2.run(138,43,200)
        #self.particleSystem2.run(255,255,255)
        
        self.particleSystem3.addParticle(PVector(random(0, 0.3), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem3.addParticle(PVector(random(0, 0.3), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem3.run(255,120,153)
        self.particleSystem3.run(255,255,255)
        
        self.particleSystem4.addParticle(PVector(random(-0.3, 0.3), -0.5), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem4.addParticle(PVector(random(-0.3, 0.3), -0.5), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem4.run(138,43,200)
        self.particleSystem4.run(255,255,255)
        
        self.particleSystem5.addParticle(PVector(random(-0.3, 0.3), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem5.addParticle(PVector(random(-0.3, 0.3), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem5.run(255,120,153)
        self.particleSystem5.run(255,255,255)
        
        self.particleSystem6.addParticle(PVector(random(-0.3, 0.3), -0.5), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem6.addParticle(PVector(random(-0.3, 0.3), -0.5), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem6.run(138,43,200)
        self.particleSystem6.run(255,255,255)
        
        self.particleSystem7.addParticle(PVector(random(-0.3, 0), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem7.addParticle(PVector(random(-0.3, 0), -0.8), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem7.run(255,120,153)
        self.particleSystem7.run(255,255,255)
        
        self.particleSystem8.addParticle(PVector(random(0, 0.3), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem8.addParticle(PVector(random(0, 0.3), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem8.run(255,120,153)
        self.particleSystem8.run(255,255,255)
        
        self.particleSystem9.addParticle(PVector(random(-0.3, 0.3), 0.6), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem9.addParticle(PVector(random(-0.3, 0.3), 0.6), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem9.run(138,43,200)
        self.particleSystem9.run(255,255,255)
        
        self.particleSystem10.addParticle(PVector(random(-0.3, 0.3), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem10.addParticle(PVector(random(-0.3, 0.3), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem10.run(255,120,153)
        self.particleSystem10.run(255,255,255)
        
        self.particleSystem11.addParticle(PVector(random(-0.3, 0.3), 0.6), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem11.addParticle(PVector(random(-0.3, 0.3), 0.6), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem11.run(138,43,200)
        self.particleSystem11.run(255,255,255)
        
        self.particleSystem12.addParticle(PVector(random(-0.3, 0), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem12.addParticle(PVector(random(-0.3, 0), 0.3), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem12.run(255,120,153)
        self.particleSystem12.run(255,255,255)
        
        self.particleSystem13.addParticle(PVector(0.3, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem13.addParticle(PVector(0.3, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem13.run(138,43,200)
        self.particleSystem13.run(255,255,255)
        
        self.particleSystem14.addParticle(PVector(0.5, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem14.addParticle(PVector(0.5, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem14.run(138,43,200)
        self.particleSystem14.run(255,255,255)
        
        self.particleSystem15.addParticle(PVector(-0.3, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem15.addParticle(PVector(-0.3, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem15.run(138,43,200)
        self.particleSystem15.run(255,255,255)
        
        self.particleSystem16.addParticle(PVector(-0.5, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem16.addParticle(PVector(-0.5, random(-0.3, 0.3)), PVector(random(-10, 10), random(0, 5)))
        self.particleSystem16.run(138,43,200)
        self.particleSystem16.run(255,255,255)
        
        tint(255,self.logoOpacity)
        self.logoImage.render()
        
        self.drawMangOne()
        
        if not self.isWheelControl:
            self.increseTint()
    ######################
    #define Function Area#
    ######################
    
    def increseTint(self):
        if self.logoOpacity <=250: self.logoOpacity += 10
    
    def decreseTint(self):
        if self.logoOpacity >=5: self.logoOpacity -= 10
    
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
        
        self.zoom = self.zoom + 20
        
    #####################
    #event Function Area#
    #####################
    
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
        
    def mouseWheel(self, event):
        self.isWheelControl = True
        if event.count < 0:
            Page.getCurrentPage().increseTint()
        else:
            Page.getCurrentPage().decreseTint()
