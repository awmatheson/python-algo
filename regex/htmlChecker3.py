#  File: htmlChecker.py
#  Description: A program that checks the html tags in a file for completeness
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/18/2015
#  Date Last Modified: 

#class representing the stack abstract data type using lists
class Stack(object):

	def __init_(self):
		self.items = []

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

#this function will read in the html tags and then put them in a list
def getTag(htmlData):
	new_item = []
	if htmlData == []:
		return
	if htmlData[0] == "<":
		for i in htmlData:
			if i == ">" or i == " " :
				newTag = ''.join(new_item)
				print(htmlData)
				return(newTag,htmlData[1:])
			elif i != "<" :
				new_item.append(i)
	else:
		getTag(htmlData[1:])

def htmlCheck(htmlData):
	newTag, newHtmlData = getTag(htmlData)
	htmlTags = [newTag]
	while newHtmlData != []:
		newTag, newHtmlData = getTag(newHtmlData)
		htmlTags.append(newTag)
		print(htmlTags)


def inputFile(fileName):
	inputData = []
	with open(fileName) as f:
		while True:
			char = f.read(1)
			if not char:
				return(inputData)
			if char != "\n" :
				inputData.append(char)


def main():
	
	#call the function that will start the file checking process
	htmlData = inputFile("htmlfile.txt")

	#check the html for errors
	htmlCheck(htmlData)

main()