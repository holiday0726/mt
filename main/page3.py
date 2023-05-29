from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page

class Page3:
    def __init__(self):
        self.frame_rate = 8000
        self.content = Content()
        self.migyung = Migyung()
        self.rocket = Rocket()
        self.migyung.load_image()
        self.rocket.load_image()
        self.rockets = []
        self.migyungs = []
        frameRate(self.frame_rate)
        
        self.stars = []
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
            
        for i in range(10):
            rand = random(500, 1000)
            self.rockets.append(Rocket())
            self.migyungs.append(Migyung())
            
            self.migyungs[i].load_image() \
                .set_x(self.rockets[i].x + self.migyungs[i].w) \
                .set_y(self.rockets[i].y + self.migyungs[i].h) \
                .render()
                    
            self.rockets[i].load_image() \
                .set_x_dir(2) \
                .set_y_dir(-2) \
                .set_x(random(width) - rand/2) \
                .set_y(rand) \
                .render() \
                .particle()
        
    def render(self):
        
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
            
        self.content.set_size(32) \
            .set_x(200) \
            .set_y(300) \
            .set_content("page3") \
            .render()
        
        for i, value in enumerate(self.migyungs):
            self.migyungs[i].set_x(self.rockets[i].x + self.migyungs[i].w) \
                .set_y(self.rockets[i].y + self.migyungs[i].h) \
                .render()
            self.rockets[i].render().particle()
        
        if all(rocket.is_collide_by_top() or rocket.is_collide_by_right() for rocket in self.rockets):
            Page.next()
