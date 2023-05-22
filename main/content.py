class Content:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 200
        self.h = 50
        self.size = 0
        self.content = ""

    def render(self):
        fill(255)
        textSize(self.size)
        text(self.content, self.x, self.y, self.w, self.h)
        return self

    def set_size(self, size):
        self.size = size
        return self

    def set_content(self, content):
        self.content = content
        return self

    def set_x(self, x):
        self.x = x
        return self

    def set_y(self, y):
        self.y = y
        return self
