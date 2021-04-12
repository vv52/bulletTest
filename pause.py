import pygame
from pygame.locals import *

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255)


def PauseGame(font, screen, joysticks):
    pause_text = font.render("- [PAUSE] -", True, WHITE)
    pause_text_rect = pause_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    continue_text = font.render("CONTINUE", True, WHITE)
    continue_text_rect = continue_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 300))
    continue_text_sel = font.render("CONTINUE", True, TURQUOISE)
    restart_text = font.render("RESTART", True, WHITE)
    restart_text_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250))
    restart_text_sel = font.render("RESTART", True, TURQUOISE)
    title_text = font.render("TITLE", True, WHITE)
    title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200))
    title_text_sel = font.render("TITLE", True, TURQUOISE)
    quit_text = font.render("QUIT", True, WHITE)
    quit_text_rect = quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150))
    quit_text_sel = font.render("QUIT", True, TURQUOISE)
    menu_up = False
    menu_down = False
    menu_select = False
    state = 0
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    paused = False
                    return 1
                if event.key == pygame.K_UP:
                    menu_up = True
                if event.key == pygame.K_DOWN:
                    menu_down = True
                if event.key == pygame.K_RETURN:
                    menu_select = True
                if event.key == pygame.K_z:
                    menu_select = True
            if event.type == JOYBUTTONDOWN:
                if event.button == 9:
                    paused = False
                    return 1
                if event.button == 1 or event.button == 0 or event.button == 2:
                    menu_select = True
            if event.type == JOYAXISMOTION:
                if event.axis == 4:
                    if event.value < 0:
                        menu_up = True
                    elif event.value > 0:
                        menu_down = True
            if event.type == JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        if menu_up:
            if state > 0:
                state -= 1
        if menu_down:
            if state < 3:
                state += 1
        if menu_select:
            if state == 0:
                paused = False
                return 1
            if state == 1:
                return 2
                pass
            if state == 2:
                pass
            if state == 3:
                paused = False
                return 0

        if state == 0:
            screen.blit(continue_text_sel, continue_text_rect)
            screen.blit(restart_text, restart_text_rect)
            screen.blit(title_text, title_text_rect)
            screen.blit(quit_text, quit_text_rect)
        if state == 1:
            screen.blit(continue_text, continue_text_rect)
            screen.blit(restart_text_sel, restart_text_rect)
            screen.blit(title_text, title_text_rect)
            screen.blit(quit_text, quit_text_rect)
        if state == 2:
            screen.blit(continue_text, continue_text_rect)
            screen.blit(restart_text, restart_text_rect)
            screen.blit(title_text_sel, title_text_rect)
            screen.blit(quit_text, quit_text_rect)
        if state == 3:
            screen.blit(continue_text, continue_text_rect)
            screen.blit(restart_text, restart_text_rect)
            screen.blit(title_text, title_text_rect)
            screen.blit(quit_text_sel, quit_text_rect)
        menu_up = False
        menu_down = False
        menu_select = False
        screen.blit(pause_text, pause_text_rect)
        pygame.display.flip()