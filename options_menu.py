import pygame
from pygame.locals import *
import json

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740


def ShowOptions(clock, screen, joysticks, options):
    background = pygame.image.load("res/img/menu.png")
    menu_up = False
    menu_down = False
    menu_select = False
    state = 0

    auto_clear_btn = pygame.image.load("res/img/auto_clear_button.png")
    auto_clear_btn_rect =\
        auto_clear_btn.get_rect(center=(SCREEN_WIDTH / 4, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 112))
    save_exit_btn = pygame.image.load("res/img/save_exit_button.png")
    save_exit_btn_rect =\
        save_exit_btn.get_rect(center=(SCREEN_WIDTH / 4, SCREEN_HEIGHT - (SCREEN_HEIGHT / 3)))
    exit_nosave_btn = pygame.image.load("res/img/exit_nosave_button.png")
    exit_nosave_btn_rect =\
        exit_nosave_btn.get_rect(center=(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT - (SCREEN_HEIGHT / 3)))

    on_btn = pygame.image.load("res/img/on.png")
    off_btn = pygame.image.load("res/img/off.png")
    on_off_btn_rect = \
        on_btn.get_rect(center=(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT - (SCREEN_HEIGHT / 3) - 112))

    with open("res/misc/settings.json") as json_file:
        options = json.load(json_file)

    no_options = options

    if options["auto_clear"] == "on":
        auto_clear = True
    else:
        auto_clear = False

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
            if state < 2:
                state += 1
        if menu_select:
            if state == 0:
                if auto_clear:
                    auto_clear = False
                    options["auto_clear"] = "off"
                else:
                    auto_clear = True
                    options["auto_clear"] = "on"
            if state == 1:
                with open("res/misc/settings.json", "w") as settings_file:
                    json.dump(options, settings_file)
                return options
            if state == 2:
                options = no_options
                if no_options["auto_clear"] == "off":
                    auto_clear = False
                else:
                    auto_clear = True
                return options

        if state == 0:
            auto_clear_btn = pygame.image.load("res/img/auto_clear_button_sel.png")
        else:
            auto_clear_btn = pygame.image.load("res/img/auto_clear_button.png")
        if state == 1:
            save_exit_btn = pygame.image.load("res/img/save_exit_button_sel.png")
        else:
            save_exit_btn = pygame.image.load("res/img/save_exit_button.png")
        if state == 2:
            exit_nosave_btn = pygame.image.load("res/img/exit_nosave_button_sel.png")
        else:
            exit_nosave_btn = pygame.image.load("res/img/exit_nosave_button.png")

        screen.blit(background, background.get_rect())
        screen.blit(auto_clear_btn, auto_clear_btn_rect)
        if auto_clear:
            screen.blit(on_btn, on_off_btn_rect)
        else:
            screen.blit(off_btn, on_off_btn_rect)
        screen.blit(save_exit_btn, save_exit_btn_rect)
        screen.blit(exit_nosave_btn, exit_nosave_btn_rect)
        pygame.display.flip()
        clock.tick(FPS)
        menu_up = False
        menu_down = False
        menu_select = False
