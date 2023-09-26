import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    fg_img = pg.image.load("ex01/fig/3.png")
    fg_img = pg.transform.flip(fg_img, True, False)
    fg_img_rotated = pg.transform.rotate(fg_img, 10)
    fg_img_list = [fg_img, fg_img_rotated]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])

        screen.blit(fg_img_list[tmr % len(fg_img_list)], [tmr%1600, 200])
        pg.display.update()

        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
