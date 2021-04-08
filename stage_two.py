import pygame
from pygame.locals import *
from time import time
import player
import attacks
import pause
import collectibles
import movement
from random import Random

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TURQUOISE = (0, 255, 255)

FAST = 5
SLOW = 2.5

vec = pygame.math.Vector2

clear_icon = pygame.image.load("res/img/clear.png")
life_icon = pygame.image.load("res/img/life.png")

# handle returning pause differential


def StageTwo(boss, magic_circle, bullets, sprites, players, orbs,
             screen, font, clock, FPS, player_one, player_magic_circle,
             lives, pause_differential):
    background = pygame.image.load("res/img/background7.png")
    best_time = time() - time()
    current_time = time() - time()
    start_time = time()
    rand = Random()
    phase_counter = 0
    frame_counter = 0
    ticker = 0
    points = 0
    best_points = 0
    death_loc = vec(0, 0)
    death = False
    death_counter = 1
    graze_counter = 0
    best_graze = 0
    last_graze_hit = False
    total_graze = 0
    extend_10k = False
    extend_20k = False
    inv_text = font.render("INVINCIBLE", True, WHITE)
    inv_text_rect = inv_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40))

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
                if event.key == pygame.K_p:
                    pause_start = time()
                    unpause = pause.PauseGame(font, screen)
                    pause_end = time()
                    pause_differential += pause_end - pause_start
                    if not unpause:
                        stage = False
                        return 0
                if event.key == pygame.K_z:
                    if player_one.clears > 0:
                        player_one.clears -= 1
                        for bullet in bullets:
                            new_orb = collectibles.PointsOrb(bullet.pos.x, bullet.pos.y)
                            sprites.add(new_orb)
                            orbs.add(new_orb)
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

    # PHASE TRANSITION / RESET

        if phase_counter < 200:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE ONE

        if 1 <= phase_counter <= 1800:
            magic_circle.fast = False
            if frame_counter % 30 == 0:
                if frame_counter % 60 == 0:
                    attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3),
                                          3, "s4", 0, bullets, sprites)
                else:
                    attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), 5, "s4i", 0, bullets, sprites)
            if frame_counter % 50 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH - 16, 16), 10, "b2", rand.randint(90, 135), bullets, sprites)
                attacks.CircleSpawner(vec(16, 16), 10, "b2", rand.randint(0, 45), bullets, sprites)
            if frame_counter % 60 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3),
                                      rand.randint(1, 10), "w", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 600 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 8, (SCREEN_HEIGHT - SCREEN_HEIGHT / 8)),
                                      rand.randint(3, 7), "s4", 180, bullets, sprites)
                attacks.CircleSpawner(vec(SCREEN_WIDTH - (SCREEN_WIDTH /8), SCREEN_HEIGHT - (SCREEN_HEIGHT / 8)),
                                      rand.randint(3, 7), "s4i", 180, bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0

    # PHASE TRANSITION

        if 1800 < phase_counter < 1980:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE TWO

        if phase_counter == 1979:
            for bullet in bullets:
                bullet.kill()
        if 1980 <= phase_counter <= 3780:
            magic_circle.fast = False
            if frame_counter % 50 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4i",
                                      frame_counter % 360, bullets, sprites)
            if frame_counter % 52 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4",
                                      frame_counter % 360, bullets, sprites)
            if frame_counter % 54 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 5, "s4i",
                                      frame_counter % 360, bullets, sprites)
            if frame_counter % 100 == 0:
                if frame_counter % 200 == 0:
                    attacks.QuarterSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 30, "b2", 30, bullets, sprites)
                    attacks.QuarterSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 30, "b2", 210, bullets, sprites)
                else:
                    attacks.QuarterSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 30, "b2", -30, bullets, sprites)
                    attacks.QuarterSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 30, "b2", 150, bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0

