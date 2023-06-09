from Page import Page
from CustomImage import CustomImage
from Firework import Firework
from Star import Star

class Page2:
    def __init__(self):
        self.star = Star(width, 400)
        self.fireworks = []

        self.myMigyung = CustomImage().setX(500).setY(600).setW(130/2).setH(190/2).setImage("migyung9")
        self.mangone = CustomImage().setX(100).setY(550).setW(170).setH(190).setImage("mangone")
        self.camera = CustomImage().setX(720).setY(550).setW(70).setH(100).setImage("camera")
        self.unduk = CustomImage().setX(0).setY(400).setW(1000).setH(400).setImage("unduk")
        
        self.migyungCnt = 1
        self.migyungs = []
        self.makeMigyung(400,650)
        self.makeMigyung(600,650)
        self.isCapture = False
            
    def render(self):
    
        self.makeFireWork()
        
        for firework in self.fireworks[:]:
            isDone = firework.render()
            if isDone: self.fireworks.remove(firework)
            
        self.star.render()
        self.unduk.render()

        for migyung in self.migyungs:
            migyung.render()
        
        self.camera.render()
        self.myMigyung.render()
        self.mangone.render()
        
        if self.isCapture:
            self.makeCaptureWindow()
            
    ######################
    #define Function Area#
    ######################
    
    def makeMigyung(self, x , y):
        
        self.migyungCnt = self.migyungCnt + 1
        imageName = "migyung"+ str(self.migyungCnt % 9)
        if(imageName == "migyung0"):   w, h = 190/2, 130/2
        elif(imageName == "migyung3"): w, h = 151/2, 190/2
        else:                          w, h = 130/2, 190/2
        
        migyung = CustomImage().setX(x-w/2).setY(y-h/2).setW(w).setH(h).setImage(imageName)
        self.migyungs.append(migyung)
    
    def makeFireWork(self):
        if random(1) < 0.07:
            self.fireworks.append(Firework(random(width), height-200, PVector(0, 0.3)))
    
    def makeCaptureWindow(self):
        stroke(255)
        strokeWeight(50)
        fill(0)
        rect(200,200,600,400)
        image(loadImage("./resource/capture.png"), 200, 200, 600, 400)
        strokeWeight(10)
        circle(810,200,75)
        fill(0)
        line(820,210,800,190)
        line(800,210,820,190)
        noFill()
        
    def moveMyMigyung(self):
        if keyCode == LEFT and self.myMigyung.x >= 0:
            self.myMigyung.setImage('migyung9')
            self.myMigyung.x -= 10
        elif keyCode == RIGHT and self.myMigyung.x <= width - self.myMigyung.w:
            self.myMigyung.setImage('migyung10')
            self.myMigyung.x += 10
        elif keyCode == UP and self.myMigyung.y >= 500:
            self.myMigyung.setImage('migyung11')
            self.myMigyung.y -= 10
        elif keyCode == DOWN and self.myMigyung.y <= height - self.myMigyung.h:
            self.myMigyung.setImage('migyung9')
            self.myMigyung.y += 10
    
    #####################
    #event Function Area#
    #####################
    
    def keyPressed(self):
        if not self.isCapture:
            self.moveMyMigyung()
            if keyCode == SHIFT:
                if self.myMigyung.x >= 40 and self.myMigyung.x <= 120 and self.myMigyung.y == 620:
                    Page.next()
                if self.myMigyung.x >= 700 and self.myMigyung.x <= 800 and self.myMigyung.y >= 520 and self.myMigyung.y <= 580:
                    saveFrame("./resource/capture.png")
                    fill(255)
                    rect(0,0, width, height)
                    noFill()
                    self.isCapture = True
                    
    def mousePressed(self):
        if mouseY >= 500 : self.makeMigyung(mouseX, mouseY)
        if mouseX >= 800 and mouseX <=820 and mouseY >= 190 and mouseY <= 210: self.isCapture = False
        
    def mouseWheel(self, event):
        if event.count < 0:
            if Page.backgroundColor <=30: Page.backgroundColor += 3
        else:
            if Page.backgroundColor >=3: Page.backgroundColor -= 3
