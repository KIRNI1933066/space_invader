import pygame
import random as rd
import math

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('images/background.bmp')

# Title and icon of game window
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('images/battleship32.bmp')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('images/battleship64.bmp')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemy_img.append(pygame.image.load('images/ufo.bmp'))
    enemy_x.append(rd.randint(0, 736))
    enemy_y.append(rd.randint(50, 150))
    enemy_x_change.append(1)
    enemy_y_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bullet_img = pygame.image.load('images/bullet.bmp')
bullet_x = 0
bullet_y = 480
bullet_y_change = 5
bullet_state = "Ready"

# Score
score_value = 0
'''font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10'''

# Game over text
'''over_font = pygame.font.Font('freesansbold.ttf', 64)'''

'''def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (150, 0, 50))
    screen.blit(score, (x, y))'''


'''def game_over_text():
    over_text = font.render("GAME OVER", True, (150, 0, 50))
    screen.blit(over_text, (200, 250))'''


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27


# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((100, 100, 100))

    # Background image
    screen.blit(background, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_SPACE and bullet_state == "Ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    player_x = player_x if player_x >= 0 else 0
    player_x = player_x if player_x <= 736 else 736

    # Enemy movement
    for i in range(num_of_enemy):

        # Game over
        '''if enemy_y[i] > 440:
            for j in range(num_of_enemy):
                enemy_y[j] = 2000
            game_over_text()
            break'''

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 1
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.75
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "Ready"
            score_value += 1
            enemy_x[i] = rd.randint(0, 736)
            enemy_y[i] = rd.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "Fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y <= 0:
        bullet_state = "Ready"
        bullet_y = 480

    player(player_x, player_y)
    # show_score(text_x, text_y)
    pygame.display.update()
