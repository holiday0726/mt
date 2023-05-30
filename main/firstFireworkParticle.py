class FirstFireworkParticle:
    def __init__(self, x, y, hue, exploded):
        self.pos = PVector(x, y)
        self.prev_positions = [self.pos.copy()]  # Store the previous position
        self.exploded = exploded
        self.lifespan = 255
        self.weight = 20
        self.hue = hue

        if not self.exploded:
            self.vel = PVector(3, -15)
        else:
            self.vel = self.random2D()
            self.vel.mult(random(2, 50))

        self.acc = PVector(0, 0)

    def apply_force(self, force):
        self.acc.add(force)

    def update(self):
        if self.exploded:
            self.vel.mult(0.96)
            self.lifespan -= 4
            
        time_scale = 0.4
        self.vel.add(PVector.mult(self.acc, time_scale))
        self.pos.add(PVector.mult(self.vel, time_scale))    
        #self.vel.add(self.acc)
        #self.pos.add(self.vel)
        self.acc.mult(0)
        self.weight  = self.weight * 0.998

    def done(self):
        return self.lifespan < 0

    def show(self):
        if not self.exploded:
            strokeWeight(self.weight)
            stroke(41,200,255)
            point(self.pos.x, self.pos.y)
        else:
            strokeWeight(2)  # adjust stroke weight to your needs
            stroke(41, 200, self.lifespan)
            
            # Draw lines between all subsequent pairs of previous positions
            for i in range(1, len(self.prev_positions)):
                line(self.prev_positions[i-1].x, self.prev_positions[i-1].y, 
                     self.prev_positions[i].x, self.prev_positions[i].y)
            
            # Add the current position to the list of previous positions
            self.prev_positions.append(self.pos.copy())
            
            # If there are more than 10 previous positions, remove the oldest one
            if len(self.prev_positions) > 2:
                self.prev_positions.pop(0)

    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))
