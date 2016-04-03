#  File: Nim.py
#  Description: An example of computing values for the nim-sum game
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 09/07/2015
#  Date Last Modified: 09/08/2015

def main():
	# open file nim.txt (in read only), which contains user input
	f = open('nim.txt', 'r')

	#read first line and assign it as the number of heaps to be computed
	nim_answers = int(f.readline().rstrip())

	#loop through the user input heaps one at a time
	for x in range(1, nim_answers+1):
		#read the next line in the file and split into a list of integers
		heap = [int(n) for n in f.readline().split()]

		#compute the nim-sum
		nim_sum = heap[0] ^ heap[1] ^ heap[2]

		#check the nim-sum value and ouput the pieces to remove and the state of the game
		if(nim_sum == 0):
			print("Heaps: %s %s %s : You lose" % (heap[0], heap[1], heap[2]))
		else:
			#calculate the number of pieces to remove from each heap
			#using the formula a - (a ^ nim-sum)
			if(heap[0] ^ nim_sum < heap[0]):
				p = heap[0]^nim_sum
				num_remove = heap[0] - p
				print("Heaps: %s %s %s : Remove %d from Heap 1" % (heap[0], heap[1], heap[2], num_remove))
			elif(heap[1] ^ nim_sum < heap[1]):
				p = heap[1]^nim_sum
				num_remove = heap[1] - p
				print("Heaps: %s %s %s : Remove %d from Heap 2" % (heap[0], heap[1], heap[2], num_remove))
			else:
				p = heap[2]^nim_sum
				num_remove = heap[2] - p
				print("Heaps: %s %s %s : Remove %d from Heap 3" % (heap[0], heap[1], heap[2], num_remove))
main()