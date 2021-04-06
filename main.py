import pygame
from pygame.locals import *
from pygame.math import Vector2
from random import Random
from time import time
from datetime import datetime, timedelta
import sys

# Define FPS
FPS = 60                            # Cap at 60 FPS

# Define screen dimensions
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740

# RGB color primitives
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FAST = 5
SLOW = 2.5

WRANGE = 6

vec = pygame.math.Vector2           # Defining simple reference to Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, spawn_x, spawn_y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [spawn_x, spawn_y]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, image, spawn_x, spawn_y, angle):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [spawn_x, spawn_y]

    def update(self):
        if self.rect.right < 0:
            self.kill()
        elif self.rect.left > SCREEN_WIDTH:
            self.kill()
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
        elif self.rect.top < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/player.png", spawn_x, spawn_y)
        self.pos = vec(self.rect.center)
        self.hitbox = Rect(1, 1, 2, 2)
        self.hitbox.center = self.rect.center
        self.acc = vec(0, 0)
        self.speed = FAST
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        pass

    def move(self):
        if self.up:
            self.acc.y = -self.speed
        elif self.down:
            self.acc.y = self.speed
        else:
            self.acc.y = 0
        if self.left:
            self.acc.x = -self.speed
        elif self.right:
            self.acc.x = self.speed
        else:
            self.acc.x = 0
        self.pos += self.acc

        if self.pos.x + 8 > SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH - 8
        if self.pos.x < 8:
            self.pos.x = 8
        if self.pos.y + 8 > SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT - 8
        if self.pos.y < 8:
            self.pos.y = 8

        self.rect.center = self.pos
        self.hitbox.center = self.pos


class Bullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/bullet.png", spawn_x, spawn_y, angle)
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


class WarblyBullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/bullet2.png", spawn_x, spawn_y, angle)
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        random_offset = vec((self.rand.randint(0, WRANGE) - (WRANGE / 2)),
                            (self.rand.randint(0, WRANGE) - (WRANGE / 2)))
        self.pos += self.velocity + random_offset
        self.rect.center = self.pos


def CircleSpawner(loc, div, kind, offset, bullets, sprites):
    bullet_counter = 0
    angle = 360 / div
    while bullet_counter < div:
        if kind == "w":
            new_bullet = WarblyBullet(loc.x, loc.y, bullet_counter * angle + offset)
        else:
            new_bullet = Bullet(loc.x, loc.y, bullet_counter * angle + offset)
        bullets.add(new_bullet)
        sprites.add(new_bullet)
        bullet_counter += 1


def main():
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)
    pygame.display.set_caption("bulletTest")

    font_color = WHITE
    font = pygame.font.Font("res/misc/Symtext.ttf", 24)

    sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()

    player = Player(256, 660)
    sprites.add(player)
    players.add(player)

    best_time = time() - time()
    current_time = time() - time()

    frame_counter = 0
    round = 0

    start_time = time()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle window exit gracefully
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.up = True
                if event.key == pygame.K_DOWN:
                    player.down = True
                if event.key == pygame.K_LEFT:
                    player.left = True
                if event.key == pygame.K_RIGHT:
                    player.right = True
                if event.key == pygame.K_LSHIFT:
                    player.speed = SLOW
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.up = False
                if event.key == pygame.K_DOWN:
                    player.down = False
                if event.key == pygame.K_LEFT:
                    player.left = False
                if event.key == pygame.K_RIGHT:
                    player.right = False
                if event.key == pygame.K_LSHIFT:
                    player.speed = FAST

        if frame_counter % 30 == 0:         # and frame counter < 150
            round += 1
            CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), round, "b", round*10, bullets, sprites)
        if frame_counter % 100 == 0:
            CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), round / 2, "w", 0, bullets, sprites)
        if frame_counter == 300:
            frame_counter = 0

        #if frame_counter % 30 == 0:
        #    round += 1
        #    CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), round * 10, "w", 0, bullets, sprites)

        player.move()

        for bullet in bullets:
            player_hit = player.hitbox.colliderect(bullet)
            if player_hit:
                player.kill()
                for obj in bullets:
                    obj.kill()
                if current_time - start_time > best_time:
                    best_time = current_time - start_time
                current_time = time() - time()
                start_time = time()
                round -= (round - 1)
                player = Player(256, 660)
                sprites.add(player)
                players.add(player)

        screen.fill(BLACK)
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

    pygame.display.quit()                           # More graceful exit handling
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()