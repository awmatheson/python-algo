#Description: A binary Tree Implementation
#Author: Alexander Matheson
#Reference: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
#Date Created: 

class BinaryTree(object):
	def __init__(self,initval,left=None,right=None,parent=None):
		self.data = initval
		self.left = left
		self.right = right
		self.parent = parent

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setRootVal(self,value):
		self.data = value

	def getRootVal(self):
		return self.data

	def isLeftChild(self):
		return self.parent and self.parent.left == self

	def isRightChild(self):
		return self.parent and self.parent.right == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.right or self.left)

	def hasAnyChildren(self):
		return self.right or self.left

	def hasBothChildren(self):
		return self.right and self.left

	def replaceNodeData(self,value,lc,rc):
        self.data = value
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

	def insertLeft(self,newNode):
		if self.left == None:
			t = BinaryTree(newNode)
			self.left = t
		else:
			t = BinaryTree(newNode)
			t.left = self.left
			self.left = t

	def insertRight(self,newNode):
		if self.right == None:
			t = BinaryTree(newNode)
			self.right = t
		else:
			t = BinaryTree(newNode)
			t.right = self.right
			self.right = t

class BinarySearchTree()

def main():
	tree = BinaryTree()
	BSD = [70,31,77,84,14,12,23,73,90]
main()