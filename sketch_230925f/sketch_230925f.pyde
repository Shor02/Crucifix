def setup():
 global x
 global y 
 background(0)

 y = height / 2
 x = width / 2
 size(500,500)
 
 x = 0

def draw():

    r = random(255)
    g = random(255)
    b = random(255)
    noStroke()
    fill(255, 255, 0)
    circle(250, 250, 50)
    fill(128, 5, 128)
    circle(250, 250, 50)
    fill(231, 8, 74)
    circle(250, 250, 50)
    fill(99, 33, 222)
    circle(250, 250, 50)
    
    if mousePressed:
        global x
        global y
        fill(r, g, b)
        circle (y, x, 20)
        x = x + 1
        y = y - 1
        fill(r, g, b)
        circle (x, y, 20)
        x = x + 1
        y = y + 1






    
