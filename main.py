import pygame
import constants as consts
import sys

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Galactic Defenders')

background_image = pygame.image.load("assets/Back_Image/Espace.jpg")


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.blit(background_image, (0, 0))

    pygame.display.update()

    clock.tick(60)
