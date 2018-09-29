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
    def collision(self, x, y):
        global diameter
        if( self.y < (y+(diameter/2)) ) and ( self.x < ( x+(diameter/2)) and (x-(diameter/2)) < (self.x+self.w)):
            return True
        else:
            return False
        

def setup():
    global x, y, diameter, obs, speed, game_over
    size(800, 300)
    
    diameter = 30
    x = 50
    y = (200-(diameter/2))
    speed = 1.5
    game_over = False
    
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
    global x, y, game_over, lim
    background(255)
    
    fill(50)
    rect(0, 200, 800, 300)
    fill(255)
    ellipse(x, y, diameter, diameter)
    
    if(y<185):
            y += speed + 0.5
    if(y>=185):
        lim = 0
    
    if game_over == False:
        for ob in obs:
            ob.draw_ob()
            ob.move()
            game_over = ob.collision(x, y)
            if game_over == True:
                break
    else:
        background(0)
        textSize(32);
        textAlign(CENTER)
        fill(200);
        text("GAME OVER", 402, 152, -30)
        fill(255) 
        text("GAME OVER", 400, 150)
        
        
def keyPressed():
    global lim, y
    if key == CODED:
        if keyCode == UP and lim < 1:
            y -= 180
            lim += 1
        
    if y<=15:
        y=15
