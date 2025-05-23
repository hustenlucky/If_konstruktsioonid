import pygame
import sys
pygame.init() # Pygame'i tööle rakendamiseks

# Värvid
Green = [153, 255, 153]
Blue = [153, 204, 255]

ekraanipind = pygame.display.set_mode((700, 450))
ekraanipind.fill(Green)
pygame.display.set_caption("Esimene mäng")

gameover = False

while not gameover:
    # Lisame pildi
    youwin = pygame.image.load("YOU.WIN.png")
    youwin = pygame.transform.scale(youwin, [500, 300])
    ekraanipind.blit(youwin, [100, 120])
     
    pygame.display.flip()
    
    # Mängu sulgemise nupust
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
pygame.quit() # Pygame välja lülitamine