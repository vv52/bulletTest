import pygame
from pygame.locals import *

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

OFFSET = SCREEN_HEIGHT / 8

WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255)
RED = (255, 0, 0)


def ShowResults(clock, screen, stage_points, total_points, stage_graze,
                total_graze, stage_gems, lives, clears, pass_stage, stage_name):
    background = pygame.image.load("res/img/results2.png")

    name_font = pygame.font.Font("res/misc/Symtext.ttf", 40)
    font = pygame.font.Font("res/misc/simsunb.ttf", 40)

    stage_name_text = name_font.render(stage_name, True, WHITE)
    if pass_stage:
        pass_stage_text = name_font.render("PASSED", True, TURQUOISE)
    else:
        pass_stage_text = name_font.render("FAILED", True, RED)
    stage_points_text = font.render(f"Stage Points: {stage_points}", True, WHITE)
    total_points_text = font.render(f"Total Points: {total_points}", True, WHITE)
    stage_graze_text = font.render(f"Stage Graze: {stage_graze}", True, WHITE)
    total_graze_text = font.render(f"Total Graze: {total_graze}", True, WHITE)
    lives_text = font.render(f"Remaining Lives: {lives}", True, WHITE)
    clears_text = font.render(f"Remaining Clears: {clears}", True, WHITE)
    stage_gems_text = font.render(f"Stage Gems: {stage_gems}", True, WHITE)

    stage_name_text_rect = stage_name_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET))
    pass_stage_text_rect = pass_stage_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET + 40))
    stage_points_text_rect = stage_points_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 3 - 40))
    total_points_text_rect = total_points_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 3))
    stage_graze_text_rect = stage_graze_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 4))
    total_graze_text_rect = total_graze_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 4 + 40))
    lives_text_rect = lives_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 5 + 40))
    clears_text_rect = clears_text.get_rect(center=(SCREEN_WIDTH / 2, OFFSET * 5 + 80))
    stage_gems_text_rect = stage_gems_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - OFFSET))

    results_screen = True
    while results_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                results_screen = False
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    results_screen = False
                    return 1
        screen.blit(background, background.get_rect())
        screen.blit(stage_name_text, stage_name_text_rect)
        screen.blit(pass_stage_text, pass_stage_text_rect)
        screen.blit(stage_points_text, stage_points_text_rect)
        screen.blit(total_points_text, total_points_text_rect)
        screen.blit(stage_graze_text, stage_graze_text_rect)
        screen.blit(total_graze_text, total_graze_text_rect)
        screen.blit(lives_text, lives_text_rect)
        screen.blit(clears_text, clears_text_rect)
        screen.blit(stage_gems_text, stage_gems_text_rect)
        pygame.display.flip()
