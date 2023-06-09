class FireworkParticle:
    def __init__(self, x, y, hue, isExploded):
        self.position = PVector(x, y)
        self.isExploded = isExploded
        self.lifeSpan = 255
        self.hue = hue

        if not self.isExploded:
            self.velocity = PVector(random(-3, 3), random(-18, -5))
        else:
            self.velocity = self.random2D()
            self.velocity.mult(random(2, random(20,30)))

        self.acceleration = PVector(0, 0)

    def applyForce(self, force):
        self.acceleration.add(force)

    def update(self):
        if self.isExploded:
            self.velocity.mult(0.9)
            self.lifeSpan -= 4

        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def isDone(self):
        return self.lifeSpan < 0

    def show(self):
        if not self.isExploded:
            strokeWeight(4)
            stroke(self.hue, 255, 255)
        else:
            strokeWeight(random(4))
            stroke(self.hue, 255, 255, self.lifeSpan)

        point(self.position.x, self.position.y)

    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))
