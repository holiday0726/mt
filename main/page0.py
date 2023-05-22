from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page

class Page0:
    def __init__(self):
        self.frame_rate = 500
        self.content = Content()
        self.migyung = Migyung()
        self.rocket = Rocket()
        self.migyung.load_image()
        self.rocket.load_image()
        frameRate(self.frame_rate)

    def render(self):
        self.rocket.render().change_dir()
        self.migyung.set_x(mouseX).set_y(mouseY).render()
