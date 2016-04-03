#  File: htmlChecker.py
#  Description: A program that checks the html tags in a file for completeness
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 10/18/2015
#  Date Last Modified: 10/20/2015

#class representing the stack abstract data type using lists
class Stack(object):

	def __init__(self):
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

#function that opens the html file and make it a string
#process each character to find the html tags
#put the tags in a list tagList and return
def getTags(filename):
	f = open(filename)
	html_string = ''.join(f.readlines())
	tagList = []
	htmlTag = None

	#loop through html_string
	for ch in html_string:
		if htmlTag == None:
			#start making a htmlTag starting at '<'
			if ch == '<':
				htmlTag = ''
		else:
			htmlTag += ch
			if ch == '>' or ch == ' ':
				#remove unwanted '<' or ' '
				htmlTag = htmlTag[:-1]
				tagList.append(htmlTag)
				htmlTag = None
	return(tagList)

#function that takes the htmlTags list and places starting tags on the stack
#checks the tags for closing tags and returns the stack after each move.
def checkTags(htmlTags):
	print("The html Tags in this file are: ", htmlTags)

	htmlStack = Stack()

	#a list to view the current stack
	stack = []
	exceptions = ['br', 'br', 'hr', 'meta']

	#loop through htmlTags to check for matches
	for tag in htmlTags:
		if tag in exceptions:
			print("Tag is %s: does not need to match:  stack is now %s" %(tag,stack))
		elif tag[0] != '/' :
			htmlStack.push(tag)
			stack.append(tag)
			print("Tag is %s: pushed: stack is now %s" %(tag,stack))
		elif tag[0] == '/' :
			if tag[1:] == htmlStack.peek():
				htmlStack.pop()
				stack.pop()
				print("Tag is %s: matches: stack is now %s" %(tag,stack))
			else:
				print("Error:  tag is %s but top of stack is %s" %(tag,htmlStack.peek()))
				return
		else:
			print("error")

	#print processing status and stack at completion of iteration
	if htmlStack.isEmpty():
		print("Processing complete.  No mismatches found.")
	else:
		print("Processing complete.  Unmatched tags remain on stack: ", stack)

def main():
	
	#call the function that will start the file checking process
	htmlTags = getTags("htmlfile.txt")

	#check the html for errors
	checkTags(htmlTags)
	

main()