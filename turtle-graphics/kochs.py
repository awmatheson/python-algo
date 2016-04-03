#koch triangle with turtle

import turtle
import math

# def koch(t, order, size):
# 	if(order == 0):
# 		t.forward(size)
# 	else:
# 		for angle in [60, -120, 60, 0]:
# 			koch(t, order-1, size/3)
# 			t.left(angle)

def main():
	t = turtle.Turtle()

	# koch(t,3,300)
	t.forward(200)
	t.right(90)
	t.forward(200)

main()