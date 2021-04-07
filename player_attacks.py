import pygame
from pygame.locals import *
import sprite

############################
# This is currently broken #
# ------------------------ #
# Also, I've decided that  #
# making a pacifist Touhou #
# game is more interesting #
# to me in the first place #
############################


def BeamAttack(x, y, p_attacks, sprites):
    new_beam = PlayerBeam(x, y)
    sprites.add(new_beam)
    p_attacks.add(new_beam)
    return new_beam


class PlayerBeam(sprite.Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/beam1.png", spawn_x, spawn_y)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/beam3.png"))
        self.rect = self.image.get_rect()
        self.doing_damage = False
        self.cancel = False
        self.frame_timer = 0
        self.anim = 0

    def update(self):
        self.frame_timer += 1
        if self.frame_timer % 10 == 0 and self.anim < 3:
            self.anim += 1
            self.image = pygame.image.load(f"res/img/beam{self.anim}.png")
        if self.anim == 3:
            self.doing_damage = True
        else:
            self.doing_damage = False
        if self.cancel:
            if self.frame_timer % 10 == 0 and self.anim > 0:
                self.anim -= 1
                self.image = pygame.image.load(f"res/img/beam{self.anim}.png")
            if self.anim == 0:
                self.kill()
