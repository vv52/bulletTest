import pygame
from pygame.locals import *

FPS = 60


def ShowControls(clock, screen, joysticks):
    background = pygame.image.load("res/img/controls.png")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False
                return 0
            if event.type == pygame.KEYDOWN:
                running = False
                return 1
            if event.type == JOYBUTTONDOWN:
                running = False
                return 1
            if event.type == JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        screen.blit(background, background.get_rect())
        pygame.display.flip()
        clock.tick(FPS)
