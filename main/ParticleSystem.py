from Particle import Particle

class ParticleSystem:
    def __init__(self, position):
        self.origin = position.copy()
        self.particles = []
        self.isStop = False

    def addParticle(self, acc, vel):
        if not self.isStop:
            self.particles.append(Particle(self.origin, acc, vel))
        
    def stop(self):
        if len(self.particles) <> 0:
            self.particles.pop()
        self.isStop = True

    def run(self, r, g, b):
        self.isStop = False
        
        for i in range(len(self.particles) - 1, -1, -1):
            p = self.particles[i]
            p.run(r, g, b)
            if p.isDead():
                self.particles.pop(i)
