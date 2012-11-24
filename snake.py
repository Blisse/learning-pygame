#! /usr/bin/env python

import pygame, pygame.gfxdraw
import math

import random
import time

from datetime import datetime


hi = 0.025
lo = 0.1
med = 0.05
speed = hi

dp_size = 640
pix_dens = 4
num_grid = dp_size/pix_dens


direction = [1,0]

x_index = [ x for x in range(0,dp_size,pix_dens) ]
y_index = [ y for y in range(0,dp_size,pix_dens) ]

screen = pygame.display.set_mode((dp_size,dp_size))

middle = dp_size/2
midpoint = middle,middle

c = datetime.now()
ch = c.hour
cm = c.minute
cs = c.second

front_color = 224,224,224
grid_color = 190, 190, 190
back_color = 27,27,27
rim_color = 153,1,0

food = [num_grid/2,num_grid/2]
eaten = pix_dens*4


boundaries = []

snake_color = 255,153,0
food_color = 50,153,224

s = num_grid/2 + 8
snake = [[s,s],[s,s+1],[s,s+2],[s,s+3]]

def valid_dir(x,y):
	global direction
	if x == 0 and y == -1:
		if direction == [0,1]:
			return
		direction[0] = 0
		direction[1] = -1
	elif x == 0 and y == 1:
		if direction == [0,-1]:
			return
		direction[0] = 0
		direction[1] = 1
	elif x == 1 and y == 0:
		if direction == [-1,0]:
			return
		direction[0] = 1
		direction[1] = 0
	elif x == -1 and y == 0:
		if direction == [1,0]:
			return
		direction[0] = -1
		direction[1] = 0

def move_worm():
	global snake, speed, eaten
	head = [snake[0][0],snake[0][1]]
	head[0] = (head[0] - direction[0]) % (num_grid-1)
	head[1] = (head[1] - direction[1]) % (num_grid-1)

	if (head == food):
		random_food()
		speed = speed * 0.90
		eaten -= 1
	else:
		snake = snake[:-1]
	snake.insert(0,head)

def worm_event(evt):
	if evt.key == pygame.K_UP:
		valid_dir(0,1)
	elif evt.key == pygame.K_DOWN:
		valid_dir(0,-1)
	elif evt.key == pygame.K_LEFT:
		valid_dir(1,0)
	elif evt.key == pygame.K_RIGHT:
		valid_dir(-1,0)
	move_worm()

def random_food():
	global food
	x = random.randrange(0,(num_grid-1))
	y = random.randrange(0,(num_grid-1))
	food = [x,y]

def update_current_time():
	dt_obj = datetime.now()
	nh = dt_obj.hour
	nm = dt_obj.minute
	ns = dt_obj.second
	return nh, nm, ns

def draw_grid():
	for x in range(0,dp_size,pix_dens):
		pygame.gfxdraw.hline(screen, 0, 640, x, grid_color)
		# pygame.gfxdraw.hline(surface, x1, x2, y, color):
		pygame.gfxdraw.vline(screen, x, 0, 640, grid_color)
		# pgyame.gfxdraw.vline(surface, x, y1, y2, color): return None

def draw_block(x,y,color):
	point1 = x_index[x], y_index[y]
	point2 = x_index[x+1], y_index[y]
	point3 = x_index[x+1], y_index[y+1]
	point4 = x_index[x], y_index[y+1]
	point_list = point1, point2, point3, point4
	pygame.gfxdraw.filled_polygon(screen, point_list, color)
	# pgyame.gfxdraw.filled_polygon(surface, points, color): return None

def draw_snake():
	for s in snake:
		draw_block(s[0],s[1],snake_color)

def draw_food():
	f = food
	draw_block(f[0],f[1],food_color)

def draw_game():
	#draw_grid()
	draw_snake()
	draw_food()

running = True

start = time.time()

while running:
  screen.fill( back_color )
  dt = datetime.now()
  if dt.second != cs:
  	ch, cm, cs = update_current_time()

  draw_game()

  for event in pygame.event.get():
	if event.type == pygame.QUIT:
	  running = False
	elif event.type == pygame.KEYDOWN:
	  worm_event(event)

  if time.time() - start > speed:
  	start = time.time()
  	move_worm()


  if eaten == 0:
  	quit
  pygame.display.flip()
