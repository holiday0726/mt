from firstFireworkParticle import FirstFireworkParticle

class FirstFirework:
    def __init__(self):
        self.hue = 42.5
        self.sat = 255
        self.gravity = PVector(0, 0.2)
        self.firework = FirstFireworkParticle(width/2-100, height, self.hue,self.sat, False, 50)
        self.exploded = False
        self.particles = []
        self.count = 0

    def done(self):
        return self.exploded and all(p.done() for p in self.particles)

    def update(self):
        if not self.exploded:
            self.firework.apply_force(self.gravity)
            self.firework.update()

            if self.count >= 300:
                self.exploded = True
                self.explode()

        for particle in self.particles:
            particle.apply_force(self.gravity)
            particle.update()
        
        self.count = self.count +1
        
    def explode(self):
        for _ in range(1000):
            p = FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 21.25, 0, True, 40)
            self.particles.append(p)
        
        for _ in range(1000):
            p2 = FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 42.5, self.sat, True, 30)
            self.particles.append(p2)

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
