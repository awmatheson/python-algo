#  File: waterjug.py
#  Description: A program that will solve a general water jug problem
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/04/2015
#  Date Last Modified: 10/09/2015


#Define State class to be maintained throughout the program
class State(object):
	def __init__(self,jugs,steps,history):
		#state variables
		self.jugs = jugs
		self.steps = steps
		self.history = history

	def __eq__(self,other):
		self.jugs == other

	#method that will scan jugs to see if we have found the goal volume in the goal jug
	def is_goal(self, endJugs):
		endVol = endJugs[1]
		endJug = endJugs[0]

		if(self.jugs[endJug - 1] == endVol):
			return True
		else:
			return False

	#successors method that will return a list of all the possible successor jugs
	def successors(self,jugSize):
		newSuccessors = []

		#for loop to make new fill combinations
		for i in range(len(self.jugs)):
			if self.jugs[i] == 0:
				new_jug = [x for x in self.jugs]
				new_jug[i] = jugSize[i]
				newSuccessors.append(new_jug)

		#for loop to empty jugs if possible
		for i in range(len(self.jugs)):
			if self.jugs[i] != 0:
				new_jug = [x for x in self.jugs]
				new_jug[i] = 0
				newSuccessors.append(new_jug)

		#for loop to empty jugs into neighbour jugs if possible
		for i in range(len(self.jugs)):
			for j in range(1,len(self.jugs)):
				new_jug = [x for x in self.jugs]
				if self.jugs[i] != 0:
					if self.jugs[j] == 0:
						capacity = min(new_jug[i], jugSize[j])
						if capacity == new_jug[i]:
							new_jug[i] = 0
							new_jug[j] = self.jugs[i]
						else:
							new_jug[i] = new_jug[i] - jugSize[j]
							new_jug[j] = jugSize[j]
					newSuccessors.append(new_jug)


					if self.jugs[j] != 0 and self.jugs[j] != jugSize[j]:
						capacity = min(jugSize[j] - new_jug[j], new_jug[i])
						if capacity == jugSize[j] - new_jug[j]:
							new_jug[i] = new_jug[i] - (jugSize[j] - new_jug[j])
							new_jug[j] = jugSize[j]
						else:
							new_jug[i] = 0
							new_jug[j] = jugSize[j]
					newSuccessors.append(new_jug)
					
		return newSuccessors

#function that will recursively look for the goal 
#and if not will continue finding new states
def doWaterJug(successorStateList,knownSuccessorsList,successorList,currentState,jugSize,endJugs):
	#determine new state data based on current state
	newSteps = currentState.steps + 1

	#define new successors list, which we will 
	#populate and feed back into doWaterJug
	newSuccessorsList = []

	#check for goal state and then print history and final jugs
	for state in successorStateList:
		if state.is_goal(endJugs):
			for i in range(len(state.history)):
				print(state.history[i])
			print(state.jugs)
			return()
		else:
			newSuccessors = state.successors(jugSize)

			#define the history of the recursive algorithm
			algo_history = state.jugs
	
		#check for duplicates and append only non duplicate successors
		for i in range(len(newSuccessors)):
			if newSuccessors[i] not in knownSuccessorsList:
				knownSuccessorsList.append(newSuccessors[i])

				currentState.history.append(newSuccessors[i])
				successorStateList.append(State(newSuccessors[i],newSteps,currentState.history))
	doWaterJug(successorStateList,knownSuccessorsList,newSuccessors,state,jugSize,endJugs)


def main():
	#get data from jugdata.txt
	f = open('jugdata.txt', 'r')
	jugSize = [ int(x) for x in f.readline().split() ]
	endJugs = [ int(x) for x in f.readline().split() ]
	
	#define the initial state
	startState = State([0]*len(jugSize),0,[])

	#check for goal state in initial state
	if startState.is_goal(endJugs):
		print("success")
	else:
		#find initial successors with successor method
		successorList = startState.successors(jugSize)

		#start state maintaining list and successor list to remove duplicates
		knownSuccessorsList = [startState.jugs]
		successorStateList = [startState]

		#call water jug function to start search
		doWaterJug(successorStateList,knownSuccessorsList,successorList,startState,jugSize,endJugs)


main()
