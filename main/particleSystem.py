from particle import Particle

class ParticleSystem:
    def __init__(self, position):
        self.origin = position.copy()
        self.particles = []
        self.is_stop = False
        
    def move(self, position):
        self.origin = position.copy()

    def add_particle(self):
        if not self.is_stop:
            self.particles.append(Particle(self.origin))
        
    def stop(self):
        self.particles.pop()
        self.is_stop = True

    def run(self):
        self.is_stop = False
        
        for i in range(len(self.particles) - 1, -1, -1):
            p = self.particles[i]
            p.run()
            if p.is_dead():
                self.particles.pop(i)
