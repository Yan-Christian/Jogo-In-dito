import pygame
import constants as consts
import sys
from button import Button
import mechanics as mec


#main menu screen

def get_font(size):
    return pygame.font.Font(consts.FONT, size)
def main_menu():
    pygame.display.set_caption("Main Menu")
    bg_music =pygame.mixer.Sound(consts.BG_MUSIC)
    button_sound = pygame.mixer.Sound(consts.BUTTON_SELECT)


    while True:
        bg_music.play()
        screen.blit(background_image,(0,0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text  = get_font(38).render(consts.TITLE, True, consts.WHITE)
        menu_rect = menu_text.get_rect(center = (consts.WINDOW_WIDTH//2,100))

        easy_button = Button(image = pygame.image.load(consts.RECT),pos=(consts.WINDOW_WIDTH//2,consts.WINDOW_HEIGHT//2),
                             text_input="EASY",font=get_font(25),base_color=consts.BASE_COLOR,hovering_color=consts.HOVERING_COLOR)
        medium_button = Button(image=pygame.image.load(consts.RECT),pos=(consts.WINDOW_WIDTH//2,consts.WINDOW_HEIGHT//2 + 100),
                               text_input="MEDIUM",font=get_font(25),base_color = consts.BASE_COLOR,hovering_color=consts.HOVERING_COLOR)
        hard_button = Button(image=pygame.image.load(consts.RECT),pos=(consts.WINDOW_WIDTH//2,consts.WINDOW_HEIGHT//2+200),
                             text_input="HARD",font =get_font(25),base_color=consts.BASE_COLOR,hovering_color=consts.HOVERING_COLOR)

        screen.blit(menu_text,menu_rect)

        for button in [easy_button,medium_button,hard_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.check_for_input(menu_mouse_pos):
                    bg_music.stop()
                    button_sound.play()
                    return 'easy'
                if medium_button.check_for_input(menu_mouse_pos):
                    bg_music.stop()
                    button_sound.play()
                    return 'medium'
                if hard_button.check_for_input(menu_mouse_pos):
                    bg_music.stop()
                    button_sound.play()
                    return 'hard'

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


        pygame.display.update()
pygame.init()
pygame.mixer.init()

# screen setup
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Galactic Defenders')

# background
background_image = pygame.image.load("assets/Back_Image/Espace.jpg")

# player setup
player_original = pygame.image.load("assets/Player_1/Player 1.png")
player_width, player_height = 50, 50
player_original = pygame.transform.scale(player_original, (player_width, player_height))
player_x = (consts.WINDOW_WIDTH - player_width) // 2
player_y = consts.WINDOW_HEIGHT - player_height
player_speed = 5
player_angle = 0

# bullet setup
bullet_speed = 7
bullet = None
bullets_left = 4
max_bullets = 4
cooldown_time = 2
reloading = False
reload_start_time = 0
bullet_direction = consts.BulletDirection.UP

# load sound effect for shooting and reloading
shoot_sound = pygame.mixer.Sound("assets/Sound game/Disparo.mp3")
reload_sound = pygame.mixer.Sound("assets/Sound game/Recarregamento.mp3")

difficulty = main_menu()
# game loop


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key inputs
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

    # Escape key to quit the game
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Space key to shoot a bullet, only if not in reload mode and bullets available
    if key[pygame.K_SPACE] and bullet is None and bullets_left > 0 and not reloading:
        shoot_sound.play()
        bullets_left -= 1

        if player_angle == 0:
            bullet = [player_x + player_width // 2, player_y]
            bullet_direction = consts.BulletDirection.UP
        if player_angle == 90:
            bullet = [player_x, player_y + player_height // 2]
            bullet_direction = consts.BulletDirection.LEFT
        if player_angle == 180:
            bullet = [player_x + player_width // 2, player_y]
            bullet_direction = consts.BulletDirection.DOWN
        if player_angle == -90:
            bullet = [player_x, player_y + player_height // 2]
            bullet_direction = consts.BulletDirection.RIGHT

        # inicia a recarga
        if bullets_left == 0:
            reloading = True
            reload_start_time = pygame.time.get_ticks()
            reload_sound.play()

    # Se estiver recarregando, verifica o tempo de recarga
    if reloading:
        current_time = pygame.time.get_ticks()
        if current_time - reload_start_time >= cooldown_time * 1000:
            bullets_left = max_bullets
            reloading = False

    if bullet:
        match bullet_direction:
            case consts.BulletDirection.UP:
                bullet[1] -= bullet_speed
                if bullet[1] <= 0:
                    bullet = None
            case consts.BulletDirection.DOWN:
                bullet[1] += bullet_speed
                if bullet[1] >= consts.WINDOW_HEIGHT:
                    bullet = None
            case consts.BulletDirection.LEFT:
                bullet[0] -= bullet_speed
                if bullet[0] <= 0:
                    bullet = None
            case consts.BulletDirection.RIGHT:
                bullet[0] += bullet_speed
                if bullet[0] >= consts.WINDOW_WIDTH:
                    bullet = None

    # Rotaciona a nave
    player_rotated = pygame.transform.rotate(player_original, player_angle)

    screen.blit(background_image, (0, 0))  # Fundo
    screen.blit(player_rotated, (player_x, player_y))  # Nave

    if bullet:
        pygame.draw.circle(screen, consts.BULLET_COLOR, (bullet[0], bullet[1]), consts.BULLET_RADIUS)

    # Mostra a quantidade de balas
    font = pygame.font.SysFont(None, 36)
    ammo_text = font.render(f'Balas: {bullets_left}', True, (255, 255, 255))
    screen.blit(ammo_text, (10, 10))

    if reloading:
        reload_text = font.render('Recarregando...', True, (255, 0, 0))
        screen.blit(reload_text, (10, 50))

    pygame.display.update()
    clock.tick(60)
