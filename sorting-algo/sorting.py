#  File: sorting.py
#  Description: A program using the various sort methods to check the speed of each under certain conditions
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 11/29/2015
#  Date Last Modified: 12/03/2015

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1,fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp

def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue

def shellSort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapInsertionSort(alist,startposition,sublistcount)
		sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):
		currentvalue = alist[i]
		position = i

		while position>=gap and alist[position-gap]>currentvalue:
			alist[position] = alist[position-gap]
			position = position - gap

		alist[position] = currentvalue

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
				k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
	if first < last:
		splitpoint = partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
	pivotvalue = alist[first]
	leftmark = first + 1
	rightmark = last
	done = False

	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark += 1

		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark -= 1

		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark

def doTest(iterations, myLists):
	
	#bubble test
	bubbleSortAvgs = []

	#iterate through various length lists
	for n in myLists:		
		average = 0	

		#itereate through number of iterations
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			bubbleSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime

			#calculate average at iteration 5
			if i == 5:
				average = average/5
				bubbleSortAvgs.append(average)

	print ("       bubbleSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(bubbleSortAvgs[0], bubbleSortAvgs[1], bubbleSortAvgs[2]))

	#selection test
	selectionSortAvgs = []
	for n in myLists:
		average = 0
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			selectionSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime
			if i == 5:
				average = average/5
				selectionSortAvgs.append(average)

	print ("    SelectionSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(selectionSortAvgs[0], selectionSortAvgs[1], selectionSortAvgs[2]))
	
	#insertion test
	insertionSortAvgs = []
	for n in myLists:
		average = 0
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			insertionSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime
			if i == 5:
				average = average/5
				insertionSortAvgs.append(average)

	print ("    InsertionSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(insertionSortAvgs[0], insertionSortAvgs[1], insertionSortAvgs[2]))

	#shell test
	shellSortAvgs = []
	for n in myLists:
		average = 0
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			shellSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime
			if i == 5:
				average = average/5
				shellSortAvgs.append(average)

	print ("        ShellSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(shellSortAvgs[0], shellSortAvgs[1], shellSortAvgs[2]))

	#merge test
	mergeSortAvgs = []
	for n in myLists:
		average = 0
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			mergeSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime
			if i == 5:
				average = average/5
				mergeSortAvgs.append(average)

	print ("        MergeSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(mergeSortAvgs[0], mergeSortAvgs[1], mergeSortAvgs[2]))

	#quick test
	quickSortAvgs = []
	for n in myLists:
		average = 0
		for i in range(1, iterations+1):
			startTime = time.perf_counter()
			quickSort(n)
			endTime = time.perf_counter()
			elapsedTime = endTime - startTime
			average += elapsedTime
			if i == 5:
				average = average/5
				quickSortAvgs.append(average)

	print ("        QuickSort     {0:0.6f}    {1:0.6f}    {2:0.6f}".format(quickSortAvgs[0], quickSortAvgs[1], quickSortAvgs[2]))

def main():

#determine size of digit string
	n = [10,100,1000]
	myLists = []
	orderedLists = []
	iterations = 5
	numbTests = 6

	#create a list to randomize
	for i in n:
		nList = [x for x in range(i)]
		myLists.append(nList)

	# Create a random list from the sorted list 
	randList = []
	for n in myLists:
		random.shuffle(n)
		randList.append(n)


	# Setup header for Random results
	print("\nInput type = Random")
	print("                      avg time    avg time   avg time")
	print("      Sort function    (n=10)      (n=100)   (n=1000)")
	print("-----------------------------------------------------")
	doTest(iterations,randList)

	#Make an ordered list for tests
	o = [10,100,1000]

	for i in o:
		oList = [x for x in range(i)]
		orderedLists.append(oList)

	# Setup header for Sorted results
	print("\nInput type = Sorted")
	print("                      avg time    avg time   avg time")
	print("      Sort function    (n=10)      (n=100)   (n=1000)")
	print("-----------------------------------------------------")
	doTest(iterations,myLists)

	#reverse ordered list
	reverseList = []
	for n in orderedLists:
		n.reverse()
		reverseList.append(n)

	# Setup header for Reverse results
	print("\nInput type = Reverse")
	print("                      avg time    avg time   avg time")
	print("      Sort function    (n=10)      (n=100)   (n=1000)")
	print("-----------------------------------------------------")
	doTest(iterations,reverseList)

main()


