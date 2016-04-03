import time

def main():

	def find_min(myList):
		start_time = time.time()
		for i in myList:
			min_value = i
			if i < min_value:
				min_value = i

		end_time = time.time()
		return min_value, end_time - start_time

	def find_min_2(myList):
		start_time = time.time()
		for i in range(len(myList)):
			for k in myList:
				if k < myList[i]:
					min_value = k

		end_time = time.time()
		return min_value, end_time - start_time

	print(find_min([2,3,4,5,6,3,2,4,1]))
	print(find_min_2([2,3,4,5,6,3,2,4,1]))

main()