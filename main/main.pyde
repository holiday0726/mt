from migyung import Migyung
from rocket import Rocket
from page import Page
from content import Content
from pageIntro import PageIntro
#from page0 import Page0
#from page1 import Page1
from page1_1 import Page1_1
from page2_2 import Page2_2
#from page2 import Page2
#from page3 import Page3
from page4 import Page4
from firstFirework import FirstFirework

migyung = Migyung()
rocket = Rocket()
content = Content()
pageIntro = 0
pages = Page.pages

def setup():
    pageIntro = PageIntro()
    #page0 = Page0()
    #page1 = Page1()
    page1_1 = Page1_1()
    page2_2 = Page2_2()
    #page2 = Page2()
    #page3 = Page3()
    page4 = Page4()
    size(1000, 800)
    pages.extend([pageIntro, page1_1, page2_2])

def draw():
    background(0)
    pages[Page.current].render()

def keyPressed():
    current = Page.current;
    
    if current == 1:
        if not pages[current].firework.exploded:
            pages[current].firework.update()
            
    if current == 2:
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
                myMigyung.y = myMigyung.y - 10
        elif (keyCode == DOWN) :
            if(myMigyung.y <= height - myMigyung.h):
                myMigyung.y = myMigyung.y + 10
        
    
def mousePressed():
    #if len(pages) - 1 == Page.current:
        #return
    
    if Page.current == 0:
        if mouseX > 550 and mouseX < 750:
            if mouseY > 500 and mouseY < 650:
                noCursor()
                Page.next()
        
    if Page.current == 1:
        #Page.next()
        pass
        #rocket = pages[Page.current].rocket
        #if rocket.x < mouseX < rocket.x + rocket.w and rocket.y - rocket.h/2 < mouseY < rocket.y + rocket.h/2:
            #Page.next()
    if Page.current == 2:
        if(500 <= mouseY ):
            pages[Page.current].makeMigyung2(mouseX, mouseY)
    # else:
    #     Page.next()
