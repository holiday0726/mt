from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page

class Page2:
    def __init__(self):
        self.content = Content()
        self.migyung = Migyung()
        self.rocket = Rocket()
        self.migyung.load_image()
        self.rocket.load_image()
        
        self.rocket.set_x(100)\
            .set_y(400)
        
        self.textImage = loadImage("text1.png")
        
        self.stars = []
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
    
    def render(self):
        cursor()
        
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
            
        image(self.textImage, 100, 200, 500, 130)
        
        self.migyung.set_x(self.rocket.x + self.migyung.w)\
            .set_y(self.rocket.y + self.migyung.h)\
            .render()
        
        self.rocket.set_x_dir(1)\
            .set_y_dir(-1)\
            .render()\
            .particle()
        
        if self.rocket.is_collide_by_top() or self.rocket.is_collide_by_right():
            self.rocket.set_x_dir(0)\
                .set_y_dir(0)\
                .set_x(-300)\
                .set_y(-300)\
                .render()\
                .particle_stop()
            Page.next()
