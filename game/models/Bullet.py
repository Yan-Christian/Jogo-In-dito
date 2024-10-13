# Classe para o projétil
import this

import pygame
import sys
from game.constants import BulletDirection
import game.constants as consts


class Bullet:
    def __init__(self, x, y, width, height, speed, bullet_direction: BulletDirection):
        self.image = pygame.image.load('assets/Bullet/bala.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        match bullet_direction.value:
            case BulletDirection.UP.value:
                self.image = pygame.transform.rotate(self.image, 90)
            case BulletDirection.DOWN.value:
                self.image = pygame.transform.rotate(self.image, -90)
            case BulletDirection.LEFT.value:
                self.image = pygame.transform.rotate(self.image, 180)
            case BulletDirection.RIGHT.value:
                self.image = pygame.transform.rotate(self.image, 0)
            case _:
                print("ERROR")
        self.rect = self.image.get_rect().copy()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.active = True

    def move(self, bullet_direction: BulletDirection):
        match bullet_direction.value:
            case BulletDirection.UP.value:
                self.rect.y -= self.speed
                if self.rect.y - self.rect.height <= 0:
                    self.active = False
            case BulletDirection.DOWN.value:
                self.rect.y += self.speed
                if self.rect.y >= consts.WINDOW_HEIGHT:
                    self.active = False
            case BulletDirection.LEFT.value:
                self.rect.x -= self.speed
                if self.rect.x - self.rect.width <= 0:
                    self.active = False
            case BulletDirection.RIGHT.value:
                self.rect.x += self.speed
                if self.rect.x >= consts.WINDOW_WIDTH:
                    self.active = False
            case _:
                print("ERROR")

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect.center)
            return self
        else:
            return None
