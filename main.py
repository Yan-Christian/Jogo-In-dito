import pygame
import constants as consts
import sys

pygame.init()

pygame.mixer.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Galactic Defenders')

background_image = pygame.image.load("assets/Back_Image/Espace.jpg")

player_original = pygame.image.load("assets/Player_1/Player 1.png")
player_width, player_height = 50, 50
player_original = pygame.transform.scale(player_original, (player_width, player_height))

player_x = (consts.WINDOW_WIDTH - player_width) // 2
player_y = consts.WINDOW_HEIGHT - player_height

player_speed = 5

player = player_original
player_angle = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        player_angle = 90

    if key[pygame.K_RIGHT] and player_x < consts.WINDOW_WIDTH - player_width:
        player_x += player_speed
        player_angle = -90

    if key[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
        player_angle = 0

    if key[pygame.K_DOWN] and player_y < consts.WINDOW_HEIGHT - player_height:
        player_y += player_speed
        player_angle = 180

    player_rotated = pygame.transform.rotate(player_original, player_angle)

    screen.blit(background_image, (0, 0))
    screen.blit(player_rotated, (player_x, player_y))

    pygame.display.update()

    clock.tick(60)
