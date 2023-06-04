class FirstFireworkParticle:
    def __init__(self, x, y, hue, sat,b, exploded, explodedMultval):
        self.pos = PVector(x, y)
        self.prev_positions1 = [self.pos.copy()]  # Store the previous position
        self.prev_positions2 = [self.pos.copy()]  # Store the previous position
        self.exploded = exploded
        self.explodedMultval = explodedMultval
        self.lifespan = 255
        self.weight = 20
        self.hue = hue
        self.sat = sat
        self.b = b


        if not self.exploded:
            self.vel = PVector(3, -15)
        else:
            self.vel = self.random2D()
            self.vel.mult(random(0, explodedMultval))

        self.acc = PVector(0, 0)

    def apply_force(self, force):
        self.acc.add(force)

    def update(self, count):
        if self.exploded:
            self.vel.mult(0.999)
            self.lifespan -= 4
        else :
            self.pos.x = self.pos.x + random(-1, 1)
            self.prev_positions1.append(self.pos.copy())
        
        time_scale = 0.2
        self.vel.add(PVector.mult(self.acc, time_scale))
        self.pos.add(PVector.mult(self.vel, time_scale))
        #self.vel.add(self.acc)
        #self.pos.add(self.vel)
        self.acc.mult(0)
        self.weight  = self.weight * (0.93 if count % 2 == 0 else 1.072)


    def done(self):
        return self.lifespan < 30

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
            #stroke(self.hue, 0, random(10,150))
            #ellipse(self.pos.x, self.pos.y, 10, 50)
            stroke(self.hue - random(10), self.sat, 255)
            point(self.pos.x, self.pos.y)
            
        else:
              # adjust stroke weight to your needs
        
            #stroke(0,0,255)
            posLen = len(self.prev_positions1);
            strokeWeight(5)
            stroke(32.5, 255, 255)
            point(self.prev_positions1[posLen-1].x, self.prev_positions1[posLen-1].y)
            strokeWeight(4)
            stroke(42.5, 255, 255)
            point(self.prev_positions1[posLen-1].x, self.prev_positions1[posLen-1].y)
            
            if(self.lifespan < 150):
                strokeWeight(2)
            else:
                strokeWeight(1)
            
            # Draw lines between all subsequent pairs of previous positions
            for i in range(1, len(self.prev_positions2)):
                stroke(self.hue+ random(-5, 5), 255, i *(self.lifespan * 0.05) + 30)
                line(self.prev_positions2[i-1].x, self.prev_positions2[i-1].y, 
                     self.prev_positions2[i].x, self.prev_positions2[i].y)
            
            if self.sat == 0:
                self.hue2 = 170+ random(-5, 5)
                self.sat2 = 170/3 - self.lifespan/3
                stroke(self.hue2, self.sat2, self.b * (self.lifespan * 0.05)+ 30)
                if(self.lifespan < 140):
                    strokeWeight(random(3,4))
                    line(self.pos.x, self.pos.y, self.pos.x+(random(-2,2)), self.pos.y+(random(-2,2)))
            else:
                stroke(self.hue+ random(-5, 5), self.sat, self.b * (self.lifespan * 0.05)+ 30)
                if(self.lifespan < 170):
                    strokeWeight(random(3,4))
                    line(self.pos.x, self.pos.y, self.pos.x+(random(-2,2)), self.pos.y+(random(-2,2)))
            
                # Add the current position to the list of previous positions
            self.prev_positions2.append(self.pos.copy())
            
            # If there are more than 10 previous positions, remove the oldest one
            if len(self.prev_positions2) > 20:
                self.prev_positions2.pop(0)

    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))
