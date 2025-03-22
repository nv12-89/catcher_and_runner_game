import pgzrun
from random import randint
import time
WIDTH=800
HEIGHT=600
TITLE="Catching Game"

catcher=Actor("positive_alien")
runner=Actor("negative_alien")

catcher.pos=WIDTH/2,HEIGHT/2
runner.pos=50,100

message="Catch the runner!"
health=0
game_state='start'

def draw():
    screen.blit("background",(-50,-5))
    if game_state=='start':
        screen.draw.text("Catch the runner",(WIDTH // 3, HEIGHT // 2),fontsize=50,color="white")
        

    elif game_state=='play':
        catcher.draw()
        runner.draw()
        screen.draw.text(f"Health: {health}",(10,10),fontsize=30,color="white")
    
    elif game_state=='over':
        screen.draw.text("Game Over",(10,10),fontsize=30,color="white")
        screen.draw.text(f"Final Score: {health}",(10,50),fontsize=30,color="white")

def update():
    global health,game_state
    if game_state=='start' and keyboard.space:
        game_state='play'
        health=0

    if game_state=='play':
        if keyboard.left:
            catcher.x-=2
        elif keyboard.right:
            catcher.x+=2
        elif keyboard.up:
            catcher.y-=2
        elif keyboard.down:
            catcher.y+=2
        if catcher.colliderect(runner):
            runner.x=randint(50,WIDTH-50)
            runner.y=randint(50,HEIGHT-50)
            health+=1
        
pgzrun.go()