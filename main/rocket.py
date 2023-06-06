from particleSystem import ParticleSystem

class Rocket:
    
    def __init__(self):
        self.image = None
        self.x = 100
        self.y = 400
        self.w = 180
        self.h = 250
        self.x_dir = 1
        self.y_dir = -1
        self.ps = ParticleSystem(PVector(self.x + self.w / 2, self.y + self.h - self.h/3))
        
    def load_image(self):
        self.image = loadImage("rocket.png")
        return self
    
    def render(self):
        #image(self.image, self.x, self.y, self.w, self.h)
        pushMatrix()
        translate(self.x, self.y)
        self.draw_head()
        self.draw_body()
        self.draw_left_tail()
        self.draw_right_tail()
        self.draw_bottom()
        self.draw_tail()
        popMatrix()
        self.x += self.x_dir
        self.y += self.y_dir
        return self
    
    def set_x(self, x):
        self.x = x
        return self
        
    def set_y(self, y):
        self.y = y
        return self
        
    def set_x_dir(self, x_dir):
        self.x_dir = x_dir
        return self

    def set_y_dir(self, y_dir):
        self.y_dir = y_dir  
        return self
    
    def is_collide_by_left(self):
        return self.x < 0 + self.w/2
    
    def is_collide_by_right(self):
        return self.x > width - self.w/2
        
    def is_collide_by_top(self):
        return self.y < 0 + self.h/2
    
    def is_collide_by_bottom(self):
        return self.y > height - self.h/2
    
    def change_dir(self):
        if self.is_collide_by_left() or self.is_collide_by_right():
            self.x_dir *= -1
        
        if self.is_collide_by_top() or self.is_collide_by_bottom():
            self.y_dir *= -1
            
        return self

    def particle_stop(self):
        self.ps.stop()
        return self
        
    def particle(self):
        #background(255)
        fill(255, 0, 0)
        self.ps.move(PVector(self.x + self.w / 2, self.y + self.h))
        self.ps.add_particle()
        self.ps.run()
        return self
        
    def draw_head(self):
        fill(255, 0, 0)
        stroke(255, 0, 0)
        strokeWeight(10)
        strokeJoin(ROUND)
        triangle(95, 15, 50, 85, 140, 85)
        noStroke()
        return self
    
    def draw_body(self):
        rectMode(CENTER)
        fill(255)
        beginShape()
        vertex(45, 85)
        vertex(145, 85)
        vertex(145, 210)
        vertex(45, 210)
        beginContour()
        for i in range(360, -1, -1):
            rad = radians(i)
            x = 95 + 37.5 * cos(rad)
            y = 145 + 37.5 * sin(rad)
            vertex(x, y)
        endContour()
        endShape(CLOSE)
        noFill()
        stroke(128)
        strokeWeight(5)
        ellipse(95, 145, 75, 75)
        noStroke()
        return self
    
    def draw_left_tail(self):
        fill(255, 0, 0)
        quad(45, 210, 45, 170, 0, 190, 0, 230)
        return self
    
    def draw_right_tail(self):
        fill(255, 0, 0)
        quad(145, 210, 145, 170, 190, 190, 190, 230)
        return self
    
    def draw_bottom(self):
        fill(128)
        arc(95, 210, 100, 100, 0, PI)
        return self
    
    def draw_tail(self):
        fill(255, 0, 0)
        quad(95, 190, 80, 240, 95, 290, 110, 240)
