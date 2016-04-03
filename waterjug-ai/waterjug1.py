#  File: waterjug.py
#  Description: A program that will solve a general water jug problem
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/04/2015
#  Date Last Modified: 10/

#Define State class to be maintained throughout the program
class State(object):
	def __init__(self,jugs,steps,history):
		#state variables
		self.jugs = [0] * len(jugSize)
		self.steps = 0
		self.history = 0

	def __eq__(self,other):
		self.jugs == other

def is_goal(self):
	endVol = self.endJugs[1]
	endJug = self.endJugs[0]

	if(self.[endJug - 1] == endVol):
		return True
	else:
		return False

def successors(state):
	newSuccessors = []

	for jugs in self.jugs:
		newSuccessors.append(fill_jug(jugs))

	print(newSuccessors)
	def fill_jug(jugs):
	for i in range(len(jugs)):
		if jug[i] == 0
			jugs[i] = theState.jugSize[i]
			return jugs

	def empty_jug(jugs):
		if jugs[0] != 0:
			jugs[0] = 0
			return jugs
		else:
			empty_jug(jugs[1:])

	def transfer_jug(jugs,jugSize):


def doWaterJug(successorList):
	#check if any states in successorList are goal states
	if is_goal(successorList):
		print("done")
	else:
		newSuccessorList = []


def main():
		#get data from jugdata.txt
	f = open('jugdata.txt', 'r')
	jugSize = [ int(x) for x in f.readline().split() ]
	endJugs = [ int(x) for x in f.readline().split() ]
		
	startState = State(0*len(jugSize),0,0*len(jugSize))

	if startState.is_goal():
		print("success")
	else:
		successorList = successors(state.jugs)
		theState.steps = 1
		doWaterJug(successorList)

main()
