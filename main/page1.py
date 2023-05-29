from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page

class Page1:
    def __init__(self):
        self.frame_rate = 200
        self.content = Content()
        self.migyung = Migyung()
        self.rocket = Rocket()
        self.migyung.load_image()
        self.rocket.load_image()
        
        frameRate(self.frame_rate)
    
    def render(self):

        self.migyung.set_x(self.rocket.x + self.migyung.w) \
            .set_y(self.rocket.y + self.migyung.h) \
            .render()

        self.rocket.set_x_dir(1) \
            .set_y_dir(-1) \
            .render() \
            .particle()

        if self.rocket.is_collide_by_top() or self.rocket.is_collide_by_right():
            self.rocket.particle_stop()
            self.rocket.set_x(100).set_y(500)
            Page.next()
