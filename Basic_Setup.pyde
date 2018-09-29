def setup():
    global x, y, diameter
    size(800, 300)
    
    diameter = 30
    x = 50
    y = (200-(diameter/2))
    
def draw():
    background(255)
    
    fill(50)
    rect(0, 200, 800, 300)
    fill(255)
    ellipse(x, y, diameter, diameter)
    
    
    
    
