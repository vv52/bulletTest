import pygame
from pygame.locals import *
from pygame.math import Vector2
from random import Random
import math

vec = pygame.math.Vector2

WRANGE = 6


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, image, spawn_x, spawn_y, angle):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [spawn_x, spawn_y]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Bullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


class Bullet2(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


class WarblyBullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/warbly_bullet2.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        random_offset = vec((self.rand.randint(0, WRANGE) - (WRANGE / 2)),
                            (self.rand.randint(0, WRANGE) - (WRANGE / 2)))
        self.pos += self.velocity + random_offset
        self.rect.center = self.pos


class SpiralBullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 5
        self.frequency = 10
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet2(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 15
        self.frequency = 50
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet3(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = -30
        self.frequency = 50
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet3Inverse(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 30
        self.frequency = 50
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet4(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 3
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = -40
        self.frequency = 60
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 4
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet4Inverse(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 3
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 40
        self.frequency = 60
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 4
        self.pos += self.velocity
        self.rect.center = self.pos
