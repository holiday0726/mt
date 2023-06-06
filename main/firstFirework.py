from firstFireworkParticle import FirstFireworkParticle
from processing.sound import SoundFile

class FirstFirework:
    def __init__(self):
        self.hue = 42.5
        self.saturation = 255
        self.brightness = 255
        self.gravity = PVector(0, 0.2)
        self.firework = FirstFireworkParticle(width / 2 - 50, height, self.hue, self.saturation, self.brightness, False, 50)
        self.exploded = False
        self.soundFile = SoundFile(this, "firstFirework.wav")
        self.particles = []
        self.count = 0

    def render(self):
        colorMode(HSB)
        if self.exploded:
            self.update()
        self.show()
        colorMode(RGB)
        return self.isDone()
    
    def isDone(self):
        return self.exploded and all(particle.isDone() for particle in self.particles)

    def update(self):
        if not self.exploded:
            self.firework.applyForce(self.gravity)
            self.firework.update(self.count)
            if self.count >= 199:
                self.explode()
            
            self.count += 1

        for particle in self.particles:
            particle.applyForce(self.gravity)
            particle.update(0)
        
    def explode(self):
        self.soundFile.play()
        self.exploded = True
            
        for i in range(400):
            self.addParticle(42.5, 0, 30)
            self.addParticle(40.5, 0, 30)
            self.addParticle(38.5, 0, 30)
            
        for i in range(80):
            self.addParticle(42.5, self.saturation, 20)
            self.addParticle(40.5, self.saturation, 20)
            self.addParticle(38.5, self.saturation, 15)
            self.addParticle(36.5, self.saturation, 15)
            self.addParticle(34.5, self.saturation, 15)
    
    def addParticle(self, hue, saturation, lifespan):
        self.particles.append(FirstFireworkParticle(self.firework.position.x, self.firework.position.y, hue, saturation, 255, True, lifespan))

    def show(self):
        self.firework.show()

        for particle in self.particles:
            particle.show()
