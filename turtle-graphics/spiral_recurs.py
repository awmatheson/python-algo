
import turtle

t = turtle.Turtle()

my_win = turtle.Screen()

def draw_spiral(t, line_len):
	if line_len > 0:
		t.forward(line_len)
		t.right(90)
		draw_spiral(t, line_len - 5)


def tree(branch_len, t):
	if branch_len > 5:
		t.forward(branch_len)
		t.right(20)
		tree(branch_len - 15, t)
		t.left(40)
		tree(branch_len - 15, t)
		t.right(20)
		t.backward(branch_len)


t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")

tree(75, t)


# draw_spiral(t, 100)

my_win.exitonclick()