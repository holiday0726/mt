class Star:
    def __init__(self, w, h):
        self.stars = []
        for i in range(30):  # adjust amount of stars here
            self.stars.append(PVector(random(w), random(h)))
    
    def render(self):
        stroke(255)
        strokeWeight(random(2,3))
        for s in self.stars:
            point(s.x, s.y)
