from firstFireworkParticle import FirstFireworkParticle

class FirstFirework:
    def __init__(self):
        self.hue = 42.5
        self.sat = 255
        self.b = 255
        self.gravity = PVector(0, 0.2)
        self.firework = FirstFireworkParticle(width/2-50, height, self.hue, self.sat, self.b, False, 50)
        self.exploded = False
        self.particles = []
        self.count = 0

    def done(self):
        return self.exploded and all(p.done() for p in self.particles)

    def update(self):

        if not self.exploded:
            
            self.firework.apply_force(self.gravity)
            self.firework.update(self.count)
            if self.count >= 200:
                self.exploded = True
                self.explode()
            self.count = self.count +1

        for particle in self.particles:
            particle.apply_force(self.gravity)
            particle.update(0)
        
        
        
    def explode(self):
        
        for _ in range(800):
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 42.5, 0, 255, True, 30))
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 40.5, 0, 255, True, 30))
            
        for _ in range(100):
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 42.5, self.sat, 255, True, 20))
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 40.5, self.sat, 255, True, 20))
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 38.5, self.sat, 255, True, 15))
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 36.5, self.sat, 255, True, 15))
            self.particles.append(FirstFireworkParticle(self.firework.pos.x, self.firework.pos.y, 34.5, self.sat, 255, True, 15))
        

    def show(self):
        #if not self.exploded:
        self.firework.show()

        for particle in self.particles:
            particle.show()
                
    def setGradient(x, y, w, h, c1, c2):
        noFill()
        for i in range(h):
            inter = map(i, 0, h, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
