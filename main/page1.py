from page import Page
from firstFirework import FirstFirework
from Star import Star
from Building import Building
from Text import Text
from Gauge import Gauge

class Page1:
    def __init__(self):
        self.star = Star(width, height)       
        self.building = Building(0, 600, 1000, 202)
        self.text = Text(100, 250, 517, 81)
        self.firework = FirstFirework()        
        self.gauge = Gauge(880, 250, 30, 300)
       
        self.backgroundColor = 0
        
    def render(self):
        cursor()

        self.gauge.render()
        self.star.render()

        isDone = self.firework.render()
        if isDone: firework = None; Page.next()
        
        self.text.render()
        self.building.render()
    
    ######################
    #define Function Area#
    ######################
    
    def increseGauge(self):
        self.gaugePercent = str(self.gauge.increse())
        
        if self.gaugePercent == str(20.0):
            self.text.setW(342).setH(36).next()
        elif self.gaugePercent == str(40.0):
            self.text.setW(571).setH(38).next()
        elif self.gaugePercent == str(60.0):
            self.text.setW(252).setH(35).next()
        elif self.gaugePercent == str(80.0):
            self.text.setW(569).setH(35).next()
        elif self.gaugePercent == str(100.0):
            self.gauge.exist = False
    
    #####################
    #event Function Area#
    #####################
    
    def keyPressed(self):
        if not self.firework.exploded:
            self.firework.update()
            self.increseGauge()
            
    def mousePressed(self):
        if mouseY > 600: self.building.next()
