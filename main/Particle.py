from random import uniform, randint

class Particle:
    def __init__(self, l, acc, vel):
        self.acceleration = acc
        self.vel = vel
        self.position = l.copy()
        self.lifespan = 255.0

    def run(self, r, g, b):
        self.update()
        self.display(r, g, b)

    def update(self):
        self.vel.add(self.acceleration)
        #self.position.add(self.velocity)
        self.position.add(PVector.mult(self.vel, 0.1))
        
        self.lifespan -= 3

    def display(self, r, g, b):
        noStroke()
        fill(r, g, b, self.lifespan)
        ellipse(self.position.x, self.position.y, 8, 8)

    def isDead(self):
        return self.lifespan < 0.0
