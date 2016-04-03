#  File: ERsim.py
#  Description: A program that manages an emergency room queue
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/24/2015
#  Date Last Modified: 10/29/2015

#class representing the queue abstract data type using lists
class Queue(object):

	def __init__(self):
		self.items = []

	def enqueue(self,item):
		return self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def showQueue(self):
		return(self.items)

#defined to read in ERsim.txt input file
def getLine(f):
	er_input = f.readline().split()
	return(er_input)

#adds a patient to specified priority queue
def addPatient(patient,critical,serious,fair):
	if patient[1] == 'Critical':
		critical.enqueue(patient[0])
	elif patient[1] == 'Serious':
		serious.enqueue(patient[0])
	elif patient[1] == 'Fair':
		fair.enqueue(patient[0])
	print('Add patient %s to %s queue' %(patient[0],patient[1]))
	
	print('Queues are: \nCritical: %s \nSerious: %s \nFair: %s\n' %(critical.showQueue(),serious.showQueue(),fair.showQueue()))

#function for treating the next patient or all patients in the line depending on priority
def treatPatient(command,critical,serious,fair):
	#define whether to treat all or only next patients by assigning number of loop iterations
	i = 0
	if command[0] == 'next':
		print("Treat next patient")
		numPatients = 1
	else:
		print("Treat all patients")
		numPatients = critical.size() + serious.size() + fair.size()

	#while loop to treat patients according to priority critical, serious, fair
	while i < numPatients:
		if critical.isEmpty():
			if serious.isEmpty():
				if fair.isEmpty():
					print("No patients in queues\n")
					break
				else:
					print("\nTreating %s from Fair queue" %fair.dequeue())
			else:
				print("\nTreating %s from Serious queue" %serious.dequeue())
		else:
			print("\nTreating %s from Critical queue" %critical.dequeue())
		i += 1

		if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
			print ('Queues are empty\n')
		else:
			print('Queues are: \nCritical: %s \nSerious: %s \nFair: %s\n' %(critical.showQueue(),serious.showQueue(),fair.showQueue()))

#function that will open the ERsim.txt file, set the priority queues
#and begin treating and adding patients
def runER():
	f = open('ERsim.txt', 'r')
	critical = Queue()
	serious = Queue()
	fair = Queue()

	#while loop to follow ERsim.txt instructions until 'exit'
	while True:
		nextStep = getLine(f)
		if nextStep[0] == 'exit':
			print('Exit')
			break
		if nextStep[0] == 'add':
			addPatient(nextStep[1:],critical,serious,fair)
		if nextStep[0] == 'treat':
			treatPatient(nextStep[1:],critical,serious,fair)


def main():

	#run the ER simulation
	runER()

main()