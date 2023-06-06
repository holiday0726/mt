class Gauge:
    def __init__(self, x, y, w, h):
        self.exist = True
        self.count = 0
        self.persent = 0
        self.h = h   
        self.w = w
        self.x = x
        self.y = y 
    
    def increse(self):
        self.count += 1
        self.persent = self.count*10 / 2 * 0.1
        
        if self.count == 200:
            self.exist = False
        
        return self.persent
    
    def render(self):
        if self.exist:
            colorMode(RGB)
            rectMode(CORNER)  
            fill(255)
            noStroke()
            rect(self.x, self.y, self.w, self.h, 10)  
            fill(255, 255, 0)
            noStroke()
            rect(self.x, self.y + (1-(self.persent*0.01)) * self.h, self.w, (self.persent*0.01) * self.h, 10)
            textSize(20)
            textAlign(CENTER, CENTER)
            fill(52)
            text(str(int(self.persent)), self.x + self.w/2, self.y + self.h/2)
