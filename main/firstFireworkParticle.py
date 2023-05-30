class FirstFireworkParticle:
    def __init__(self, x, y, hue, sat, exploded, explodedMultval):
        self.pos = PVector(x, y)
        self.prev_positions1 = [self.pos.copy()]  # Store the previous position
        self.prev_positions2 = [self.pos.copy()]  # Store the previous position
        self.exploded = exploded
        self.explodedMultval = explodedMultval
        self.lifespan = 255
        self.weight = 20
        self.hue = hue
        self.sat = sat

        if not self.exploded:
            self.vel = PVector(3, -15)
        else:
            self.vel = self.random2D()
            self.vel.mult(random(2, explodedMultval))

        self.acc = PVector(0, 0)

    def apply_force(self, force):
        self.acc.add(force)

    def update(self):
        if self.exploded:
            self.vel.mult(0.98)
            self.lifespan -= 4
        
        self.pos.x = self.pos.x + random(-1, 1)
        self.prev_positions1.append(self.pos.copy())
        
        time_scale = 0.3
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
            posLen = len(self.prev_positions1);
            for i in range(1, posLen):
                strokeWeight(self.weight * i / posLen)  # Increase stroke weight to make older positions more prominent
                stroke(0,0,255)
                point(self.prev_positions1[i-1].x, self.prev_positions1[i-1].y)

            # Add the current position to the list of previous positions
            
            # If there are more than 10 previous positions, remove the oldest one
            #if len(self.prev_positions1) > 500:
                #self.prev_positions1.pop(0)
    
            strokeWeight(self.weight)
            stroke(self.hue, self.sat, 255)
            point(self.pos.x, self.pos.y)
        else:
            strokeWeight(1)  # adjust stroke weight to your needs
            
            # Draw lines between all subsequent pairs of previous positions
            for i in range(1, len(self.prev_positions2)):
                stroke(self.hue, self.sat, (30-i)*(self.lifespan*0.001))
                line(self.prev_positions2[i-1].x, self.prev_positions2[i-1].y, 
                     self.prev_positions2[i].x, self.prev_positions2[i].y)
                
            strokeWeight(random(3,5))
            stroke(self.hue, self.sat, self.lifespan)
            point(self.pos.x, self.pos.y)
            # Add the current position to the list of previous positions
            self.prev_positions2.append(self.pos.copy())
            
            # If there are more than 10 previous positions, remove the oldest one
            if len(self.prev_positions2) > 15:
                self.prev_positions2.pop(0)

    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))
