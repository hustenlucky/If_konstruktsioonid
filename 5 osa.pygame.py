import pygame, random
pygame.init()

# Цвета
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
lilla = [153, 255, 255]
pink = [255, 153, 255]
white = [255, 255, 255]
# Размеры экрана
screenX = 680
screenY = 520
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Surface")
clock = pygame.time.Clock()
posX, posY = 100, 100
speedX = 3
speedY = 3.4
player = pygame.Rect(posX, posY, 120, 120)
playerImage = pygame.image.load("drakon.png")
playerImage = pygame.transform.scale(playerImage, [player.width, player.height])
# Враги
enemies = []
enemyImage = pygame.image.load("yasherka.png")
enemyImage = pygame.transform.scale(enemyImage, [60, 73])
enemyCounter = 0
totalEnemies = 20
score = 0
gameOver = False
while not gameOver:
    clock.tick(60)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    # позиции игрока
    posX += speedX
    posY += speedY
    # Отскок 
    if posX + player.width >= screenX or posX <= 0:
        speedX = -speedX
    if posY + player.height >= screenY or posY <= 0:
        speedY = -speedY
    player = pygame.Rect(posX, posY, 120, 120)
    # Создание врагов
    if enemyCounter < totalEnemies:
        enemy = pygame.Rect(random.randint(0, screenX - 60), random.randint(0, screenY - 73), 60, 73)
        enemies.append(enemy)
        enemyCounter += 1
    # Проверка столкновений
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, screenX - enemy.width)
            enemy.y = random.randint(0, screenY - enemy.height)

    screen.fill(blue)
    screen.blit(playerImage, player)

    for enemy in enemies:
        screen.blit(enemyImage, enemy) 

    pygame.display.flip()

    # Победа
    if score >= 100:
        gameOver = True

pygame.quit()
