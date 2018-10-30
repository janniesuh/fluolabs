score = 0
time = 60
gameOver = False
x=0
y=0

def setup():
    size(480, 360)
    
def draw():
    global time, x, y
    background(0)
    textSize(20)
    text("score: " + str(score), 0, 30)
    text("time: " + str(time), 0, 50)
    if (frameCount % 120 == 0):
        time = time - 2
        x = random(width)
        y = random(height)
        
        
    # check end of game
    if (time == 0):
        text("Game Over!" , width/2 - 50, height/2)
        gameOver = True
        noLoop()
        
        
    # draaw dinosaur
    ellipse(x, y, 30, 30)
    
def mouseClicked():
    global score
    d = dist(x, y, mouseX, mouseY)
    if (d < 15):
        score += 10
    else: 
        score -= 20
    
