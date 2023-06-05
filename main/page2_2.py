from content import Content
from customImage import CustomImage
from page import Page
from firework import Firework

class Page2_2:
    def __init__(self):
        self.stars = []
        self.fireworks = []
        
        self.migyung2 = CustomImage()
        self.migyung3 = CustomImage()
        self.migyung2.load_image("migyung2")
        self.migyung3.load_image("migyung3")
        
        self.migyungCnt = 0
        self.migyungs = []
        
        self.migyung2.set_x(400)\
            .set_y(600)\
            .set_w(self.migyung2.w/2)\
            .set_h(self.migyung2.h/2)
        
        self.migyung3.set_x(600)\
            .set_y(600)\
            .set_w(151/2)\
            .set_h(190/2)
            
        self.migyungs.append(self.migyung2)
        self.migyungs.append(self.migyung3)
        
        self.undukImage = loadImage("unduk.png")
        
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(400)))
            
        self.myMigyung = CustomImage()
        self.myMigyung.load_image("migyung9")
        self.myMigyung.set_x(500)\
            .set_y(600)\
            .set_w(130/2)\
            .set_h(190/2)
            
        self.mangone = CustomImage()
        self.mangone.load_image("mangone")
        self.mangone.set_x(100)\
            .set_y(550)\
            .set_w(170)\
            .set_h(190)
            
        self._camera = CustomImage()
        self._camera.load_image("camera")
        self._camera.set_x(720)\
                    .set_y(670)\
                    .set_w(53)\
                    .set_h(38)
        self.isCapture = False
        
    def makeMigyung2(self, x , y):
        migyung = CustomImage()
        self.migyungCnt = self.migyungCnt + 1
        migyung.load_image("migyung"+ str(self.migyungCnt % 9))
        if(self.migyungCnt % 9 == 0):
            migyung.set_w(190/2)\
                .set_h(130/2)\
                .set_x(x - migyung.w/2)\
                .set_y(y - migyung.h/2)
        else:
            migyung.set_w(migyung.w/2)\
                .set_h(migyung.h/2)\
                .set_x(x - migyung.w/2)\
                .set_y(y - migyung.h/2)
        self.migyungs.append(migyung)
        
    def render(self):
        
        colorMode(HSB)
        # Draw gradient sky
        #setGradient(0, 0, width, height, color(0, 0, 0), color(0, 0, 64))
        background(0)
        
        # Draw fireworks
        if random(1) < 0.07:
            self.fireworks.append(Firework())
    
        for firework in self.fireworks[:]:
            firework.update()
            firework.show()
    
            if firework.done():
                self.fireworks.remove(firework)
                
        image(self.undukImage, 0, 400, 1000, 400)
        
        for migyung in self.migyungs:
            migyung.render()
        
        
        self.myMigyung.render()
        self.mangone.render()
        self._camera.render()
        
        # Draw stars
        stroke(255)
        strokeWeight(random(2,3))
        for s in self.stars:
            point(s.x, s.y)
            
        if self.isCapture:
            stroke(255)
            strokeWeight(50)
            rect(200,200,600,400)
            image(loadImage("capture.png"), 200, 200, 600, 400)
            strokeWeight(10)
            circle(810,200,75)
            line(820,210,800,190)
            line(800,210,820,190)
            
