import pygame
import random
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.jumping = False
        self.falling = False
        self.score = 0

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocity = 3

enemy =Enemy(350,400)
enemy2 =Enemy(950,420)
player = Player(50,450)

# Functions 

def draw():
    screen.fill("orange")
    pygame.draw.rect(screen,"blue",(player.x,player.y,50,50))    
    pygame.draw.rect(screen,"red",(enemy.x,enemy.y,50,100))
    pygame.draw.rect(screen,"white",(0,500,800,20))
    pygame.draw.rect(screen,"red",(enemy2.x,enemy2.y,50,80))
    pygame.display.flip()

def enemyMovement():
    enemy.x -= enemy.velocity
    enemy2.x -= enemy.velocity

    if enemy.x < -115:
        enemy.x = random.randint(250,300) * enemy.velocity
        enemy.velocity += 1
        player.score +=1
    if enemy2.x < -115:
        enemy2.x = random.randint(100,300) * enemy.velocity

def controlPlayer():
    if player.jumping:
        if player.y< 300:
            player.y -= 4.9
        else:
            player.y-=8.1
    if player.y < 280:
        player.jumping = False
        player.falling = True

    if player.y < 450 :
        player.y += 4
    else:
        player.falling=False

def collision():
    pass
    if player.y + 50 >= enemy.y :
       # print("true")
        if abs((enemy.x + 25) - (player.x + 25) ) < 50 :
            #print("inner collision")
            print("your score is: ",player.score)
            quit()
        else:
            pass
            #print("inner false") 
    else:      
        pass     
        #print("false")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.falling == False:
                    player.jumping = True
                

    enemyMovement()
    controlPlayer()
    collision()
    draw()

    clock.tick(60)