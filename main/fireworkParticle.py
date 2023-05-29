class FireworkParticle:
    def __init__(self, x, y, hue, exploded):
        self.pos = PVector(x, y)
        self.exploded = exploded
        self.lifespan = 255
        self.hue = hue

        if not self.exploded:
            self.vel = PVector(random(-3, 3), random(-18, -5))
        else:
            self.vel = self.random2D()
            self.vel.mult(random(2, random(20,30)))

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
