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
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/player_c.png", spawn_x, spawn_y)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/player1_collide.png"))
        self.pos = vec(self.rect.center)
        self.acc = vec(0, 0)
        self.speed = FAST
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def update(self):
        if self.left:
            self.image = pygame.image.load("res/img/player_l.png")
        elif self.right:
            self.image = pygame.image.load("res/img/player_r.png")
        else:
            self.image = pygame.image.load("res/img/player_c.png")
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


class Bullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


class Bullet2(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos


class WarblyBullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/warbly_bullet2.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.rand = Random()

    def update(self):
        random_offset = vec((self.rand.randint(0, WRANGE) - (WRANGE / 2)),
                            (self.rand.randint(0, WRANGE) - (WRANGE / 2)))
        self.pos += self.velocity + random_offset
        self.rect.center = self.pos


class SpiralBullet(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 2
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 5
        self.frequency = 10
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet2(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = 15
        self.frequency = 50
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class SpiralBullet3(BulletSprite):
    def __init__(self, spawn_x, spawn_y, angle):
        super().__init__("res/img/big_spiral_bullet.png", spawn_x, spawn_y, angle)
        self.mask = pygame.mask.from_surface(pygame.image.load("res/img/big_bullet_collide.png"))
        self.velocity = Vector2(1, 0).rotate(angle) * 1.5
        self.pos = Vector2(self.rect.center)
        self.angle = angle
        self.amplitude = -30
        self.frequency = 50
        self.ticker = 0

    def update(self):
        self.ticker += 1
        if self.ticker % self.frequency == 0:
            self.angle += self.amplitude
            self.velocity = Vector2(1, 0).rotate(self.angle) * 2
        self.pos += self.velocity
        self.rect.center = self.pos


class BossOne(Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/yukari.png", spawn_x, spawn_y)
        self.pos = vec(self.rect.center)

    def update(self):
        self.rect.center = self.pos


class MagicCircle(Sprite):
    def __init__(self, spawn_x, spawn_y):
        super().__init__("res/img/magic_circle.png", spawn_x, spawn_y)
        self.pos = vec(self.rect.center)
        self.og_rect = self.rect
        self.frame = 0

    def update(self):
       # if self.frame == -3600:
       #     self.frame = 0
       # self.frame += 1
       # if self.frame % 10 == 0:
       #     self.image = pygame.transform.rotate(self.image, self.frame)
       #     self.rect = self.image.get_rect()
        self.rect.center = self.pos


def CircleSpawner(loc, div, kind, offset, bullets, sprites):
    bullet_counter = 0
    angle = 360 / div
    while bullet_counter < div:
        if kind == "w":
            new_bullet = WarblyBullet(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s":
            new_bullet = SpiralBullet(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s2":
            new_bullet = SpiralBullet2(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s3":
            new_bullet = SpiralBullet3(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "b2":
            new_bullet = Bullet2(loc.x, loc.y, bullet_counter * angle + offset)
        else:
            new_bullet = Bullet(loc.x, loc.y, bullet_counter * angle + offset)
        bullets.add(new_bullet)
        sprites.add(new_bullet)
        bullet_counter += 1


def BarSpawner(loc_y, div, angle, kind, bullets, sprites):
    bullet_counter = 0
    space = SCREEN_WIDTH / div
    rand = Random()
    range = int(round(div / 8))
    bound = rand.randint(0, div - range)

    while bullet_counter < div:
        if bullet_counter < bound or bullet_counter > bound + range:
            if kind == "w":
                new_bullet = WarblyBullet(space * bullet_counter, loc_y, angle)
            elif kind == "s":
                new_bullet = SpiralBullet(space * bullet_counter, loc_y, angle)
            elif kind == "s2":
                new_bullet = SpiralBullet2(space * bullet_counter, loc_y, angle)
            elif kind == "s3":
                new_bullet = SpiralBullet3(space * bullet_counter, loc_y, angle)
            elif kind == "b2":
                new_bullet = Bullet2(space * bullet_counter, loc_y, angle)
            else:
                new_bullet = Bullet(space * bullet_counter, loc_y, angle)
            bullets.add(new_bullet)
            sprites.add(new_bullet)
        bullet_counter += 1


def main():
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     pygame.HWSURFACE | pygame.DOUBLEBUF, vsync=1)
    pygame.display.set_caption("Touhou: Destitute Dreamscape (alpha demo)")

    font_color = WHITE
    font = pygame.font.Font("res/misc/Symtext.ttf", 24)

    background = pygame.image.load("res/img/background6.png")

    sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    players = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    circles = pygame.sprite.Group()

    player = Player(256, 660)
    sprites.add(player)
    players.add(player)

    magic_circle = MagicCircle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    sprites.add(magic_circle)
    circles.add(magic_circle)

    boss_one = BossOne(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    sprites.add(boss_one)
    bosses.add(boss_one)

    best_time = time() - time()
    current_time = time() - time()

    start_time = time()

    rand = Random()

    phase_counter = 0
    frame_counter = 0
    ticker = 0

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

        if phase_counter < 1800:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 3:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 3:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

    # phase one
        if phase_counter <= 1800:
            if frame_counter % 25 == 0:
                if ticker < 20:
                    ticker += 1
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker, "b", ticker * 10, bullets, sprites)
            if frame_counter % 100 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker / 2, "w", 0, bullets, sprites)
            if frame_counter % 245 == 0 or frame_counter % 250 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker * 2, "s", ticker, bullets, sprites)
            if frame_counter == 500:
                frame_counter = 0

        if 1800 < phase_counter < 1980:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 4:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 4:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

    # phase two
        if 1980 <= phase_counter <= 3780:
            if frame_counter % 30 == 0:
                if ticker < 30:
                    ticker += 2
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                              3, "b", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 60 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4),
                              2, "s", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 120 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4), ticker * 2, "w", 0, bullets, sprites)
            if frame_counter == 480:
                frame_counter = 0

        if 3780 < phase_counter < 3960:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 3:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 3:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

    # phase three
        if 3960 <= phase_counter <= 4760:
            if frame_counter % 30 == 0:
                if ticker < 30:
                    ticker += 1
                #if ticker < 50:
                #    ticker += 2
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker, "s2", ticker * 10, bullets, sprites)
            if frame_counter % 100 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3), ticker / 5, "s3", ticker * 2, bullets, sprites)
            if frame_counter % 300 == 0:
                BarSpawner(32, 20, 90, "b2", bullets, sprites)
            if frame_counter == 600:
                frame_counter = 0

        if 4760 < phase_counter < 4940:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 8:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 8:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

    # phase four
        if 4940 <= phase_counter <= 6740:
            if frame_counter % 60 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 8),
                              50, "b", rand.randint(45, 135), bullets, sprites)
            if frame_counter % 200 == 0:
                BarSpawner(SCREEN_HEIGHT / 8, 20, 90, "w", bullets, sprites)
            if frame_counter % 300 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                              25, "s", rand.randint(0, 360), bullets, sprites)
            if frame_counter == 600 == 0:
                frame_counter = 0

        if 6740 < phase_counter < 6800:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 10):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 10:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 10:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

    # phase four and a half
        if 6800 <= phase_counter <= 7020:
            if frame_counter % 10 == 0:
                BarSpawner(32, 10, rand.randint(45, 135), "b2", bullets, sprites)
            if frame_counter == 60:
                frame_counter = 0

        if 7020 < phase_counter < 7200:
            if boss_one.pos != vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2):
                if boss_one.pos.x < SCREEN_WIDTH / 2:
                    boss_one.pos.x += 1
                elif boss_one.pos.x > SCREEN_WIDTH / 2:
                    boss_one.pos.x -= 1
                if boss_one.pos.y < SCREEN_HEIGHT / 2:
                    boss_one.pos.y += 1
                elif boss_one.pos.y > SCREEN_HEIGHT / 2:
                    boss_one.pos.y -= 1
                magic_circle.pos = boss_one.pos

        if phase_counter == 7199:
            for bullet in bullets:
                bullet.kill()

    # phase five
        if 7200 <= phase_counter <= 9000:
            if frame_counter % 30 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                              5, "b2", rand.randint(45, 135), bullets, sprites)
            if frame_counter % 90 == 0:
                CircleSpawner(vec(SCREEN_WIDTH / 2, 8),
                              40, "s3", rand.randint(0, 360), bullets, sprites)
            if frame_counter % 120 == 0:
                BarSpawner(SCREEN_HEIGHT - 8, 30, 270, "b", bullets, sprites)

        player.move()

        for bullet in bullets:
            player_hit = pygame.sprite.collide_mask(player, bullet)
            if player_hit:
                player.kill()
                for obj in bullets:
                    obj.kill()
                if current_time - start_time > best_time:
                    best_time = current_time - start_time
                current_time = time() - time()
                start_time = time()
                frame_counter = 0
                phase_counter = 0
                ticker = 0
                player = Player(256, 660)
                sprites.add(player)
                players.add(player)
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

    pygame.display.quit()                           # More graceful exit handling
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()