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
            
        self.gaugePercent = 0.00
        self.gaugeHeight = 300   
        self.gaugeWidth = 50    
        self.gaugeX = 800         
        self.gaugeY = 250 
        frameRate(50000)
    
    def increseGauge(self):
        self.gaugePercent += 0.005
        if (self.gaugePercent >= 1):
            self.gaugePercent == 1
            
        
    def render(self):
        cursor()
        #Page.next()
        colorMode(HSB)
        background(0)
        
        
        #Draw gauge
        colorMode(RGB)
        rectMode(CORNER)  
        fill(255)
        noStroke()
        rect(self.gaugeX, self.gaugeY, self.gaugeWidth, self.gaugeHeight, 10)  
        fill(100, 100, 200)
        noStroke()
        rect(self.gaugeX, self.gaugeY + (1-self.gaugePercent) * self.gaugeHeight, self.gaugeWidth, self.gaugePercent * self.gaugeHeight, 10)
        textSize(20)
        textAlign(CENTER, CENTER)
        fill(0)
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
        
        image(self.textImage, 100, 300, 300, 60)
        if self.firework.done():
            firework = None
            Page.next()
            
     