# CHANGE EVERYTHING BELOW HERE

    # PHASE TRANSITION

        if 3780 < phase_counter < 3960:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE THREE

        if 3960 <= phase_counter <= 5760:
            magic_circle.fast = False
            if frame_counter % 30 == 0:
                if ticker < 30:
                    ticker += 1
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker, "s2", ticker * 10, bullets, sprites)
            if frame_counter % 100 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker / 5, "s3", ticker * 2, bullets, sprites)
            if frame_counter % 300 == 0:
                attacks.BarSpawner(32, 20, 90, "b2", bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0

        if 5760 < phase_counter < 5940:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE FOUR

        if 5940 <= phase_counter <= 7740:
            magic_circle.fast = False
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

    # PHASE TRANSITION

        if 7740 < phase_counter < 7800:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 10))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

    # PHASE FOUR AND A HALF

        if 7800 <= phase_counter <= 8020:
            magic_circle.fast = False
            if frame_counter % 10 == 0:
                attacks.BarSpawner(32, 10, rand.randint(45, 135), "b2", bullets, sprites)
            if frame_counter == 60:
                frame_counter = 0

    # PHASE TRANSITION

        if 8020 < phase_counter < 8200:
            at_position = movement.FrameMove(boss.pos, vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            if not at_position:
                magic_circle.fast = True
            magic_circle.rect.center = boss.rect.center

        if phase_counter == 8199:
            for bullet in bullets:
                bullet.kill()

    # PHASE FIVE

        if 8200 <= phase_counter <= 10000:
            magic_circle.fast = False
            if frame_counter % 30 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                              5, "b2", rand.randint(45, 135), bullets, sprites)
            if frame_counter % 90 == 0:
                attacks.CircleSpawner(vec(SCREEN_WIDTH / 2, 8),
                              40, "s3", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 120 == 0:
                attacks.BarSpawner(SCREEN_HEIGHT - 8, 20, 270, "w", bullets, sprites)

    # END STAGE

        if phase_counter > 10000:
            magic_circle.fast = False
            stage = False
            return 1

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
                death = True
                death_loc = player_one.rect.center
                player_one.kill()
                for obj in bullets:
                    obj.kill()
                total_graze = 0
                if lives == 0:
                    if current_time - start_time > best_time:
                        best_time = current_time - start_time
                    if points > best_points:
                        best_points = points
                    current_time = time() - time()
                    start_time = time()
                    points = 0
                    frame_counter = 0
                    phase_counter = 0
                    ticker = 0
                    lives = 2
                    extend_10k = False
                    extend_20k = False
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

        points_text = font.render(f"{points}", True, WHITE)
        points_text_rect = points_text.get_rect(center=(SCREEN_WIDTH - 80, 40))
        best_points_text = font.render(f"{best_points}", True, WHITE)
        best_points_text_rect = best_points_text.get_rect(center=(80, 40))
        graze_count_text = font.render(f"{graze_counter}", True, TURQUOISE)
        graze_count_text_rect = graze_count_text.get_rect(center=(SCREEN_WIDTH - 80, 60))
        best_graze_text = font.render(f"{best_graze}", True, TURQUOISE)
        best_graze_text_rect = best_graze_text.get_rect(center=(80, 60))

        screen.blit(points_text, points_text_rect)
        screen.blit(best_points_text, best_points_text_rect)
        screen.blit(graze_count_text, graze_count_text_rect)
        screen.blit(best_graze_text, best_graze_text_rect)

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
        if 3960 <= phase_counter <= 4260:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE THREE", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
        if 4940 <= phase_counter <= 5240:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE FOUR", True, WHITE)
                phase_text_rect = phase_text.get_rect(center=(SCREEN_WIDTH / 2, 40))
                screen.blit(phase_text, phase_text_rect)
        if 7200 <= phase_counter <= 7500:
            if phase_counter % 60 < 30:
                phase_text = font.render("PHASE FIVE", True, WHITE)
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
        if points > 20000 and not extend_20k:
            extend_20k = True
            if lives < 3:
                lives += 1