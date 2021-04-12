import pygame
from pygame.locals import *
import controls
import options_menu

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740


def TitleScreen(clock, screen, joysticks, options):
    background = pygame.image.load("res/img/menu.png")
    menu_up = False
    menu_down = False
    menu_select = False
    state = 0
    start_game_btn = pygame.image.load("res/img/start_game_button.png")
    start_game_btn_rect = start_game_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 112))
    controls_btn = pygame.image.load("res/img/controls_button.png")
    controls_btn_rect = controls_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 56))
    options_btn = pygame.image.load("res/img/options_button.png")
    options_btn_rect = options_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3)))
    exit_game_btn = pygame.image.load("res/img/exit_game_button.png")
    exit_game_btn_rect = exit_game_btn.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) + 56))

    title_screen = True
    while title_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                title_screen = False
                return 0, options
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_up = True
                if event.key == pygame.K_DOWN:
                    menu_down = True
                if event.key == pygame.K_RETURN:
                    menu_select = True
                if event.key == pygame.K_z:
                    menu_select = True
            if event.type == JOYBUTTONDOWN:
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
                return 1, options
            if state == 1:
                controls.ShowControls(clock, screen, joysticks)
            if state == 2:
                continue_game, options = options_menu.ShowOptions(clock, screen, joysticks, options)
                if continue_game == 0:
                    return 0, options
            if state == 3:
                return 0, options

        if state == 0:
            start_game_btn = pygame.image.load("res/img/start_game_button_sel.png")
        else:
            start_game_btn = pygame.image.load("res/img/start_game_button.png")
        if state == 1:
            controls_btn = pygame.image.load("res/img/controls_button_sel.png")
        else:
            controls_btn = pygame.image.load("res/img/controls_button.png")
        if state == 2:
            options_btn = pygame.image.load("res/img/options_button_sel.png")
        else:
            options_btn = pygame.image.load("res/img/options_button.png")
        if state == 3:
            exit_game_btn = pygame.image.load("res/img/exit_game_button_sel.png")
        else:
            exit_game_btn = pygame.image.load("res/img/exit_game_button.png")

        screen.blit(background, background.get_rect())
        screen.blit(start_game_btn, start_game_btn_rect)
        screen.blit(controls_btn, controls_btn_rect)
        screen.blit(options_btn, options_btn_rect)
        screen.blit(exit_game_btn, exit_game_btn_rect)
        pygame.display.flip()
        clock.tick(FPS)
        menu_up = False
        menu_down = False
        menu_select = False
