import pygame
import sprite

vec = pygame.math.Vector2

class Yukari(sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/yukari.png", spawn_x, spawn_y)
        self.pos = vec(self.rect.center)

    def update(self):
        self.rect.center = self.pos


class MagicCircle(sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/magic_circle.png", spawn_x, spawn_y)
        self.pos = vec(self.rect.center)
        self.frame = 0
        self.original_image = pygame.image.load("res/img/magic_circle.png")
        self.image = self.original_image
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 1 % 360
        cx, cy = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)
