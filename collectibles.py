import pygame
from pygame.locals import *
import sprite

vec = pygame.math.Vector2


class PointsOrb(sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/orb.png", spawn_x, spawn_y)
        self.mask = pygame.mask.from_surface(self.image)
        self.original_image = pygame.image.load("res/img/orb.png")
        self.image = self.original_image
        self.pos = vec(self.rect.center)
        self.angle = 0

    def update(self):
        cx, cy = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 4 % 360
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)
        self.rect.center = self.pos
