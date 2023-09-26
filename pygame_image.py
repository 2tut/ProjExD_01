import sys
import pygame as pg
import math

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_flipped = pg.transform.flip(bg_img, True, False)

    fg_img = pg.image.load("ex01/fig/3.png")
    fg_img_flipped = pg.transform.flip(fg_img, True, False)
    fg_img_rotated = pg.transform.rotozoom(fg_img_flipped, 10, 1.0)

    fg_img_list = []
    fg_img_list_length = 50
    for i in range(fg_img_list_length):
        angle = 20*math.sin(math.pi*i/fg_img_list_length) - 5
        img = pg.transform.rotozoom(fg_img_rotated, angle, 1.0)
        fg_img_list.append(img)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        bg_x = tmr%3200

        screen.blit(bg_img, [-bg_x, 0])
        screen.blit(bg_img_flipped, [1600-bg_x, 0])
        screen.blit(bg_img, [3200-bg_x, 0])

        screen.blit(fg_img_list[tmr % len(fg_img_list)], [300, 200])
        pg.display.update()

        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
