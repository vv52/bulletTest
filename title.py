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
import controls
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


def TitleScreen(clock, screen):
    background = pygame.image.load("res/img/menu.png")
    menu_up = False
    menu_down = False
    menu_select = False
    state = 0
    start_game_btn = pygame.image.load("res/img/start_game_button.png")
    start_game_btn_rect = start_game_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 112))
    controls_btn = pygame.image.load("res/img/controls_button.png")
    controls_btn_rect = controls_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 56))
    exit_game_btn = pygame.image.load("res/img/exit_game_button.png")
    exit_game_btn_rect = exit_game_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3)))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_up = True
                if event.key == pygame.K_DOWN:
                    menu_down = True
                if event.key == pygame.K_RETURN:
                    menu_select = True

        if menu_up:
            if state > 0:
                state -= 1
        if menu_down:
            if state < 2:
                state += 1
        if menu_select:
            if state == 0:
                return 1
            if state == 1:
                controls.ShowControls(clock, screen)
            if state == 2:
                return 0

        if state == 0:
            start_game_btn = pygame.image.load("res/img/start_game_button_sel.png")
        else:
            start_game_btn = pygame.image.load("res/img/start_game_button.png")
        if state == 1:
            controls_btn = pygame.image.load("res/img/controls_button_sel.png")
        else:
            controls_btn = pygame.image.load("res/img/controls_button.png")
        if state == 2:
            exit_game_btn = pygame.image.load("res/img/exit_game_button_sel.png")
        else:
            exit_game_btn = pygame.image.load("res/img/exit_game_button.png")

        screen.blit(background, background.get_rect())
        screen.blit(start_game_btn, start_game_btn_rect)
        screen.blit(controls_btn, controls_btn_rect)
        screen.blit(exit_game_btn, exit_game_btn_rect)
        pygame.display.flip()
        clock.tick(FPS)
        menu_up = False
        menu_down = False
        menu_select = False
