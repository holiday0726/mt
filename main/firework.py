from fireworkParticle import FireworkParticle
from processing.sound import SoundFile

class Firework:
    def __init__(self, x, y, gravity):
        self.hue = random(255)
        self.gravity = gravity
        self.firework = FireworkParticle(x, y, self.hue, False)
        self.exploded = False
        self.isSoundPlayed = False
        self.soundFile = SoundFile(this, "explosion.mp3")
        self.particles = []

    def done(self):
        return self.exploded and all(p.done() for p in self.particles)

    def update(self):
        if not self.exploded:
            self.firework.apply_force(self.gravity)
            self.firework.update()

            print(self.firework.vel.y)
            if self.firework.vel.y >= -1.2:
                if not self.isSoundPlayed:
                    self.isSoundPlayed = True
                    self.soundFile.play()
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
