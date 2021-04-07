import pygame
from pygame.locals import *

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

WHITE = (255, 255, 255)


def PauseGame(font, screen):
    pause_text = font.render("PAUSE", True, WHITE)
    pause_text_rect = pause_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                    return 1
        screen.blit(pause_text, pause_text_rect)
        pygame.display.flip()