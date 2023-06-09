add_library("sound")
from processing.sound import SoundFile

from Page import Page
from Page0 import Page0
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3

def setup():
    size(1000, 800)
    frameRate(60)
    SoundFile(this, "oseann.wav").play()
    Page.extendPage([Page0(), Page1(), Page2(), Page3()])
    
def draw():
    background(Page.backgroundColor)
    Page.getCurrentPage().render()

def keyPressed():
    if keyCode == CONTROL and Page.currentPageNum < Page.getTotalPageNum()-1: Page.next()
    Page.getCurrentPage().keyPressed()

def mouseWheel(event):
    Page.getCurrentPage().mouseWheel(event)
        

def mousePressed():    
    Page.getCurrentPage().mousePressed()
