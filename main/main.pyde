add_library("sound")

#from migyung import Migyung
#from rocket import Rocket
from page import Page
#from content import Content
from pageIntro import PageIntro
#from page0 import Page0
#from page1 import Page1
#from page2 import Page2
#from page3 import Page3
#from page4 import Page4
from page1_1 import Page1_1
from page2_2 import Page2_2
from page3_3 import Page3_3
from processing.sound import SoundFile

#migyung = Migyung()
#rocket = Rocket()
#content = Content()
pageIntro = 0
pages = Page.pages

def setup():
    pageIntro = PageIntro()
    #page0 = Page0()
    #page1 = Page1()
    #page2 = Page2()
    #page3 = Page3()
    #page4 = Page4()
    page1_1 = Page1_1()
    page2_2 = Page2_2()
    page3_3 = Page3_3()
    size(1000, 800)
    pages.extend([pageIntro, page1_1, page2_2, page3_3])
    baseSound = SoundFile(this, "oseann.wav")
    baseSound.play()
    
def draw():
    background(0)
    pages[Page.current].render()
def keyPressed():
    current = Page.current
                    
    if current == 1:
        if not pages[current].firework.exploded:
            pages[current].firework.update()
            pages[current].increseGauge()
            
    if current == 2:
        if pages[current].isCapture:
            return
        
        myMigyung = pages[current].myMigyung
        if (keyCode == LEFT) :
            if(myMigyung.x >= 0):
                myMigyung.load_image('migyung9')
                myMigyung.x = myMigyung.x - 10
        elif (keyCode == RIGHT) :
            if(myMigyung.x <= width - myMigyung.w):
                myMigyung.load_image('migyung10')
                myMigyung.x = myMigyung.x + 10
        elif (keyCode == UP) :
            if(myMigyung.y >= 500):
                myMigyung.load_image('migyung11')
                myMigyung.y = myMigyung.y - 10
        elif (keyCode == DOWN) :
            if(myMigyung.y <= height - myMigyung.h):
                myMigyung.load_image('migyung9')
                myMigyung.y = myMigyung.y + 10
                
        if keyCode == SHIFT:
            if myMigyung.x >= 40 and myMigyung.x <= 120:
                if myMigyung.y == 620:
                    Page.next()
        
            if myMigyung.x >= 700 and myMigyung.x <= 800:
                if myMigyung.y >= 520 and myMigyung.y <= 580:
                    saveFrame("capture.png")
                    fill(255,0,200)
                    rect(0,0, width, height)
                    noFill()
                    pages[current].isCapture = True
            
    
    if current == 3:
        if keyCode == ALT:
            pages[current].appendFireWork()
        if keyCode == LEFT :
            pages[current].mangoneX = pages[current].mangoneX - 20
        if keyCode == RIGHT :
            pages[current].mangoneX = pages[current].mangoneX + 20
        if keyCode == UP :
            pages[current].mangoneY = pages[current].mangoneY - 20
        if keyCode == DOWN :
            pages[current].mangoneY = pages[current].mangoneY + 20
            
    if keyCode == CONTROL:
        if current < 3:
            Page.next()

def mouseWheel(event):
    
    current = Page.current
    
    if Page.current == 1:
        if event.count < 0:
            pages[current].backPlus()
        else:
            pages[current].backMinus()
            
    if Page.current == 3:
        if event.count < 0:
            pages[current].zoom += 10
        else:
            pages[current].zoom -= 10

def mousePressed():
    
    current = Page.current
    
    #if len(pages) - 1 == Page.current:
        #return
    
    if Page.current == 0:
        if mouseX > 446 and mouseX < 770:
            if mouseY > 520 and mouseY < 680:
                noCursor()
                Page.next()
        
    if current == 1:
        if mouseY>600:
            pages[Page.current].changeBuliding()
        #rocket = pages[Page.current].rocket
        #if rocket.x < mouseX < rocket.x + rocket.w and rocket.y - rocket.h/2 < mouseY < rocket.y + rocket.h/2:
            #Page.next()
    if current == 2:
        if 500 <= mouseY :
            pages[Page.current].makeMigyung2(mouseX, mouseY)
        if mouseX >= 800 and mouseX <=820:
            if mouseY >= 190 and mouseY <= 210:
                pages[Page.current].isCapture = False
    # else:
    #     Page.next()
