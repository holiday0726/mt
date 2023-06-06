add_library("sound")
from processing.sound import SoundFile

from page import Page
from page0 import Page0
from page1 import Page1
from page2 import Page2
from page3 import Page3

backgroundColor = 0

def setup():
    size(1000, 800)
    frameRate(60)
    SoundFile(this, "oseann.wav").play()
    Page.extendPage([Page0(), Page1(), Page2(), Page3()])
    
def draw():
    global backgroundColor
    background(backgroundColor)
    Page.getCurrentPage().render()

def keyPressed():
    if keyCode == CONTROL and Page.currentPageNum < Page.getTotalPageNum()-1: Page.next()
    Page.getCurrentPage().keyPressed()

def mouseWheel(event):
    global backgroundColor

    if event.count < 0:
        if backgroundColor <=30: backgroundColor += 3
    else:
        if backgroundColor >=3: backgroundColor -= 3

def mousePressed():    
    Page.getCurrentPage().mousePressed()
