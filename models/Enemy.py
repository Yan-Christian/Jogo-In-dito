# Classe para os inimigos
import random

import pygame

import constants


class Enemy:
    def __init__(self, x, y, width, height, speed, difficulty):
        # Definindo a imagem do inimigo conforme a dificuldade
        if difficulty == 'easy':
            self.image = pygame.image.load('assets/Enemies/Level_1.png')
        elif difficulty == 'medium':
            self.image = pygame.image.load('assets/Enemies/Level_2.png')
        else:
            self.image = pygame.image.load('assets/Enemies/Level_3.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect().copy()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def move(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y

        # Inverter direção ao atingir bordas da tela
        if self.rect.left <= 0 or self.rect.right >= constants.WINDOW_WIDTH:
            self.direction_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= constants.WINDOW_HEIGHT:
            self.direction_y *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)