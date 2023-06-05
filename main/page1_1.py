from content import Content
from page import Page
from firstFirework import FirstFirework
from processing.sound import SoundFile

class Page1_1:
    def __init__(self):
        self.stars = []
        self.firework = FirstFirework()
        self.currentImage = loadImage("text4.png")
        self.currentBuilding = 0
        self.buildingList = ["building1.png","building2.png","building3.png","building4.png"]
        self.buildingImage = loadImage("building1.png")
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
        self.sf = SoundFile(this,"explosion.mp3")
       
        self.backgroundColor = 0
        self.gaugeExist = True;
        self.gaugePercent = 0.00
        self.gaugeHeight = 300   
        self.gaugeWidth = 30    
        self.gaugeX = 880         
        self.gaugeY = 250 
        
        self.imageX = 100
        self.imageY = 250
        self.imageW = 0
        self.imageH = 0
        
        self.builX = 0
        self.builY = 0
        self.builW = 0
        self.builH = 0
        
        frameRate(60)
    
    def renderImage(self, content): 
        self.currentImage = loadImage(content)
    
    def increseGauge(self):
        self.gaugePercent += 0.005
        
        if self.gaugePercent <= 0.195:
            self.imageW = 517
            self.imageH = 81
            self.renderImage('text4.png')
        
        if self.gaugePercent >= 0.2 and self.gaugePercent < 0.395:
            self.imageW = 342
            self.imageH = 36
            self.renderImage('text5.png')
            
        elif self.gaugePercent >= 0.4 and self.gaugePercent < 0.595:
            self.imageW = 571
            self.imageH = 38
            
            self.renderImage('text2.png')
            
        elif self.gaugePercent >= 0.6 and self.gaugePercent < 0.795:
            self.imageW = 252
            self.imageH = 35
            self.renderImage('text1.png')
            
        elif self.gaugePercent >= 0.8 and self.gaugePercent < 0.995:
            self.imageW = 569
            self.imageH = 35
            self.renderImage('text3.png')
            
        if self.gaugePercent >= 0.995:
            self.gaugePercent == 1.1
            self.gaugeExist = False
            self.sf.play()
            
    def backPlus(self):
        if self.backgroundColor <=45:
            self.backgroundColor += 3
        
    def backMinus(self):
        if self.backgroundColor >=3:
            self.backgroundColor -= 3
        
    def changeBuliding(self):
        self.currentBuilding +=1
        if (self.currentBuilding==3):
            self.currentBuilding =0
    
    def drawBuilding(self):
        self.builX=0
        self.builY=600
        self.builW=1000
        self.builH=202
        self.buildingImage = loadImage(self.buildingList[self.currentBuilding])
        image(self.buildingImage, self.builX, self.builY, self.builW, self.builH)
    
    def render(self):
        cursor()
        #Page.next()
        colorMode(HSB)
        background(self.backgroundColor)

        #Draw gauge
        
        if self.gaugeExist:
            
            colorMode(RGB)
            rectMode(CORNER)  
            fill(255)
            noStroke()
            rect(self.gaugeX, self.gaugeY, self.gaugeWidth, self.gaugeHeight, 10)  
            fill(255, 255, 0)
            noStroke()
            rect(self.gaugeX, self.gaugeY + (1-self.gaugePercent) * self.gaugeHeight, self.gaugeWidth, self.gaugePercent * self.gaugeHeight, 10)
            textSize(20)
            textAlign(CENTER, CENTER)
            fill(52)
            text(str(int(self.gaugePercent * 100)), self.gaugeX + self.gaugeWidth/2, self.gaugeY + self.gaugeHeight/2)
        
        
        # Draw stars
        colorMode(HSB)
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)

        # Draw fireworks)
        if self.firework.exploded:
            self.firework.update()
        self.firework.show()
        
        image(self.currentImage, self.imageX, self.imageY, self.imageW, self.imageH)
        self.drawBuilding()
        if self.firework.done():
            firework = None
            Page.next()
            
     
