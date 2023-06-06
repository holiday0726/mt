from random import uniform, randint

class Particle:
    def __init__(self, l):
        self.acceleration = PVector(0, 0.05)
        self.velocity = PVector(uniform(-1, 2), uniform(-1, 2))
        self.position = l.copy()
        self.lifespan = 255.0

    def run(self):
        self.update()
        self.display()

    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.lifespan -= 4.5

    def display(self):
        # stroke(0, self.lifespan)
        noStroke()
        rand = randint(1, 4)
        if rand == 1:
            fill(255, self.lifespan)
        else:
            fill(255, 0, 0, self.lifespan)
        r = 10
        ellipse(self.position.x + randint(-10, 11), self.position.y, r, r)

    def is_dead(self):
        return self.lifespan < 0.0
