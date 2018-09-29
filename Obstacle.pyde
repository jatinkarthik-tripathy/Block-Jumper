import random

class obstacle:
    def __init__(self, x,y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw_ob(self):
        fill(60)
        rect(self.x, self.y, self.w, self.h)
    
    def move(self):
        global speed
        self.x -= speed
        if self.x <= 0 :
            self.x=780
            self.h = random.randrange(20, 50)
            self.y = 200 - self.h
        

def setup():
    global x, y, diameter, obs, speed
    size(800, 300)
    
    diameter = 30
    x = 50
    y = (200-(diameter/2))
    speed = 1.5
    
    obs = []
    x_val = 780
    y_val = 180
    ht = 20
    wdt = 20
    for i in range(4):
        ob = obstacle(x_val, y_val, wdt, ht)
        x_val += 200
        ht = random.randrange(20, 50)
        y_val = 200 - ht
        obs.append(ob)
    
    
def draw():
    background(255)
    
    fill(50)
    rect(0, 200, 800, 300)
    fill(255)
    ellipse(x, y, diameter, diameter)
    
    for ob in obs:
        ob.draw_ob()
        ob.move()
    
    
