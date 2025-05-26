# import pygame
# import sys
# import random
# pygame.init()

# värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# black = [0, 0, 0]
# white = [255, 255, 255]
# grey = [175, 175, 175]

# ekraani seaded
# pind = pygame.display.set_mode([640, 480])
# pygame.display.set_caption("Majake")
# pind.fill(lGreen)

# Funktsioonid ühe rea jaoks
# def drawHouse(x, y, width, height, screen, color): pygame.draw.lines(screen, color, False, [(x, y - ((3/4.0) * height)), (x, y), (x + width, y), (x + width, y - (3/4.0) * height), (x, y - ((3/4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3/4.0) * height)], 3)
# def drawDoor(x, y, width, height, screen, color): pygame.draw.rect(screen, color, [x, y, width, height])
# def drawWindow(x, y, width, height, screen, color): pygame.draw.rect(screen, color, [x, y, width, height])
# def drawChimney(x, y, width, height, screen, color): pygame.draw.rect(screen, color, [x, y, width, height])

# Kutsun funktsioone välja
# drawHouse(100, 400, 300, 400, pind, grey); drawDoor(100 + (300 // 2) - (80 // 2), 400 - 120, 80, 120, pind, black);
# drawWindow(100 + (300 // 2) - (80 // 2) + 90, 400 - 120 + (120 // 4), 50, 50, pind, grey);
# drawWindow(100 + (300 // 2) - (80 // 2) - 30, 400 - 120 + (120 // 2), 10, 5, pind, grey);
# drawChimney(210 + (300 // 2) - (40 // 2), 390 - (3 / 4.0) * 400 - 80, 40, 80, pind, grey)

# Joonistame kogu stseeni
# drawScene()

# pygame.display.flip()

# main loop
# while True:
#     event = pygame.event.poll()
#     if event.type == pygame.QUIT:
#         break

# pygame.quit()
 

