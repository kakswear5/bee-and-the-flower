import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
TITLE = "the bee & the flower"

score = 0
game_over = False

bee = Actor("bee")
bee.pos = (100,100)

flower = Actor("flower")
flower.pos= (200,200)

def draw():
    screen.blit("bg",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("score: " + str (score),
                     midtop=(WIDTH/2,10),
                     fontsize=45,
                     color="blue")
    if game_over:
        screen.fill("purple")

        screen.draw.text("TIME'S UP YOUR FINAL SCORE IS  " + str(score),
                         midtop=(WIDTH/2,10),
                     fontsize=45,
                     color="blue")

def  place_flower():
    flower.x = randint(65,(WIDTH-70))
    flower.y = randint(65,(HEIGHT-70))

def timer():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.a:
        bee.x = bee.x - 2
    if keyboard.d:
        bee.x = bee.x + 2
    if keyboard.w:
        bee.y = bee.y - 2
    if keyboard.s:
        bee.y = bee.y + 2

    flower_collected= bee.colliderect(flower)

    if flower_collected:
        score = score +10
        place_flower()

clock.schedule(timer,15.0)





pgzrun.go()    


