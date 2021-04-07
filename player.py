import pygame
from pygame.locals import *
from pygame.math import Vector2
import sprite

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

FAST = 5
SLOW = 2.5

vec = pygame.math.Vector2


class Player(sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/player_c.png", spawn_x, spawn_y)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/player1_collide.png"))
        self.pos = vec(self.rect.center)
        self.acc = vec(0, 0)
        self.speed = FAST
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.image = pygame.image.load("res/img/player_l.png")
        elif self.right:
            self.image = pygame.image.load("res/img/player_r.png")
        else:
            self.image = pygame.image.load("res/img/player_c.png")
        pass

    def move(self):
        if self.up:
            self.acc.y = -self.speed
        elif self.down:
            self.acc.y = self.speed
        else:
            self.acc.y = 0
        if self.left:
            self.acc.x = -self.speed
        elif self.right:
            self.acc.x = self.speed
        else:
            self.acc.x = 0
        self.pos += self.acc

        if self.pos.x + 8 > SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH - 8
        if self.pos.x < 8:
            self.pos.x = 8
        if self.pos.y + 8 > SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT - 8
        if self.pos.y < 8:
            self.pos.y = 8

        self.rect.center = self.pos

