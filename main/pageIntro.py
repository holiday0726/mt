class PageIntro:
    def __init__(self):
        self.introImage = loadImage("intro.png")

    def render(self):
        image(self.introImage, 0, 0, 1000, 800)
        
