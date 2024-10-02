from enum import Enum

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 650

BULLET_RADIUS = 2
BULLET_SPEED = 10
BULLET_DX = 0
BULLET_DY = 0
BULLET_COLOR = (255, 255, 255)


class BulletDirection(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
