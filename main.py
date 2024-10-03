import pygame
import constants as consts
import sys
import random
from button import Button
import mechanics as mec


# Classe para os inimigos
class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.image = pygame.image.load("assets/Enemies/Level_1.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def move(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        # Inverter direção ao atingir bordas da tela
        if self.rect.left <= 0 or self.rect.right >= consts.WINDOW_WIDTH:
            self.direction_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= consts.WINDOW_HEIGHT:
            self.direction_y *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def get_font(size):
    return pygame.font.Font(consts.FONT, size)


def main_menu():
    pygame.display.set_caption("Main Menu")
    bg_music = pygame.mixer.Sound(consts.BG_MUSIC)
    button_sound = pygame.mixer.Sound(consts.BUTTON_SELECT)

    while True:
        bg_music.play()
        screen.blit(background_image, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(38).render(consts.TITLE, True, consts.WHITE)
        menu_rect = menu_text.get_rect(center=(consts.WINDOW_WIDTH // 2, 100))

        easy_button = Button(image=pygame.image.load(consts.RECT), pos=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2),
                             text_input="EASY", font=get_font(25), base_color=consts.BASE_COLOR, hovering_color=consts.HOVERING_COLOR)
        medium_button = Button(image=pygame.image.load(consts.RECT), pos=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2 + 100),
                               text_input="MEDIUM", font=get_font(25), base_color=consts.BASE_COLOR, hovering_color=consts.HOVERING_COLOR)
        hard_button = Button(image=pygame.image.load(consts.RECT), pos=(consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2 + 200),
                             text_input="HARD", font=get_font(25), base_color=consts.BASE_COLOR, hovering_color=consts.HOVERING_COLOR)

        screen.blit(menu_text, menu_rect)

        for button in [easy_button, medium_button, hard_button]:
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

# Configuração dos inimigos
enemy_list = []
enemy_spawn_time = 2000  # Tempo para criação de novos inimigos (em milissegundos)
last_enemy_spawn = pygame.time.get_ticks()

def create_enemy():
    """Função para criar um inimigo em uma posição aleatória."""
    x = random.randint(0, consts.WINDOW_WIDTH - 50)
    y = random.randint(0, consts.WINDOW_HEIGHT // 2)  # Inimigos começam na metade superior da tela
    speed = random.randint(1, 3)
    enemy = Enemy(x, y, 50, 50, speed)
    enemy_list.append(enemy)


difficulty = main_menu()

# Loop principal do jogo
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
        elif player_angle == 90:
            bullet = [player_x, player_y + player_height // 2]
            bullet_direction = consts.BulletDirection.LEFT
        elif player_angle == 180:
            bullet = [player_x + player_width // 2, player_y]
            bullet_direction = consts.BulletDirection.DOWN
        elif player_angle == -90:
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

    # Atualizar a bala
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

    # Criar novos inimigos de acordo com o tempo
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn > enemy_spawn_time:
        create_enemy()
        last_enemy_spawn = current_time

    # Atualizar movimento dos inimigos e verificar colisões
    for enemy in enemy_list:
        enemy.move()
        if bullet and enemy.rect.collidepoint(bullet[0], bullet[1]):
            bullet = None  # Remove a bala
            enemy_list.remove(enemy)  # Remove o inimigo atingido

    # Desenhar na tela
    screen.blit(background_image, (0, 0))  # Fundo
    player_rotated = pygame.transform.rotate(player_original, player_angle)
    screen.blit(player_rotated, (player_x, player_y))  # Nave

    # Desenhar inimigos
    for enemy in enemy_list:
        enemy.draw(screen)

    # Desenhar a bala
    if bullet:
        pygame.draw.circle(screen, consts.BULLET_COLOR, (bullet[0], bullet[1]), consts.BULLET_RADIUS)

    # Exibir balas restantes
    font = pygame.font.SysFont(None, 36)
    ammo_text = font.render(f'Balas: {bullets_left}', True, (255, 255, 255))
    screen.blit(ammo_text, (10, 10))

    # Exibir mensagem de recarregamento, se aplicável
    if reloading:
        reload_text = font.render('Recarregando...', True, (255, 0, 0))
        screen.blit(reload_text, (10, 50))

    # Atualizar a tela
    pygame.display.update()
    clock.tick(60)
