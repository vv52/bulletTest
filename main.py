import pygame
from pygame.locals import *
from pygame.math import Vector2
from random import Random
from time import time
from datetime import datetime, timedelta
import player
import stage_one
import stage_two
import yukari
import title
import results
import sys

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255)

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

    font = pygame.font.Font("res/misc/Symtext.ttf", 24)

    sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    circles = pygame.sprite.Group()
    orbs = pygame.sprite.Group()

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

    lives = 2
    total_points = 0
    total_graze = 0
    total_gems = 0
    stage_clears = 0
    stage_points = 0
    stage_graze = 0
    stage_gems = 0

    stage_times = []
    total_time = time() - time()
    pause_differential = time() - time()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False

    # TITLE

        title_check = title.TitleScreen(clock, screen)
        if not title_check:
            running = False
            break

    # STAGE ONE

        start_time = time()
        pass_stage, stage_points, stage_graze, stage_gems, stage_clears,\
            lives, pause_differential = stage_one.StageOne(boss, magic_circle, bullets, sprites, players,
                                                           orbs, screen, font, clock, total_points, player_one,
                                                           player_magic_circle, lives, pause_differential)
        end_time = time()
        if not pass_stage:
            running = False
            break
        stage_times.append(end_time - start_time - pause_differential)
        total_points += stage_points
        total_graze += stage_graze

    # STAGE ONE RESULTS

        results_check = results.ShowResults(clock, screen, stage_points, total_points, stage_graze,
                                            total_graze, stage_gems, lives, stage_clears, pass_stage, "STAGE ONE")

    # STAGE TWO

        start_time = time()
        pass_stage, stage_points, stage_graze, stage_clears, \
        lives, pause_differential = stage_two.StageTwo(boss, magic_circle, bullets, sprites, players,
                                                       orbs, screen, font, clock, total_points, player_one,
                                                       player_magic_circle, lives, pause_differential)
        end_time = time()
        if not pass_stage:
            running = False
            break
        stage_times.append(end_time - start_time - pause_differential)
        total_points += stage_points
        total_graze += stage_graze

    pygame.display.quit()                           # More graceful exit handling
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()