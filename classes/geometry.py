#  File: geometry.py
#  Description: A geometry program for solving geometry problems
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/11/2015
#  Date Last Modified: 10/14/2015

import linecache
import math

#a point that represents an x and a y coordinate
class Point(object):

	def __init__(self,p1):
		self.x = p1[0]
		self.y = p1[1]

	def __str__(self):
		return("(%.1f,%.1f)" %(self.x,self.y))

	def dist(self,other):
		x1 = self.x
		x2 = other.x
		y1 = self.y
		y2 = other.y

		return(math.sqrt(((x2-x1)**2)+((y2-y1)**2)))

	def __eq__(self,other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

#a line that represents two points with x and y coordinates
class Line(object):

	def __init__(self,p1,p2):
		self.p1 = p1
		self.p2 = p2

	def __str__(self):
		if self.isHorizontal():
			return("y = %.1f" %self.p1.y)
		elif self.isVertical():
			return("x = %.1f" %self.p1.x)
		else:
			return("y = %.1fx + %.1f" %(self.slope(),self.yIntercept()))

	def slope(self):
		if self.p2.x == self.p1.x:
			return (float('inf'))
		else:
			return ((self.p2.y - self.p1.y)/(self.p2.x - self.p1.x))

	def isHorizontal(self):
		if is_equal(self.slope(),0):
			return(True)
		else:
			return(False)

	def isVertical(self):
		if self.slope() == float('inf'):
			return(True)
		else:
			return(False)

	def xIntercept(self):
		if self.isHorizontal():
			return(float('inf'))
		elif self.isVertical():
			return(self.p1.x)
		else:
			return(self.yIntercept()/self.slope())

	def yIntercept(self):
		if self.isVertical():
			return(float('inf'))
		elif self.isHorizontal():
			return(self.p1.y)
		else:
			return(self.p1.y-(self.slope()*self.p1.x))

	def isParallel(self,other):
		if is_equal(self.slope(),other.slope()):
			return(True)
		else:
			return(False)

	def isPerpendicular(self,other):
		if is_equal(self.slope()/other.slope(),-1):
			return True
		else:
			return False

	# def onLine(self):

	# use the formula |Am + Bn + C| / sqrt(A**2 + B**2) where the point is m,n
	#the line is Ax + By + C
	def perpDist(self,pt):
		C = self.yIntercept()
		A = self.slope()
		B = 1

		dist = abs(A*pt.x + B*pt.y + C) / math.sqrt(A**2 + B**2)
		return(dist)


	def intersectionPoint(self,other):
		new_line_eq1 = [(self.p1.y - self.p2.y), (self.p2.x - self.p1.x), (self.p1.x*self.p2.y - self.p2.x*self.p1.y)]
		new_line_eq2 = [(other.p1.y - other.p2.y), (other.p2.x - other.p1.x), (other.p1.x*other.p2.y - other.p2.x*other.p1.y)]

		D  = new_line_eq1[0] * new_line_eq2[1] - new_line_eq1[1] * new_line_eq2[0]
		Dx = new_line_eq1[2] * new_line_eq2[1] - new_line_eq1[1] * new_line_eq2[2]
		Dy = new_line_eq1[0] * new_line_eq2[2] - new_line_eq1[2] * new_line_eq2[0]
		if D != 0:
			x = Dx / D
			y = Dy / D
			return("(%.1f,%.1f)" %(x,y))
		else:
			return False

class Circle():

	def __init__(self,radius,p1):
		self.radius = radius
		self.center = Point(p1)

	def __str__(self):
		return("Circle: \n\tradius: %.1f \n\tcenter: (%.1f,%.1f)" %(self.radius,self.center.x,self.center.y))

	def circumference(self):
		return (2*math.pi*self.radius)

	def area(self):
		return (math.pi*self.radius**2)

	def containsPoint(self,pt):
		dist_squared = (self.center.x - pt.x)**2 + (self.center.y - pt.y)**2
		if dist_squared <= self.radius**2:
			return True
		else:
			return False

	#check the line has a point on the circle then check the perp distance is = radius
	def hasTangentLine(self,line):
		if is_equal(line.perpDist(self.center),self.radius):
			return(True)
		else:
			return(False)

#function to check equality with tolerance
def is_equal(num1,num2):
	tolerance = 1.0e-16
	return (abs (num1-num2) < tolerance)

#read geometry.txt file and return data for point (must specify line value when calling)
def getPoint(lineNum):
	return([ float(x) for x in linecache.getline('geometry.txt', lineNum).split() ])

#read geometry.txt file and return data for line (must specify line value when calling)
def getLine(lineNum):
	inputs = [ float(x) for x in linecache.getline('geometry.txt', lineNum).split() ]
	return([inputs[0],inputs[1]],[inputs[2],inputs[4]])

#read geometry.tx file and return data for circle (must specify line value when calling)
def getCircle(lineNum):
	inputs = [ float(x) for x in linecache.getline('geometry.txt', lineNum).split() ]
	radius = inputs[0]
	p1 = [inputs[1], inputs[2]]
	return([radius,p1])

def main():
	
	# read the coordinates of Point A
	# print Point A
	pA = Point(getPoint(1))
	print(pA)

	# read the coordinates of Point A
	# print Point A
	pB = Point(getPoint(2))
	print(pB)

	# print the distance between A and B
	print("The distance between %s and %s is %.1f" %(pA,pB,pA.dist(pB)))

	# create a line AB
	lineAB = Line(pA,pB)

	# print the slope of AB
	print("The slope of line %s is %.1f" %(lineAB,lineAB.slope()))

	# print the x-intercept of the line AB
	print("The x-intercept of line %s is %.1f" %(lineAB,lineAB.xIntercept()))

	# print the y-intercept of the line AB
	print("The y-intercept of line %s is %.1f" %(lineAB,lineAB.yIntercept()))

	# read the coordinates of Point C
	pC = Point(getPoint(3))

	# read the coordinates of Point D
	pD = Point(getPoint(4))

	# create a line CD
	lineCD = Line(pC,pD)

	# print the string representation of the line AB
	print(lineAB)

	# print the string representation of the line CD
	print(lineCD)

	# print if the lines AB and CD are parallel or not
	if lineAB.isParallel(lineCD):
		print("Lines are parallel")
	else:
		print("Lines are not parallel")

		# if they are not parallel, print the intersection point of AB and CD
		print("The intersection point is: " + lineAB.intersectionPoint(lineCD))

	# print if the lines AB and CD are perpendicular or not
	if lineAB.isPerpendicular(lineCD):
		print("These lines are perpendicular")
	else:
		print("These lines are not perpendicular")

	# read the radius of circle1 and the coordinates of its center
	circle_data = getCircle(5)
	circle1 = Circle(circle_data[0],circle_data[1])

	# read the radius of circle2 and the coordinates of its center
	circle_data = getCircle(6)
	circle2 = Circle(circle_data[0],circle_data[1])

	# print the string representations of circle1 and circle2
	print(circle1)
	print(circle2)

	# determine if point P is inside circle1
	pP = Point(getPoint(7))
	if circle1.containsPoint(pP):
		print("%s lies within the circle: \n%s" %(pP,circle1))
	else:
		print("%s does not lie within circle: \n%s" %(pP,circle1))

	# determine if point Q is inside circle1
	pQ = Point(getPoint(8))
	if circle1.containsPoint(pQ):
		print("%s lies within the circle: \n%s" %(pQ,circle1))
	else:
		print("%s does not lie within circle: \n%s" %(pQ,circle1))

	# print whether line CD is tangent to circle2
	if circle2.hasTangentLine(lineCD):
		print("%s is tangent to the circle: \n%s" %(lineCD,circle2))
	else:
		print("%s is not tangent to the circle: \n%s" %(lineCD,circle2))

	# close file "geometry.txt"

main()
