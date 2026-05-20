import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.jpg")

pygame.display.set_caption("Space Riders")

icon = pygame.image.load("ufo.png")
playerImg = pygame.image.load("player.png")


bulletImg = pygame.image.load("bullet.png")

new_score = 0    

powerImg = pygame.image.load("power.png")
powerupX = random.randint(0, 767)
powerupY = -10000
powerupY_change = 0.02

playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 10

for i in range(num_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 767))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.6)
    enemyY_change.append(40)


bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x,y):
    score = font.render("Score :" + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (290, 300))

def player(x,y):
    screen.blit(playerImg, (x, y))

def powerup(x,y):
    screen.blit(powerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x , y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    
def powerCollision(playerX, playerY, powerupX, powerupY):
    distance = math.sqrt((math.pow(playerX-powerupX,2)) + (math.pow(playerY-powerupY,2)))
    if distance < 27:
        return True
    else:
        return False

pygame.display.set_icon(icon)

running = True
while running:

    screen.fill((0, 0, 0))
    
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                 playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change    

    if playerX <=0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768   

    enemyX += enemyX_change    

    for i  in range(num_enemies):

        if enemyY[i] > 425:
            for j  in range(num_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 0.6
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 768:
            enemyX_change[i] = -0.6
            enemyY[i] += enemyY_change[i]


        powerupY += powerupY_change
        
            

        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 767)
            enemyY[i] = random.randint(50, 150)

        power_collision = powerCollision(playerX,playerY,powerupX,powerupY)
        if power_collision:
            powerupY = -10000
            powerupX = random.randint(0, 767)
            bulletX = playerX 
            

            

       
        score = score_value // 10
        if score != new_score:
            new_score = score
            powerupY = -50
            powerupY += powerupY_change
            

        enemy(enemyX[i], enemyY[i], i)


    if bulletY <=0:
        bulletY =480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    powerup(powerupX, powerupY)
    show_score(textX, textY)

    pygame.display.update()