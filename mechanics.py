import constants as consts


def shoot (player_x,player_y,player_angle):
    if player_angle == 90:
        #atirar para esquerda
        bullet_x = player_x + 2
        bullet_y = player_y
        bullet_dx = -consts.BULLET_SPEED

    if player_angle == 180:
        #atirar para baixo
        bullet_y = player_y + 2
        bullet_dy = consts.BULLET_SPEED
    if player_angle == -90:
        #atirar para direita
        bullet_x = player_x + 2
        bullet_dx = consts.BULLET_SPEED
    if player_angle == 0:
        #atirar para cima
        bullet_y = player_y -2
        bullet_dy = -consts.BULLET_SPEED



