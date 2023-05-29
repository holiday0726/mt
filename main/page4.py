from content import Content
from migyung import Migyung
from rocket import Rocket
from page import Page

class Page4:
    def __init__(self):
        self.stars = []
        self.fireworks = []

        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(width), random(height)))
    
    def render(self):
        colorMode(HSB)
        # Draw gradient sky
        #setGradient(0, 0, width, height, color(0, 0, 0), color(0, 0, 64))
        background(0)
        # Draw stars
        stroke(255)
        strokeWeight(2)
        for s in self.stars:
            point(s.x, s.y)
        
        # Draw fireworks
        if random(1) < 0.03:
            self.fireworks.append(Firework())
    
        for firework in self.fireworks[:]:
            firework.update()
            firework.show()
    
            if firework.done():
                self.fireworks.remove(firework)


class FireworkParticle:
    def __init__(self, x, y, hue, exploded):
        self.pos = PVector(x, y)
        self.exploded = exploded
        self.lifespan = 255
        self.hue = hue

        if not self.exploded:
            self.vel = PVector(0, random(-15, -5))
        else:
            self.vel = self.random2D()
            self.vel.mult(random(2, 20))

        self.acc = PVector(0, 0)

    def apply_force(self, force):
        self.acc.add(force)

    def update(self):
        if self.exploded:
            self.vel.mult(0.9)
            self.lifespan -= 4

        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def done(self):
        return self.lifespan < 0

    def show(self):
        if not self.exploded:
            strokeWeight(4)
            stroke(self.hue, 255, 255)
        else:
            strokeWeight(random(4))
            stroke(self.hue, 255, 255, self.lifespan)

        point(self.pos.x, self.pos.y)
    
    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))


class Firework:
    def __init__(self):
        self.hue = random(255)
        self.gravity = PVector(0, 0.2)
        self.firework = FireworkParticle(random(width), height, self.hue, False)
        self.exploded = False
        self.particles = []

    def done(self):
        return self.exploded and all(p.done() for p in self.particles)

    def update(self):
        if not self.exploded:
            self.firework.apply_force(self.gravity)
            self.firework.update()

            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()

        for particle in self.particles:
            particle.apply_force(self.gravity)
            particle.update()

    def explode(self):
        for _ in range(300):
            p = FireworkParticle(self.firework.pos.x, self.firework.pos.y, self.hue, True)
            self.particles.append(p)

    def show(self):
        if not self.exploded:
            self.firework.show()

        for particle in self.particles:
            particle.show()
                
    def setGradient(x, y, w, h, c1, c2):
        noFill()
        for i in range(h):
            inter = map(i, 0, h, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
