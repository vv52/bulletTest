import pygame
from pygame.locals import *
from time import time
import player
import attacks
import pause
import collectibles
import movement
from random import Random

FPS = 60

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255)
YELLOW = (255, 255, 0)

FAST = 5
SLOW = 2.5

vec = pygame.math.Vector2

clear_icon = pygame.image.load("res/img/clear.png")
life_icon = pygame.image.load("res/img/life.png")


def StageThree(boss, magic_circle, bullets, sprites, players, orbs,
             screen, font, clock, prev_points, player_one, player_magic_circle,
             lives, pause_differential, joysticks, options, e10, e25, e50):
    background = pygame.image.load("res/img/background8.png")
    best_time = time() - time()
    current_time = time() - time()
    start_time = time()
    rand = Random()
    phase_counter = 0
    frame_counter = 0
    ticker = 0
    best_points = 0
    death_loc = vec(0, 0)
    death = False
    death_counter = 1
    graze_counter = 0
    points = 0
    best_graze = 0
    last_graze_hit = False
    total_graze = 0
    total_gems = 0
    extend_10k = e10
    extend_25k = e25
    extend_50k = e50
    inv_text = font.render("INVINCIBLE", True, WHITE)
    inv_text_rect = inv_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40))
    warning_image = pygame.image.load("res/img/warning.png")
    warning_image_rect = warning_image.get_rect(center=(SCREEN_WIDTH / 4, SCREEN_HEIGHT - (SCREEN_HEIGHT / 8)))

    player_one.up = False
    player_one.down = False
    player_one.left = False
    player_one.right = False

    stage = True
    while stage:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stage = False
                return 0, points, total_graze, total_gems, player_one.clears, \
                       False, lives, pause_differential, player_one, extend_10k,\
                               extend_25k, extend_50k
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
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    pause_start = time()
                    unpause = pause.PauseGame(font, screen, joysticks)
                    pause_end = time()
                    pause_differential += pause_end - pause_start
                    if unpause == 2:
                        player_one.kill()
                        for obj in bullets:
                            obj.kill()
                        total_graze = 0
                        current_time = time() - time()
                        start_time = time()
                        points = 0
                        total_gems = 0
                        frame_counter = 0
                        phase_counter = 0
                        ticker = 0
                        lives = 2
                        extend_10k = False
                        extend_25k = False
                        extend_50k = False
                        player_one = player.Player(256, 660)
                        sprites.add(player_one)
                        players.add(player_one)
                    if not unpause:
                        stage = False
                        return 0, points, total_graze, total_gems, player_one.clears, \
                               False, lives, pause_differential, player_one, extend_10k,\
                               extend_25k, extend_50k
                if event.key == pygame.K_z and player_one.spawn_timer == 0:
                    if player_one.clears > 0:
                        player_one.clears -= 1
                        for bullet in bullets:
                            new_orb = collectibles.PointsOrb(bullet.pos.x, bullet.pos.y)
                            sprites.add(new_orb)
                            orbs.add(new_orb)
                            total_gems += 1
                            bullet.kill()
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
            if event.type == JOYBUTTONDOWN:
                if event.button == 1 and player_one.spawn_timer == 0:
                    if player_one.clears > 0:
                        player_one.clears -= 1
                        for bullet in bullets:
                            new_orb = collectibles.PointsOrb(bullet.pos.x, bullet.pos.y)
                            sprites.add(new_orb)
                            orbs.add(new_orb)
                            total_gems += 1
                            bullet.kill()
                if event.button == 7:
                    player_one.speed = SLOW
                if event.button == 9:
                    pause_start = time()
                    unpause = pause.PauseGame(font, screen, joysticks)
                    pause_end = time()
                    pause_differential += pause_end - pause_start
                    if unpause == 2:
                        player_one.kill()
                        for obj in bullets:
                            obj.kill()
                        total_graze = 0
                        current_time = time() - time()
                        start_time = time()
                        points = 0
                        total_gems = 0
                        frame_counter = 0
                        phase_counter = 0
                        ticker = 0
                        lives = 2
                        extend_10k = False
                        extend_25k = False
                        extend_50k = False
                        player_one = player.Player(256, 660)
                        sprites.add(player_one)
                        players.add(player_one)
                    if not unpause:
                        stage = False
                        return 0, points, total_graze, total_gems, player_one.clears, \
                               False, lives, pause_differential, player_one, extend_10k,\
                               extend_25k, extend_50k
            if event.type == JOYBUTTONUP:
                if event.button == 7:
                    player_one.speed = FAST
            if event.type == JOYAXISMOTION:
                if event.axis == 4:
                    if event.value < 0:
                        player_one.up = True
                    elif event.value > 0:
                        player_one.down = True
                    elif event.value == 0:
                        player_one.up = False
                        player_one.down = False
                if event.axis == 3:
                    if event.value < 0:
                        player_one.left = True
                    elif event.value > 0:
                        player_one.right = True
                    elif event.value == 0:
                        player_one.left = False
                        player_one.right = False
            if event.type == JOYDEVICEADDED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
                for joystick in joysticks:
                    print(joystick.get_name())
            if event.type == JOYDEVICEREMOVED:
                joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    # PHASE TRANSITION / RESET

        if phase_counter < 200:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE ONE

        if ticker == 360:
            ticker = 0
        if 1 <= phase_counter <= 900:
            magic_circle.fast = False
            if frame_counter % 5 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4", ticker, bullets, sprites)
            if frame_counter % 60 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 15, "b", -ticker, bullets, sprites)
            if frame_counter % 120 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 10, "w", ticker, bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0
        if 901 <= phase_counter <= 1800:
            if frame_counter % 5 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4", -ticker, bullets, sprites)
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4", -ticker - 10, bullets, sprites)
            if frame_counter % 30 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                                      10, "b", rand.randint(0, 89), bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0
        ticker += 1

    # PHASE TRANSITION

        if 1800 < phase_counter < 1980:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE TWO

        if 1980 <= phase_counter <= 3780:
            magic_circle.fast = False
            if frame_counter % 120 < 60:
                if frame_counter % 5 == 0:
                    attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                                          6, "s4", -ticker, bullets, sprites)
                    attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                                          6, "s4i", -ticker - 10, bullets, sprites)
            if frame_counter % 120 == 60:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                                      30, "b2", rand.randint(0,45), bullets, sprites)

    # PHASE TRANSITION

    #    if 3780 < phase_counter < 4060:
    #        at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8))
    #        if not at_position:
    #            magic_circle.fast = True
    #        magic_circle.rect.center = boss.rect.center

    # PHASE THREE

    #    if 3960 <= phase_counter <= 5760:
    #        magic_circle.fast = False
    #        if frame_counter % 30 == 0:
    #            if ticker < 40:
    #                ticker += 1
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8),
    #                                  ticker, "s4", ticker * 10, bullets, sprites)
    #        if frame_counter % 60 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 4, SCREEN_HEIGHT - (SCREEN_HEIGHT / 8)),
    #                                  15, "s2", rand.randint(0, 360), bullets, sprites)
    #        if frame_counter % 100 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8),
    #                                  ticker / 5, "s4i", ticker * 2, bullets, sprites)
    #        if frame_counter == 600:
    #            frame_counter = 0

    #    if 5760 < phase_counter < 6040:
    #        at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT / 8))
    #        if not at_position:
    #            magic_circle.fast = True
    #        magic_circle.rect.center = boss.rect.center

    # PHASE FOUR

    #    if 5940 <= phase_counter <= 7740:
    #        magic_circle.fast = False
    #        if frame_counter % 30 == 0:
    #            if ticker < 40:
    #                ticker += 1
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT / 8),
    #                                  ticker, "s4", ticker * 10, bullets, sprites)
    #        if frame_counter % 60 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 4, SCREEN_HEIGHT - (SCREEN_HEIGHT / 8)),
    #                                  15, "s2", rand.randint(0, 360), bullets, sprites)
    #        if frame_counter % 100 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH - (SCREEN_WIDTH / 4), SCREEN_HEIGHT / 8),
    #                                  ticker / 5, "s4i", ticker * 2, bullets, sprites)
    #        if frame_counter == 600:
    #            frame_counter = 0

    # PHASE TRANSITION

    #    if 7740 < phase_counter < 7800:
    #        at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 10))
    #        if not at_position:
    #            magic_circle.fast = True
    #        magic_circle.rect.center = boss.rect.center

    # PHASE FOUR AND A HALF

    #    if 7800 <= phase_counter <= 8020:
    #        magic_circle.fast = False
    #        if frame_counter % 10 == 0:
    #            attacks.BarSpawner(32, 80, rand.randint(45, 135), "w", bullets, sprites)
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH - 16, 16), 10, "b", rand.randint(90, 135), bullets, sprites)
    #            attacks.CircleSpawner(vec(16, 16), 10, "b", rand.randint(0, 45), bullets, sprites)
    #        if frame_counter == 60:
    #            frame_counter = 0

    # PHASE TRANSITION

    #    if 8020 < phase_counter < 8200:
    #        at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    #        if not at_position:
    #            magic_circle.fast = True
    #        magic_circle.rect.center = boss.rect.center

    #    if phase_counter == 8199:
    #        for bullet in bullets:
    #            bullet.kill()

    # PHASE FIVE

    #    if 8200 <= phase_counter <= 10000:
    #        magic_circle.fast = False
    #        if frame_counter % 10 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    #                                  5, "b", rand.randint(0, 360), bullets, sprites)
    #        if frame_counter % 100 == 0:
    #            if phase_counter < 9100:
    #                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    #                                  40, "s4i", rand.randint(0, 360), bullets, sprites)
    #            else:
    #                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    #                                      40, "s4", rand.randint(0, 360), bullets, sprites)
    #        if frame_counter % 500 == 0:
    #            attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
    #                                  20, "w", rand.randint(0, 360), bullets, sprites)

    # END STAGE

        if phase_counter == 10000:
            for bullet in bullets:
                bullet.kill()

        if phase_counter > 10300:
            magic_circle.fast = False
            stage = False
            return 1, points, total_graze, total_gems, player_one.clears, True, lives, pause_differential, player_one, \
                   extend_10k, extend_25k, extend_50k

    # HANDLE PLAYER

        player_one.move()
        player_magic_circle.rect.center = player_one.rect.center

        for orb in orbs:
            if orb.pos != player_one.pos:
                if player_one.pos.x - orb.pos.x > 400 or player_one.pos.y - orb.pos.y > 400:
                    orb.pos += (player_one.pos - orb.pos) / 32
                elif player_one.pos.x - orb.pos.x > 200 or player_one.pos.y - orb.pos.y > 200:
                    orb.pos += (player_one.pos - orb.pos) / 16
                elif player_one.pos.x - orb.pos.x > 100 or player_one.pos.y - orb.pos.y > 100:
                    orb.pos += (player_one.pos - orb.pos) / 8
                else:
                    orb.pos += (player_one.pos - orb.pos) / 4

        for bullet in bullets:
            player_one_hit = pygame.sprite.collide_mask(player_one, bullet)
            if player_one_hit and player_one.spawn_timer == 0:
                if options["auto_clear"] == "on" and player_one.clears > 0:
                    player_one.clears -= 1
                    for bullet in bullets:
                        new_orb = collectibles.PointsOrb(bullet.pos.x, bullet.pos.y)
                        sprites.add(new_orb)
                        orbs.add(new_orb)
                        total_gems += 1
                        bullet.kill()
                else:
                    death = True
                    death_loc = player_one.rect.center
                    player_one.kill()
                    for obj in bullets:
                        obj.kill()
                    if options["keep_graze"] == "off":
                        total_graze = 0
                    if lives == 0:
                        stage = False
                        return 1, points, total_graze, total_gems, player_one.clears, \
                               False, lives, pause_differential, player_one, extend_10k,\
                               extend_25k, extend_50k
                    else:
                        lives -= 1
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

        graze_hit = pygame.sprite.spritecollide(player_one, bullets, False)
        if graze_hit:
            player_magic_circle.fast = True
            player_one.grazing = True
            if last_graze_hit:
                graze_counter += 1
                total_graze += 1
                if total_graze != 0 and total_graze % 1000 == 0 and player_one.clears < 5:
                    player_one.clears += 1
        else:
            player_magic_circle.fast = False
            player_one.grazing = False
            if last_graze_hit:
                if graze_counter > best_graze:
                    best_graze = graze_counter
                graze_counter = 0
        last_graze_hit = player_one.grazing

        orb_hits = pygame.sprite.spritecollide(player_one, orbs, True)
        if orb_hits:
            for hit in orb_hits:
                points += 5

        # DRAW TO SCREEN

        screen.blit(background, background.get_rect())
        for obj in sprites:
            obj.draw(screen)
            obj.update()

        player_one.draw(screen)

        if death:
            explosion = pygame.image.load(f"res/img/pop{death_counter}.png")
            explosion_rect = explosion.get_rect(center=death_loc)
            screen.blit(explosion, explosion_rect)
            if phase_counter % 5 == 0:
                death_counter += 1
            if death_counter > 5:
                death_counter = 1
                death = False

        points_text = font.render(f"{points + prev_points}", True, WHITE)
        points_text_rect = points_text.get_rect(center=(SCREEN_WIDTH - 80, 40))
        total_gems_text = font.render(f"{total_gems}", True, YELLOW)
        total_gems_text_rect = total_gems_text.get_rect(center=(80, 40))
        graze_count_text = font.render(f"{graze_counter}", True, TURQUOISE)
        graze_count_text_rect = graze_count_text.get_rect(center=(SCREEN_WIDTH - 80, 60))
        total_graze_text = font.render(f"{total_graze}", True, TURQUOISE)
        total_graze_text_rect = total_graze_text.get_rect(center=(80, 60))

        if phase_counter < 10000:
            screen.blit(points_text, points_text_rect)
        else:
            if phase_counter % 10 < 5:
                screen.blit(points_text, points_text_rect)
        screen.blit(total_gems_text, total_gems_text_rect)
        screen.blit(graze_count_text, graze_count_text_rect)
        screen.blit(total_graze_text, total_graze_text_rect)

        if player_one.clears > 0:
            clears = player_one.clears
            while clears > 0:
                screen.blit(clear_icon, clear_icon.get_rect(center=((40 * clears), SCREEN_HEIGHT - 40)))
                clears -= 1

        if lives > 0:
            lives_index = lives
            while lives_index > 0:
                screen.blit(life_icon,
                            life_icon.get_rect(center=((SCREEN_WIDTH - (40 * lives_index)), SCREEN_HEIGHT - 40)))
                lives_index -= 1

        if phase_counter <= 300:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE ONE", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
        if 1980 <= phase_counter <= 2280:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE TWO", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
        if 3860 <= phase_counter < 3960:
            if phase_counter % 80 < 50:
                if phase_counter % 10 < 5:
                    screen.blit(warning_image, warning_image_rect)
        if 3960 <= phase_counter <= 4260:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE THREE", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
            if phase_counter % 80 < 50:
                if phase_counter % 10 < 5:
                    screen.blit(warning_image, warning_image_rect)
        if 5940 <= phase_counter <= 6240:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE FOUR", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
            if phase_counter % 80 < 50:
                if phase_counter % 10 < 5:
                    screen.blit(warning_image, warning_image_rect)
        if 8200 <= phase_counter <= 8500:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE FIVE", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
        if 10000 <= phase_counter <= 10300:
            if phase_counter % 60 < 30:
                phase_text = font.render("STAGE CLEAR", True, TURQUOISE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)

        if player_one.spawn_timer > 0:
            if phase_counter % 20 < 10:
                screen.blit(inv_text, inv_text_rect)

        # FRAME UPKEEP

        pygame.display.flip()
        clock.tick(FPS)
        frame_counter += 1
        phase_counter += 1
        if phase_counter < 10000:
            if player_one.grazing:
                if 1000 <= graze_counter < 2500:
                    points += 3
                elif graze_counter > 2500:
                    points += 4
                else:
                    points += 2
            else:
                points += 1
        if points > 10000 and not extend_10k:
            extend_10k = True
            if lives < 3:
                lives += 1
        if points > 25000 and not extend_25k:
            extend_25k = True
            if lives < 3:
                lives += 1
        if points > 50000 and not extend_50k:
            extend_50k = True
            if lives < 3:
                lives += 1