import pygame
import sys
import random
pygame.init()

#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
black = [0, 0, 0]
white = [255, 255, 255]
grey = [175, 175, 175]

#ekraani seaded
pind = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Majake")
pind.fill(lGreen)

#funktsioonid
def drawHouse(x, y, width, height, screen, color):
   points = [(x,y- ((3/4.0) * height)), (x,y), (x+width,y), (x+width,y-(3/4.0) * height),
        (x,y- ((3/4.0) * height)), (x + width/2.0,y-height), (x+width,y-(3/4.0)*height)]
   lineThickness = 3
   pygame.draw.lines(screen, color, False, points, lineThickness)

#kutsun funktsiooni välja
drawHouse(100, 400, 300, 400, pind, grey)

#ДВЕРЬ
door_width = 80
door_height = 120
door_x = 100 + (300 // 2) - (door_width // 2)  
door_y = 400 - door_height
pygame.draw.rect(pind, black, [door_x, door_y, door_width, door_height])

#ОКНО
window_width = 50
window_height = 50
window_x = door_x + door_width + 10  
window_y = door_y + (door_height // 4)  
pygame.draw.rect(pind, grey, [window_x, window_y, window_width, window_height])

window_width = 10
window_height = 5
window_x = door_x + door_width + -20 
window_y = door_y + (door_height // 2)  
pygame.draw.rect(pind, grey, [window_x, window_y, window_width, window_height])

#ДЫМОХОД
chimney_width = 40
chimney_height = 80
chimney_x = 210 + (300 // 2) - (chimney_width // 2)  
chimney_y = 390 - (3 / 4.0) * 400 - chimney_height 
pygame.draw.rect(pind, grey, [chimney_x, chimney_y, chimney_width, chimney_height])

pygame.display.flip()

#main loop
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()