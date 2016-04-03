#  File: Turtle.py
#  Description: A program using the turtle graphics package to draw graphs
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 09/13/2015
#  Date Last Modified: 09/16/2015

import turtle
import math

def main():

	#define screen size
	turtle.setup(width=900, height=900, startx=0, starty=0)
	turtle.title("CS 313E Assignment 2")

	#create turtle from Turtle class
	ttl = turtle.Turtle()
	ttl.speed(30)

	#define grid size and interval
	x_min = -400
	x_max = 400
	y_min = -400
	y_max = 400
	grid_interval = 100
	step_size = 0.01

	#define functions

	#draw grid
	ttl.pu()
	ttl.goto(-400,0)
	ttl.pd()
	ttl.forward(800)
	ttl.pu()
	ttl.goto(0,-400)
	ttl.left(90)
	ttl.pd()
	ttl.forward(800)

	#draw x-axis tickmarks
	for i in range(int((x_max-x_min)/grid_interval)+1):
		new_x = x_min + (grid_interval*i)
		interval_value = (x_min/grid_interval) + (1*i)
		ttl.pu()
		ttl.goto((new_x-10),-30)
		ttl.pd()
		ttl.write(interval_value, font=("Arial", 20, "normal"))
		ttl.pu()
		ttl.goto(new_x,-5)
		ttl.pd()
		ttl.goto(new_x,5)

	#draw y-axis tickmarks
	for i in range(int((y_max-y_min)/grid_interval)+1):
		new_y = y_min + (grid_interval*i)
		interval_value = (y_min/grid_interval) + (1*i)
		ttl.pu()
		ttl.goto(-50,(new_y-10))
		ttl.pd()
		ttl.write(interval_value, font=("Arial", 20, "normal"))
		ttl.pu()
		ttl.goto(-5,new_y)
		ttl.pd()
		ttl.goto(5,new_y)

	#function start, stop
	x_start = (math.pi)*-1
	x_stop = (math.pi)

	#change color and go to starting point of sin function
	ttl.pu()
	ttl.pencolor("red")
	x = x_start
	y = math.sin(x)
	ttl.goto(x*grid_interval,y*grid_interval)
	ttl.pd()

	#draw function
	while x <= x_stop:
		x += step_size
		y = math.sin(x)
		ttl.goto(x*grid_interval,y*grid_interval)

	#change color and go to starting point of cos function
	ttl.pu()
	ttl.pencolor("blue")
	x = x_start
	y = math.cos(x)
	ttl.goto(x*grid_interval,y*grid_interval)
	ttl.pd()

	#draw function
	while x <= x_stop:
		x += step_size
		y = math.cos(x)
		ttl.goto(x*grid_interval,y*grid_interval)

	#change color and go to starting point of polynomial function x2 - 4
	ttl.pu()
	ttl.pencolor("green")
	x = x_start
	y = x*x - 4
	ttl.goto(x*grid_interval,y*grid_interval)
	ttl.pd()

	#draw function
	while x <= x_stop:
		x += step_size
		y = x*x - 4
		ttl.goto(x*grid_interval,y*grid_interval)

	#change color and go to starting point of exponential function
	ttl.pu()
	ttl.pencolor("purple")
	x = x_start
	y = math.exp(x)
	ttl.goto(x*grid_interval,y*grid_interval)
	ttl.pd()

	#draw function
	while x <= x_stop:
		x += step_size
		y = math.exp(x)
		ttl.goto(x*grid_interval,y*grid_interval)

main()
