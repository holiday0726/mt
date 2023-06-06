from FireworkParticle import FireworkParticle
from processing.sound import SoundFile

class Firework:
    def __init__(self, x, y, gravity):
        self.hue = random(255)
        self.gravity = gravity
        self.fireworkParticle = FireworkParticle(x, y, self.hue, False)
        self.exploded = False
        self.isSoundPlayed = False
        self.soundFile = SoundFile(this, "explosion.mp3")
        self.particles = []

    def isDone(self):
        return self.exploded and all(particle.isDone() for particle in self.particles)

    def update(self):
        if not self.exploded:
            self.fireworkParticle.applyForce(self.gravity)
            self.fireworkParticle.update()
            self.explode()
        else:
            for particle in self.particles:
                particle.applyForce(self.gravity)
                particle.update()
    
    # Added conditional due to sync issue
    def playSound(self):
        if not self.isSoundPlayed:
            if self.fireworkParticle.velocity.y >= -1.2: 
                self.isSoundPlayed = True
                self.soundFile.play()
                
    def explode(self):
        self.playSound()
        if self.fireworkParticle.velocity.y >= 0:
            self.exploded = True
            for i in range(300):
                self.particles.append(FireworkParticle(self.fireworkParticle.position.x, self.fireworkParticle.position.y, self.hue, True))
        
    def show(self):
        if not self.exploded:
            self.fireworkParticle.show()

        for particle in self.particles:
            particle.show()
            
    def render(self):
        colorMode(HSB)
        self.update()
        self.show()
        colorMode(RGB)
        return self.isDone()

    def setGradient(self, x, y, w, h, color1, color2):
        noFill()
        for i in range(h):
            interpolation = map(i, 0, h, 0, 1)
            color = lerpColor(color1, color2, interpolation)
            stroke(color)
