#bubble sort and smart bubble sort algorithm

def bubbleSort(myList):

	for num in range(len(myList) - 1,0,-1):
		for i in range(num):
			if myList[i] > myList[i+1]:
				temp = myList[i]
				myList[i] = myList[i+1]
				myList[i] = temp

def shortBubbleSort(myList):

	exchanges = True
	passnum = len(myList) - 1

	while passnum > 0 and exchanges == True:
		exchanges = False
		for i in range(passnum):
			if myList[i] > myList[i+1]:
				exchanges = True
				temp = myList[i]
				myList[i] = myList[i+1]
				myList[i] = temp
		passnum -= 1

def main ():
	
	alist=[20,30,100,90,50,60,70,80,60,110]
	bubbleSort(alist)
	print(alist)

main()