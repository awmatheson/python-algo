#  File: TreeConvert.py
#  Description: A program that converts binary tree from list of lists 
#          or prints binary trees in preorder, postorder or inorder format
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 11/17/2015
#  Date Last Modified: 11/20/2015

#List of lists implementation of Binary Tree
def ListBinaryTree(initdata):
	return [initdata, [], []]

#get the root value of the tree
def getRootVal(root):
	return root[0]

#change the root value of the tree
def setRootVal(root, newVal):
	root[0] = newVal

#get the left child of the root of the tree
def getLeftChild(root):
	return root[1]

#get the right child of the root of the tree
def getRightChild(root):
	return root[2]

#insert a new left branch at the specified node "root"
def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])


#Nodes and Pointers implementation of Binary Tree
class NodeBinaryTree(object):
	def __init__(self,initval):
		self.data = initval
		self.left = None
		self.right = None

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setRootVal(self,value):
		self.data = value

	def getRootVal(self):
		return self.data

	def insertLeft(self, newNode):
		if self.left == None:
			t = NodeBinaryTree(newNode)
			self.left = t
		else:
			t = NodeBinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insertRight(self,newNode):
		t = NodeBinaryTree(newNode)
		t.right = self.right
		self.right = t

def convert(pyList):
	if pyList == []:
		return None
	else:
		tree = NodeBinaryTree(pyList[0])
		tree.left = convert(pyList[1])
		tree.right = convert(pyList[2])
		return tree

def getData(inputfile):
	f = open(inputfile)
	pyListData = []
	end = False

	while not end:
		inList = (f.readline())
		if inList != "":
			pyList = eval(inList)
			pyListData.append(pyList)
		else:
			end = True

	return pyListData

def listConvert(pyListData):
	listofTrees = []
	for pyList in pyListData:
		newTree = convert(pyList)
		listofTrees.append(newTree)

	return listofTrees

def inorder(tree):
	#return string of tree in inorder
	if tree != None:
		inorder(tree.left)
		print(tree.getRootVal(), end = ' ')
		inorder(tree.right)

def preorder(tree):
	#return string of tree in preorder
	if tree:
		print(tree.getRootVal(), end = ' ')
		preorder(tree.left)
		preorder(tree.right)

def postorder(tree):
	#return string of tree in postorder
	if tree != None:
		postorder(tree.left)
		postorder(tree.right)
		print(tree.getRootVal(), end = ' ')

#Main
def main():

	pyLists = getData("treedata.txt")

	trees = listConvert(pyLists)
	print(trees)
	
	for i in range(len(trees)):
		treeInorder = []
		print("\nlist = " + str(pyLists[i]))
		print("inorder:")
		inorder(trees[i])
		print("\npreorder:")
		preorder(trees[i])
		print("\npostorder:")
		postorder(trees[i])
		print("")

main()
