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

running = True


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print(joystick.get_name())

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
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

    options = []

    auto_clear = False

    global running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False
            if event.type == JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    # TITLE

        continue_game, options = title.TitleScreen(clock, screen, joysticks)
        if not continue_game:
            running = False
            break

        for option in options:
            if option == "auto_clear":
                auto_clear = True

    # STAGE ONE

        start_time = time()
        continue_game, stage_points, stage_graze, stage_gems, stage_clears, pass_stage, lives,\
            pause_differential, player_one = stage_one.StageOne(boss, magic_circle, bullets, sprites, players,
                                                                orbs, screen, font, clock, total_points, player_one,
                                                                player_magic_circle, lives, pause_differential,
                                                                joysticks, auto_clear)
        end_time = time()
        if not continue_game:
            running = False
            break
        stage_times.append(end_time - start_time - pause_differential)
        total_points += stage_points
        total_graze += stage_graze
        total_gems += stage_gems

    # STAGE ONE RESULTS

        continue_game = results.ShowResults(clock, screen, stage_points, total_points, stage_graze, total_graze,
                                            stage_gems, lives, stage_clears, pass_stage, joysticks, auto_clear,
                                            "STAGE ONE")
        if not continue_game:
            running = False
            break

    # STAGE TWO

        if pass_stage:
            player_one.pos = vec(256, 660)
            start_time = time()
            continue_game, stage_points, stage_graze, stage_gems, stage_clears, pass_stage, lives,\
                pause_differential, player_one = stage_two.StageTwo(boss, magic_circle, bullets, sprites, players,
                                                                    orbs, screen, font, clock, total_points, player_one,
                                                                    player_magic_circle, lives, pause_differential,
                                                                    joysticks, auto_clear)
            end_time = time()
            if not continue_game:
                running = False
                break
            stage_times.append(end_time - start_time - pause_differential)
            total_points += stage_points
            total_graze += stage_graze
            total_gems += stage_gems

    # STAGE TWO RESULTS

            continue_game = results.ShowResults(clock, screen, stage_points, total_points, stage_graze, total_graze,
                                                stage_gems, lives, stage_clears, pass_stage, joysticks, "STAGE TWO")
            if not continue_game:
                running = False
                break

    # RESET ON FAIL

        if not pass_stage:
            player_one = player.Player(256, 660)
            sprites.add(player_one)
            players.add(player_one)
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

    pygame.display.quit()                           # More graceful exit handling
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()