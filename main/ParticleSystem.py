from Particle import Particle

class ParticleSystem:
    def __init__(self, position):
        self.origin = position.copy()
        self.particles = []
        self.is_stop = False

    def addParticle(self, acc, vel):
        if not self.is_stop:
            self.particles.append(Particle(self.origin, acc, vel))
        
    def stop(self):
        self.particles.pop()
        self.is_stop = True

    def run(self, r, g, b):
        self.is_stop = False
        
        for i in range(len(self.particles) - 1, -1, -1):
            p = self.particles[i]
            p.run(r, g, b)
            if p.is_dead():
                self.particles.pop(i)
