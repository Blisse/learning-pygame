#! /usr/bin/env python

import pygame, pygame.gfxdraw
import math

from datetime import datetime

dp_size = 640

screen = pygame.display.set_mode((dp_size,dp_size))
running = 1

middle = dp_size/2
midpoint = middle,middle

c = datetime.now()
ch = c.hour
cm = c.minute
cs = c.second

front_color = 224,224,224
back_color = 27,27,27
rim_color = 153,1,0

second_color = 255,153,0
minute_color = 153,5,4
hour_color = 50,153,187

second_length = 240
minute_length = 250
hour_length = 140



def update_current_time():
	dt_obj = datetime.now()
	nh = dt_obj.hour
	nm = dt_obj.minute
	ns = dt_obj.second
	return nh, nm, ns

def get_point_second(unit, length):
	unit = ( unit + 45 ) % 60
	deg = ( unit / 60.0 ) * 360.0
	rad = math.radians(deg)
	x = ( length * math.cos(rad) ) + middle
	y = ( length * math.sin(rad) ) + middle
	return x, y

def get_point_minute(unit, length):
	unit = ( unit + 45 ) % 60
	deg = ( unit / 60.0 ) * 360.0
	rad = math.radians(deg)
	x = ( length * math.cos(rad) ) + middle
	y = ( length * math.sin(rad) ) + middle
	return x, y

def get_point_hour(unit, subunit, length):
	unit = ( ( unit - 3.0 ) % 12 ) + subunit / 60.0
	deg = ( unit / 12.0 ) * 360.0
	rad = math.radians(deg)
	x = ( length * math.cos(rad) ) + middle
	y = ( length * math.sin(rad) ) + middle
	return x, y

def draw_second():
	s_point = get_point_second(cs, second_length)
 	pygame.draw.aaline(screen, second_color, midpoint, s_point)

def draw_minute():
	s_point = get_point_minute(cm, minute_length)
	sa_point = get_point_minute(cm+0.7, minute_length/3)
	sb_point = get_point_minute(cm-0.7, minute_length/3)
	pointlist = midpoint, sa_point, s_point, sb_point
 	pygame.gfxdraw.filled_polygon(screen, pointlist, minute_color)

def draw_hour():
	s_point = get_point_hour(ch, cm, hour_length)
	sa_point = get_point_hour(ch+0.1, cm, hour_length/2)
	sb_point = get_point_hour(ch-0.1, cm, hour_length/2)
	pointlist = midpoint, sa_point, s_point, sb_point
 	pygame.gfxdraw.filled_polygon(screen, pointlist, hour_color)

def draw_face():
	pygame.gfxdraw.filled_circle(screen, middle, middle, minute_length+2, rim_color)
	pygame.gfxdraw.filled_circle(screen, middle, middle, minute_length-2, front_color)

def draw_clock():
	draw_face()
	draw_second()
	draw_minute()
	draw_hour()

while running:
  event = pygame.event.poll()
  if event.type == pygame.QUIT:
    running = 0

  screen.fill( back_color )
  dt = datetime.now()
  if dt.second != cs:
    ch, cm, cs = update_current_time()
    print "{0:02d}, {1:02d}, {2:02d}".format(ch,cm,cs)
  draw_clock()

  pygame.display.flip()
