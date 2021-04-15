from random import Random
import projectiles

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 740


def CircleSpawner(loc, div, kind, offset, bullets, sprites):
    bullet_counter = 0
    angle = 360 / div
    while bullet_counter < div:
        if kind == "w":
            new_bullet = projectiles.WarblyBullet(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s":
            new_bullet = projectiles.SpiralBullet(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s2":
            new_bullet = projectiles.SpiralBullet2(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s3":
            new_bullet = projectiles.SpiralBullet3(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s3i":
            new_bullet = projectiles.SpiralBullet3Inverse(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s4":
            new_bullet = projectiles.SpiralBullet4(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "s4i":
            new_bullet = projectiles.SpiralBullet4Inverse(loc.x, loc.y, bullet_counter * angle + offset)
        elif kind == "b2":
            new_bullet = projectiles.Bullet2(loc.x, loc.y, bullet_counter * angle + offset)
        else:
            new_bullet = projectiles.Bullet(loc.x, loc.y, bullet_counter * angle + offset)
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
                new_bullet = projectiles.WarblyBullet(space * bullet_counter, loc_y, angle)
            elif kind == "s":
                new_bullet = projectiles.SpiralBullet(space * bullet_counter, loc_y, angle)
            elif kind == "s2":
                new_bullet = projectiles.SpiralBullet2(space * bullet_counter, loc_y, angle)
            elif kind == "s3":
                new_bullet = projectiles.SpiralBullet3(space * bullet_counter, loc_y, angle)
            elif kind == "s3i":
                new_bullet = projectiles.SpiralBullet3Inverse(space * bullet_counter, loc_y, angle)
            elif kind == "s4":
                new_bullet = projectiles.SpiralBullet4(space * bullet_counter, loc_y, angle)
            elif kind == "s4i":
                new_bullet = projectiles.SpiralBullet4Inverse(space * bullet_counter, loc_y, angle)
            elif kind == "b2":
                new_bullet = projectiles.Bullet2(space * bullet_counter, loc_y, angle)
            else:
                new_bullet = projectiles.Bullet(space * bullet_counter, loc_y, angle)
            bullets.add(new_bullet)
            sprites.add(new_bullet)
        bullet_counter += 1


def QuarterSpawner(loc, div, kind, offset, bullets, sprites):
    bullet_counter = 0
    angle = 90 / div
    while bullet_counter < div:
        if kind == "w":
            new_bullet = projectiles.WarblyBullet(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s":
            new_bullet = projectiles.SpiralBullet(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s2":
            new_bullet = projectiles.SpiralBullet2(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s3":
            new_bullet = projectiles.SpiralBullet3(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s3i":
            new_bullet = projectiles.SpiralBullet3Inverse(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s4":
            new_bullet = projectiles.SpiralBullet4(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "s4i":
            new_bullet = projectiles.SpiralBullet4Inverse(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        elif kind == "b2":
            new_bullet = projectiles.Bullet2(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        else:
            new_bullet = projectiles.Bullet(loc.x, loc.y, bullet_counter * angle + 45 + offset)
        bullets.add(new_bullet)
        sprites.add(new_bullet)
        bullet_counter += 1


def Stream(loc, angle, kind, bullets, sprites):
    if kind == "w":
        new_bullet = projectiles.WarblyBullet(loc.x, loc.y, angle + 90)
    elif kind == "s":
        new_bullet = projectiles.SpiralBullet(loc.x, loc.y, angle + 90)
    elif kind == "s2":
        new_bullet = projectiles.SpiralBullet2(loc.x, loc.y, angle + 90)
    elif kind == "s3":
        new_bullet = projectiles.SpiralBullet3(loc.x, loc.y, angle + 90)
    elif kind == "s3i":
        new_bullet = projectiles.SpiralBullet3Inverse(loc.x, loc.y, angle + 90)
    elif kind == "s4":
        new_bullet = projectiles.SpiralBullet4(loc.x, loc.y, angle + 90)
    elif kind == "s4i":
        new_bullet = projectiles.SpiralBullet4Inverse(loc.x, loc.y, angle + 90)
    elif kind == "b2":
        new_bullet = projectiles.Bullet2(loc.x, loc.y, angle + 90)
    elif kind == "cr":
        new_bullet = projectiles.BulletCross(loc.x, loc.y, angle)
    elif kind == "ma":
        new_bullet = projectiles.BulletModA(loc.x, loc.y, angle)
    elif kind == "mb":
        new_bullet = projectiles.BulletModB(loc.x, loc.y, angle)
    elif kind == "bd":
        new_bullet = projectiles.BulletBarD(loc.x, loc.y, angle)
    else:
        new_bullet = projectiles.Bullet(loc.x, loc.y, angle + 90)
    bullets.add(new_bullet)
    sprites.add(new_bullet)


def Gatling(loc, div, dir, width, count, kind, bullets, sprites):
    pos = count % div
    angle = 0
    if dir == "right":
        angle = 0
        loc.y += (pos * width) - ((div * width) / 2)
    elif dir == "down":
        angle = 90
        loc.x += (pos * width) - ((div * width) / 2)
    elif dir == "left":
        angle = 180
        loc.y += (pos * width) - ((div * width) / 2)
    elif dir == "up":
        angle = 270
        loc.x += (pos * width) - ((div * width) / 2)
    if kind == "w":
        new_bullet = projectiles.WarblyBullet(loc.x, loc.y, angle)
    elif kind == "s":
        new_bullet = projectiles.SpiralBullet(loc.x, loc.y, angle)
    elif kind == "s2":
        new_bullet = projectiles.SpiralBullet2(loc.x, loc.y, angle)
    elif kind == "s3":
        new_bullet = projectiles.SpiralBullet3(loc.x, loc.y, angle)
    elif kind == "s3i":
        new_bullet = projectiles.SpiralBullet3Inverse(loc.x, loc.y, angle)
    elif kind == "s4":
        new_bullet = projectiles.SpiralBullet4(loc.x, loc.y, angle)
    elif kind == "s4i":
        new_bullet = projectiles.SpiralBullet4Inverse(loc.x, loc.y, angle)
    elif kind == "b2":
        new_bullet = projectiles.Bullet2(loc.x, loc.y, angle)
    else:
        new_bullet = projectiles.Bullet(loc.x, loc.y, angle)
    bullets.add(new_bullet)
    sprites.add(new_bullet)
