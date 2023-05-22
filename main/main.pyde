from migyung import Migyung
from rocket import Rocket
from page import Page
from content import Content
from page0 import Page0
from page1 import Page1
from page2 import Page2
from page3 import Page3

migyung = Migyung()
rocket = Rocket()
content = Content()
page0 = 0
page1 = 0
page2 = 0
page3 = 0
pages = Page.pages

def setup():
    global page0, page1, page2, page3
    page0 = Page0()
    page1 = Page1()
    page2 = Page2()
    page3 = Page3()
    noCursor()
    size(1000, 800)
    pages.extend([page0, page1, page2, page3])

def draw():
    global page0, page1, page2, page3
    background(0)
    pages[Page.current].render()
    print(Page.current)

def mousePressed():
    if len(pages) - 1 == Page.current:
        return
    if Page.current == 0:
        rocket = pages[Page.current].rocket
        if rocket.x < mouseX < rocket.x + rocket.w and rocket.y - rocket.h/2 < mouseY < rocket.y + rocket.h/2:
            Page.next()
    # else:
    #     Page.next()
