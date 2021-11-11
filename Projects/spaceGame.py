import pygame
import random 
import math

# initialize pygame

pygame.init()


# create the screen

screen = pygame.display.set_mode((800, 600))


# Background

background = pygame.image.load('planetBackground.png')


# Title and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-galaxy.png')
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('001-spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('004-alien.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(15)

# Bullet

# Ready- You can't see the bullet
# Fire- The bullet is moving

bulletImg = pygame.image.load('005-bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

score = 0

# Player and Enemy func

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY)-> Union[int,list]:
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2))) 

    if distance < 27:
        return True
    else:
        return False
    

# Game Loop

running = True

while running:
    # RGB- RED, GREEN, BLUE
    screen.fill((30,12,155))
    # background Img
    screen.blit(background, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = - 2

            if event.key == pygame.K_RIGHT:
                playerX_change = 2

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current X of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundrings of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736
    
    # Enemy movement

    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
            
        elif enemyX[i] >= 736:
            enemyX_change[i]= - 1
            enemyY[i] += enemyY_change[i]
            
        # Collision
        col = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if col:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score) 
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

 # Collision
    col = iscollision(enemyX, enemyY, bulletX, bulletY)
    if col:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score) 
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    pygame.display.update()

