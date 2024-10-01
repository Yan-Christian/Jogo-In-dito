import pygame
import constants as consts

pygame.init()

#sound effects initiation
pygame.mixer.init()


#screen
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()

#game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    #controls
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()

