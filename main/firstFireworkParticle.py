class FirstFireworkParticle:
    def __init__(self, x, y, hue, sat,b, exploded, explodedMultval):
        self.pos = PVector(x, y)
        self.prev_positions1 = [self.pos.copy()]
        self.prev_positions2 = [self.pos.copy()]
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
            self.weight  = self.weight * (0.93 if count % 2 == 0 else 1.072)
        
        time_scale = 0.2
        self.vel.add(PVector.mult(self.acc, time_scale))
        self.pos.add(PVector.mult(self.vel, time_scale))
        self.acc.mult(0)
        


    def done(self):
        return self.lifespan < 30

    def show(self):
        if not self.exploded:
            posLen = len(self.prev_positions1);
            for i in range(1, posLen):
                strokeWeight(self.weight * i / posLen) 
                stroke(0,0,255)
                point(self.prev_positions1[i-1].x, self.prev_positions1[i-1].y)

            strokeWeight(self.weight)
            stroke(self.hue - random(10), self.sat, 255)
            point(self.pos.x, self.pos.y)
            
        else:
            if(self.lifespan < 150):
                strokeWeight(2)
                for i in range(1, len(self.prev_positions2), 5):
                    stroke(self.hue+ random(-5, 5), 255, i *(self.lifespan * 0.05) + 30)
                    line(self.prev_positions2[i-5].x, self.prev_positions2[i-5].y, 
                        self.prev_positions2[i].x, self.prev_positions2[i].y)
            elif(self.lifespan < 170):
                strokeWeight(1)
                for i in range(10, len(self.prev_positions2), 2):
                    stroke(self.hue+ random(-5, 5), 255, i *(self.lifespan * 0.05) + 30)
                    line(self.prev_positions2[i-2].x, self.prev_positions2[i-2].y, 
                        self.prev_positions2[i].x, self.prev_positions2[i].y)
            elif(self.lifespan < 210):
                strokeWeight(1)
                for i in range(5, len(self.prev_positions2), 1):
                    stroke(self.hue+ random(-5, 5), 255, i *(self.lifespan * 0.05) + 30)
                    line(self.prev_positions2[i-1].x, self.prev_positions2[i-1].y, 
                         self.prev_positions2[i].x, self.prev_positions2[i].y)
            else:
                strokeWeight(1)
                for i in range(1, len(self.prev_positions2), 1):
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
            
            self.prev_positions2.append(self.pos.copy())
            
            if len(self.prev_positions2) > 20:
                self.prev_positions2.pop(0)
                
    def random2D(self):
        angle = random(TWO_PI)
        return PVector(cos(angle), sin(angle))
