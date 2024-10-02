import pygame
import constants as consts
import sys

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Galactic Defenders')

background_image = pygame.image.load("assets/Back_Image/Espace.jpg")

player = pygame.image.load("assets/Player_1/Player 1.png")
player_width, player_height = 50, 50
player = pygame.transform.scale(player, (player_width, player_height))

player_x = (consts.WINDOW_WIDTH - player_width) // 2
player_y = consts.WINDOW_HEIGHT - player_height

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(background_image, (0, 0))
    screen.blit(player, (player_x, player_y))

    pygame.display.update()


    clock.tick(60)
