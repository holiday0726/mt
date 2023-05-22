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
    
    def render(self):
        cursor()
        self.content.set_size(32)\
            .set_x(200)\
            .set_y(300)\
            .set_content("page2")\
            .render()
        
        self.migyung.set_x(self.rocket.x + self.migyung.w)\
            .set_y(self.rocket.y + self.migyung.h)\
            .render()
        
        self.rocket.set_x_dir(1)\
            .set_y_dir(-1)\
            .render()\
            .particle()
        
        print(self.rocket.x, self.rocket.y)
        
        if self.rocket.is_collide_by_top() or self.rocket.is_collide_by_right():
            self.rocket.set_x_dir(0)\
                .set_y_dir(0)\
                .set_x(-300)\
                .set_y(-300)\
                .render()\
                .particle_stop()
            Page.next()
