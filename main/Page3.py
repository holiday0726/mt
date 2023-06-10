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
        self.isStopFireworkLeft = False
        self.isStopFireworkRight = False
        self.isStopFireworkBottom = False
        self.isStopFireworkTop = False
        
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
        
        self.star.render()
    
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
        
        
        self.runFireworkTop(self.isStopFireworkTop)
        self.runFireworkBottom(self.isStopFireworkBottom)
        self.runFireworkLeft(self.isStopFireworkLeft)
        self.runFireworkRight(self.isStopFireworkRight)
        
    
        tint(255,self.logoOpacity)
        self.logoImage.render()
        
        self.drawMangOne()
        
        if not self.isWheelControl:
            self.increseTint()
    ######################
    #define Function Area#
    ######################
    
    def increseTint(self):
        if self.logoOpacity <=250: self.logoOpacity += 5
    
    def decreseTint(self):
        if self.logoOpacity >=5: self.logoOpacity -= 5


    def runFireworkBottom(self, isStop=False):
        
        particleSystems = [self.particleSystem3, self.particleSystem4, self.particleSystem5, self.particleSystem6, self.particleSystem7]
        
        if isStop:
            for particleSystem in particleSystems:
                particleSystem.stop()
            return
        
        isLong = True
        for particleSystem in particleSystems:
            acc =  PVector(random(-0.3, 0.3), -0.8) if isLong else PVector(random(-0.3, 0.3), -0.5) 
            vel = PVector(random(-10, 10), random(0, 5))
            
            particleSystem.addParticle(acc.copy(), vel.copy())
            particleSystem.addParticle(acc.copy(), vel.copy())
            
            if isLong:  particleSystem.run(255,120,153)
            else :   particleSystem.run(138,43,200)
            
            particleSystem.run(255,255,255)
            isLong = not isLong
            
    def runFireworkTop(self, isStop=False):
        
        particleSystems = [self.particleSystem8, self.particleSystem9, self.particleSystem10, self.particleSystem11, self.particleSystem12]
        
        if isStop:
            for particleSystem in particleSystems:
                particleSystem.stop()
            return
        
        isLong = True
        for particleSystem in particleSystems:
            acc =  PVector(random(-0.3, 0.3), 0.6) if isLong else PVector(random(-0.3, 0.3), 0.3) 
            vel = PVector(random(-10, 10), random(0, 5))
            
            particleSystem.addParticle(acc.copy(), vel.copy())
            particleSystem.addParticle(acc.copy(), vel.copy())
            
            if isLong:  particleSystem.run(255,120,153)
            else :   particleSystem.run(138,43,200)
            
            particleSystem.run(255,255,255)
            isLong = not isLong
        
    def runFireworkLeft(self, isStop=False):
        
        particleSystems = [self.particleSystem13, self.particleSystem14]
        
        if isStop:
            for particleSystem in particleSystems:
                particleSystem.stop()
            return
        
        isLong = False
        for particleSystem in particleSystems:
            acc =  PVector(0.5, random(-0.3, 0.3)) if isLong else PVector(0.3, random(-0.3, 0.3))
            vel = PVector(random(-10, 10), random(0, 5))
            
            particleSystem.addParticle(acc.copy(), vel.copy())
            particleSystem.addParticle(acc.copy(), vel.copy())
            
            particleSystem.run(138,43,200)
            particleSystem.run(255,255,255)
            isLong = not isLong
        
    def runFireworkRight(self, isStop=False):
        
        particleSystems = [self.particleSystem15, self.particleSystem16]
        
        if isStop:
            for particleSystem in particleSystems:
                particleSystem.stop()
            return
        
        isLong = False
        for particleSystem in particleSystems:
            acc =  PVector(-0.5, random(-0.3, 0.3)) if isLong else PVector(-0.3, random(-0.3, 0.3))
            vel = PVector(random(-10, 10), random(0, 5))
            
            particleSystem.addParticle(acc.copy(), vel.copy())
            particleSystem.addParticle(acc.copy(), vel.copy())
            
            particleSystem.run(138,43,200)
            particleSystem.run(255,255,255)
            isLong = not isLong
    
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
            if self.isStopFireworkLeft and self.isStopFireworkRight and self.isStopFireworkTop and self.isStopFireworkBottom:
                self.isStopFireworkTop, self.isStopFireworkBottom = False, False
                self.isStopFireworkLeft, self.isStopFireworkRight = False, False
                self.isWheelControl = True
                self.logoOpacity = 255
            else:
                self.isStopFireworkTop, self.isStopFireworkBottom = True, True
                self.isStopFireworkLeft, self.isStopFireworkRight = True, True
                self.isWheelControl = True
                self.logoOpacity = 0
        if keyCode == LEFT:
            self.isStopFireworkLeft = not self.isStopFireworkLeft
        elif keyCode == RIGHT:
            self.isStopFireworkRight = not self.isStopFireworkRight
        elif keyCode == UP:
            self.isStopFireworkTop = not self.isStopFireworkTop
        elif keyCode == DOWN:
            self.isStopFireworkBottom = not self.isStopFireworkBottom

    def mousePressed(self):
        pass
        
    def mouseWheel(self, event):
        self.isWheelControl = True
        if event.count < 0:
            Page.getCurrentPage().increseTint()
        else:
            Page.getCurrentPage().decreseTint()
