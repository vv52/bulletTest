import pygame
from pygame.locals import *
from pygame.math import Vector2
from random import Random
from time import time
from datetime import datetime, timedelta
import player
import stage_one
import yukari
import sys

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FAST = 5
SLOW = 2.5

vec = pygame.math.Vector2


def main():
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)
    pygame.display.set_caption("Touhou: Destitute Dreamscape (alpha demo)")

    font_color = WHITE
    font = pygame.font.Font("res/misc/Symtext.ttf", 24)

    sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    circles = pygame.sprite.Group()

    player_one = player.Player(256, 660)
    sprites.add(player_one)
    players.add(player_one)

    magic_circle = yukari.MagicCircle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    player_magic_circle = player.PlayerMagicCircle(256, 660)
    sprites.add(magic_circle)
    sprites.add(player_magic_circle)
    circles.add(magic_circle)
    circles.add(player_magic_circle)

    boss = yukari.Yukari(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    sprites.add(boss)
    bosses.add(boss)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_one.up = True
                if event.key == pygame.K_DOWN:
                    player_one.down = True
                if event.key == pygame.K_LEFT:
                    player_one.left = True
                if event.key == pygame.K_RIGHT:
                    player_one.right = True
                if event.key == pygame.K_LSHIFT:
                    player_one.speed = SLOW
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_one.up = False
                if event.key == pygame.K_DOWN:
                    player_one.down = False
                if event.key == pygame.K_LEFT:
                    player_one.left = False
                if event.key == pygame.K_RIGHT:
                    player_one.right = False
                if event.key == pygame.K_LSHIFT:
                    player_one.speed = FAST

        start_time = time()
        pass_stage = stage_one.StageOne(boss, magic_circle, bullets, sprites, players, screen,
                                        font, font_color, clock, FPS, player_one, player_magic_circle)
        end_time = time()
        stage_one_time = end_time - start_time
        if not pass_stage:
            running = False

    pygame.display.quit()                           # More graceful exit handling
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()