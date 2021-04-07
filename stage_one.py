import pygame
from pygame.locals import *
from time import time
from datetime import datetime, timedelta
import player
import attacks
from random import Random

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

FAST = 5
SLOW = 2.5

vec = pygame.math.Vector2


def StageOne(boss, magic_circle, bullets, sprites, players, screen, font, font_color, clock, FPS, player_one):
    background = pygame.image.load("res/img/background6.png")
    best_time = time() - time()
    current_time = time() - time()
    start_time = time()
    rand = Random()
    phase_counter = 0
    frame_counter = 0
    ticker = 0

    stage = True
    while stage:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stage = False
                return 0
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

        if phase_counter < 1800:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 3:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 3:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

    # phase one
        if phase_counter <= 1800:
            if frame_counter % 25 == 0:
                if ticker < 20:
                    ticker += 1
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker, "b", ticker * 10, bullets, sprites)
            if frame_counter % 100 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker / 2, "w", 0, bullets, sprites)
            if frame_counter % 245 == 0 or frame_counter % 250 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker * 2, "s", ticker, bullets, sprites)
            if frame_counter == 500:
                frame_counter = 0

        if 1800 < phase_counter < 1980:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 4:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 4:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

    # phase two
        if 1980 <= phase_counter <= 3780:
            if frame_counter % 30 == 0:
                if ticker < 30:
                    ticker += 2
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                              3, "b", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 60 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                              2, "s", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 120 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4), ticker * 2, "w", 0, bullets, sprites)
            if frame_counter == 480:
                frame_counter = 0

        if 3780 < phase_counter < 3960:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 3:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 3:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

    # phase three
        if 3960 <= phase_counter <= 4760:
            if frame_counter % 30 == 0:
                if ticker < 30:
                    ticker += 1
                #if ticker < 50:
                #    ticker += 2
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker, "s2", ticker * 10, bullets, sprites)
            if frame_counter % 100 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker / 5, "s3", ticker * 2, bullets, sprites)
            if frame_counter % 300 == 0:
                attacks.BarSpawner(32, 20, 90, "b2", bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0

        if 4760 < phase_counter < 4940:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 8:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 8:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

    # phase four
        if 4940 <= phase_counter <= 6740:
            if frame_counter % 60 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8),
                              50, "b", rand.randint(45, 135), bullets, sprites)
            if frame_counter % 200 == 0:
                attacks.BarSpawner(SCREEN_HEIGHT / 8, 20, 90, "w", bullets, sprites)
            if frame_counter % 300 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                              25, "s", rand.randint(0, 360), bullets, sprites)
            if frame_counter == 600 == 0:
                frame_counter = 0

        if 6740 < phase_counter < 6800:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 10):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 10:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 10:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

    # phase four and a half
        if 6800 <= phase_counter <= 7020:
            if frame_counter % 10 == 0:
                attacks.BarSpawner(32, 10, rand.randint(45, 135), "b2", bullets, sprites)
            if frame_counter == 60:
                frame_counter = 0

        if 7020 < phase_counter < 7200:
            if boss.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2):
                if boss.pos.x < SCREEN_WIDTH / 2:
                    boss.pos.x += 1
                elif boss.pos.x > SCREEN_WIDTH / 2:
                    boss.pos.x -= 1
                if boss.pos.y < SCREEN_HEIGHT / 2:
                    boss.pos.y += 1
                elif boss.pos.y > SCREEN_HEIGHT / 2:
                    boss.pos.y -= 1
                magic_circle.rect.center = boss.rect.center

        if phase_counter == 7199:
            for bullet in bullets:
                bullet.kill()

    # phase five
        if 7200 <= phase_counter <= 9000:
            if frame_counter % 30 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                              5, "b2", rand.randint(45, 135), bullets, sprites)
            if frame_counter % 90 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, 8),
                              40, "s3", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 120 == 0:
                attacks.BarSpawner(SCREEN_HEIGHT - 8, 30, 270, "b", bullets, sprites)

    # if over 9000
        if phase_counter > 9000:
            stage = False
            return 1

        player_one.move()

        for bullet in bullets:
            player_one_hit = pygame.sprite.collide_mask(player_one, bullet)
            if player_one_hit:
                player_one.kill()
                for obj in bullets:
                    obj.kill()
                if current_time - start_time > best_time:
                    best_time = current_time - start_time
                current_time = time() - time()
                start_time = time()
                frame_counter = 0
                phase_counter = 0
                ticker = 0
                player_one = player.Player(256, 660)
                sprites.add(player_one)
                players.add(player_one)
            if bullet.rect.x < 0:
                bullet.kill()
            elif bullet.rect.x > SCREEN_WIDTH:
                bullet.kill()
            elif bullet.rect.y > SCREEN_HEIGHT:
                bullet.kill()
            elif bullet.rect.y < 0:
                bullet.kill()

        screen.blit(background, background.get_rect())
        for obj in sprites:
            obj.draw(screen)
            obj.update()

        current_time = time()
        sec = timedelta(seconds=int(current_time - start_time))
        sec2 = timedelta(seconds=int(best_time))
        d = datetime(1, 1, 1) + sec
        dd = datetime(1, 1, 1) + sec2
        time_text = font.render(f"%d:%d:%d" % (d.hour, d.minute, d.second), True, font_color)
        time_text_rect = time_text.get_rect(center=(SCREEN_WIDTH - 80, 40))
        best_text = font.render(f"%d:%d:%d" % (dd.hour, dd.minute, dd.second), True, font_color)
        best_text_rect = best_text.get_rect(center=(80, 40))
        screen.blit(time_text, time_text_rect)
        screen.blit(best_text, best_text_rect)

        pygame.display.flip()
        clock.tick(FPS)
        frame_counter += 1
        phase_counter += 1