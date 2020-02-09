from display import *
from draw import *

s = new_screen()
l = 1
xs = 150
ys = 350
iterator = 0
c = [0, 0, 0]
up = True
cc = 10
while (l <= 300):
    if up:
        if c[0] <= 255:
            c[0] = c[0] + cc % 255
        elif c[1] <= 255:
            c[1] = c[1] + cc % 255
        elif c[2] <= 255:
            c[2] = c[2] + cc % 255
        else:
            up = False
    else:
        if c[0] > 0:
            c[0] = c[0] - cc
            if (c[0] < 0): c[0] = 0
        elif c[1] > 0:
            c[1] = c[1] - cc
            if (c[1] < 0): c[1] = 0
        elif c[2] > 0:
            c[2] = c[2] - cc
            if (c[2] < 0): c[2] = 0
        else:
            up = True
    if (iterator % 4 == 0):
        xn = xs + l
        yn = ys + l
    elif (iterator % 4 == 1):
        xn = xs - l
        yn = ys + l
    elif (iterator % 4 == 2):
        xn = xs - l
        yn = ys - l
    elif (iterator % 4 == 3):
        xn = xs + l
        yn = ys - l
    iterator = iterator + 1
    draw_line(xs, ys, xn, yn, s, c)
    xs = xn
    ys = yn
    l = l + (iterator % 4)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
