from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	if x0 > x1:
		x0, x1 = x1, x0
		y0, y1 = y1, y0
	x0 = int(x0)
	x1 = int(x1)
	y0 = int(y0)
	y1 = int(y1)
	dx = x1 - x0
	dy = y1 - y0
	if (dx == 0):
		y = y0
		x = x0
		while(y <= y1):
			plot(screen, color, x, y)
			y = y + 1
		return
	change = float(dy) / float(dx)
	if (dy == 0):
		x = x0
		y = y0
		while(x <= x1):
			plot(screen, color, x, y)
			x = x + 1
	elif (change) >= 1:
		d = dy - (2 * dx)
		x = x0
		y = y0
		while(y <= y1):
			plot(screen, color, x, y)
			if d < 0:
				x = x + 1
				d = d + (2 * dy)
			y = y + 1
			d = d - (2 * dx)
	elif (0 < (change) < 1):
		d = (2 * dy) - dx
		x = x0
		y = y0
		while(x <= x1):
			plot(screen, color, x, y)
			if d > 0:
				y = y + 1
				d = d - (2 * dx)
			x = x + 1
			d = d + (2 * dy)
	elif (-1 < (change) <= 0):
		d = (2 * dy) + dx
		x = x0
		y = y0
		while (x <= x1):
			plot(screen, color, x, y)
			if d < 0:
				y = y - 1
				d = d + (2 * dx)
			x = x + 1
			d = d + (2 * dy)
	else:
		d = dy + (2 * dx)
		x = x0
		y = y0
		while(y >= y1):
			plot(screen, color, x, y)
			if d > 0:
				x = x + 1
				d = d + (2 * dy)
			y = y - 1
			d = d + (2 * dx)
