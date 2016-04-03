#  File: LinkedLists.py
#  Description: A program that creates and modifies linked lists
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 11/8/2015
#  Date Last Modified: 11/12/2015


#Node class to create nodes within linked lists
class Node(object):
  def __init__(self, init_data = None, _next = None):
    self.data = init_data
    self.next = _next

  #method to use node as string when printing (redundant getData)
  def __str__(self):
    return str(self.data)

  def getData(self):
    #get data contained within node
    return(self.data)

  def setData(self,newData):
    #set node data
    self.data = newData

  def getNext(self):
    #get next node in the list
    return self.next

  def setNext(self, newNext):
    #set the next node in the list
    self.next = newNext


#Linked List Class for creating and manipulating linked lists
class LinkedList(object):
  def __init__(self):
    self.head = None

  def getLength (self):
    # Return the number of items in the list 
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = current.getNext()
    return count

  def addFirst (self, item):
    # Add an item to the beginning of the list
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def addLast (self, item):
    # Add an item to the end of a list
    if self.isEmpty():
      self.addFirst(item)
    else:
      current = self.head
      while current != None:
        previous = current
        current = current.getNext()
      temp = Node(item)
      previous.setNext(temp)

  def addInOrder (self, item):
    # Insert an item into the proper place of an ordered list.
    # This assumes that the original list is already properly
    #    ordered.
    if self.isEmpty():
      self.addFirst(item)
    else:
      current = self.head
      previous = None
      found = False
      stop = False

      while current != None and not found and not stop:
        if current.getData() == item:
          found = True
        else:
          if current.getData() > item:
            stop = True
          else:
            previous = current
            current = current.getNext()

      temp = Node(item)
      if previous == None:
        self.head = temp
        temp.setNext(current)
      else:
        previous.setNext(temp)
        temp.setNext(current)


  def findUnordered (self, item): 
  # Search in an unordered list
  #    Return True if the item is in the list, False
  #    otherwise.
    current = self.head
    found = False

    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()
    return found

  def findOrdered (self, item): 
  # Search in an ordered list
  #    Return True if the item is in the list, False
  #    otherwise.
  # This method MUST take advantage of the fact that the
  #    list is ordered to return quicker if the item is not
  #    in the list.
    current = self.head
    found = False
    stop = False

    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()
    return found

  def delete (self, item):
  # Delete an item from an unordered list
  #    if found, return True; otherwise, return False
    current = self.head
    found = False
    previous = None

    while not found:
      if current == None:
        return found
      if current.getData() == item:
        found = True
      else:
        previous = current
        current = current.getNext()

    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())

    return found

  def __str__ (self):
  # Return a string representation of data suitable for printing.
  #    Long lists (more than 10 elements long) should be neatly
  #    printed with 10 elements to a line, two spaces between
  #    elements
    current = self.head
    stringaling = []
    endStringaling = []
    count = 0
    while current != None:
      stringaling.append(current.getData())
      if count == 10:
        endStringaling.append("  ".join(stringaling))
        count = -1
        stringaling = []
      count += 1
      current = current.getNext()
    if stringaling != []:
      endStringaling.append("  ".join(stringaling))
    return("\n".join(endStringaling))

  def copyList (self):
  # Return a new linked list that's a copy of the original,
  #    made up of copies of the original elements
    newList = LinkedList()
    current = self.head

    while current != None:
      newList.addLast(current.getData())
      current = current.getNext()

    return(newList)

  def reverseList (self): 
  # Return a new linked list that contains the elements of the
  #    original list in the reverse order.
    newList = LinkedList()
    current = self.head

    while current != None:
      newList.addFirst(current.getData())
      current = current.getNext()

    return(newList)

  def sortList (self): 
  # Return a new linked list that contains the elements of the
  #    original list, sorted into ascending (alphabetical) order.
  #    Do NOT use a sort function:  do this by iteratively
  #    traversing the first list and then inserting copies of
  #    each item into the correct place in the new list.
    newList = LinkedList()
    current = self.head

    while current != None:
      newList.addInOrder(current.getData())
      current = current.getNext()

    return(newList)


  def isSorted (self):
  # Return True if a list is sorted in ascending (alphabetical)
  #    order, or False otherwise
    if self.isEmpty():
      return True
    else:
      previous = self.head
      itSorted = False
      current = previous.getNext()

      while current != None:
        if current.getData() >= previous.getData():
          itSorted = True
        elif current.getData() <= previous.getData():
          return False
        previous = current
        current = current.getNext()
      return itSorted

  def isEmpty (self):
  # Return True if a list is empty, or False otherwise
    if self.head == None:
      return True
    else:
      return False

  def mergeList (self, b): 
  # Return an ordered list whose elements consist of the 
  #    elements of two ordered lists combined.
    newList = LinkedList()
    current = self.head

    while current != None:
      newList.addLast(current.getData())
      current = current.getNext()

    current = b.head
    while current != None:
      newList.addLast(current.getData())
      current = current.getNext()

    return newList.sortList()

  def isEqual (self, b):
  # Test if two lists are equal, item by item, and return True.
    if self.getLength() != b.getLength():
      return False
    else:
      egalite = True
      current = self.head
      currentb = b.head
      while current != None:
        if current.getData() == currentb.getData():
          egalite = True
        else:
          return False
        current = current.getNext()
        currentb = currentb.getNext()
      return egalite

  def removeDuplicates (self):
  # Modify a list, keeping only the first occurrence of an element
  #    and removing all duplicates.  Do not change the order of
  #    the remaining elements.
    if self.isEmpty():
      return self
    else:
      current = self.head
      items = []
      newLinkedList = LinkedList()

      while current != None:
        items.append(current.getData())
        current = current.getNext()

      newList = [items[0]]
      newLinkedList.addFirst(items[0])
      for i in items:
        for j in range(len(items) - 1):
          if i != items[j]:
            if items[j] not in newList:
              newLinkedList.addLast(items[j])
              newList.append(items[j])
      return newLinkedList

def main():

  print ("\n\n***************************************************************")
  print ("Test of addFirst:  should see 'node34...node0'")
  print ("***************************************************************")
  myList1 = LinkedList()
  for i in range(35):
    myList1.addFirst("node"+str(i))

  print (myList1)

  print ("\n\n***************************************************************")
  print ("Test of addLast:  should see 'node0...node34'")
  print ("***************************************************************")
  myList2 = LinkedList()
  for i in range(35):
    myList2.addLast("node"+str(i))

  print (myList2)

  print ("\n\n***************************************************************")
  print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
  print ("***************************************************************")
  greekList = LinkedList()
  greekList.addInOrder("gamma")
  greekList.addInOrder("delta")
  greekList.addInOrder("alpha")
  greekList.addInOrder("epsilon")
  greekList.addInOrder("omega")
  print (greekList)

  print ("\n\n***************************************************************")
  print ("Test of getLength:  should see 35, 5, 0")
  print ("***************************************************************")
  emptyList = LinkedList()
  print ("   Length of myList1:  ", myList1.getLength())
  print ("   Length of greekList:  ", greekList.getLength())
  print ("   Length of emptyList:  ", emptyList.getLength())

  print ("\n\n***************************************************************")
  print ("Test of findUnordered:  should see True, False")
  print ("***************************************************************")
  print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
  print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

  print ("\n\n***************************************************************")
  print ("Test of findOrdered:  should see True, False")
  print ("***************************************************************")
  print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
  print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

  print ("\n\n***************************************************************")
  print ("Test of delete:  should see 'node25 found', 'node34 found',")
  print ("   'node0 found', 'node40 not found'")
  print ("***************************************************************")
  print ("   Deleting 'node25' (random node) from myList1: ")
  if myList1.delete("node25"):
    print ("      node25 found")
  else:
    print ("      node25 not found")
  print ("   myList1:  ")
  print (myList1)

  print ("   Deleting 'node34' (first node) from myList1: ")
  if myList1.delete("node34"):
    print ("      node34 found")
  else:
    print ("      node34 not found")
  print ("   myList1:  ")
  print (myList1)

  print ("   Deleting 'node0'  (last node) from myList1: ")
  if myList1.delete("node0"):
    print ("      node0 found")
  else:
    print ("      node0 not found")
  print ("   myList1:  ")
  print (myList1)

  print ("   Deleting 'node40' (node not in list) from myList1: ")
  if myList1.delete("node40"):
    print ("      node40 found")
  else:
    print ("   node40 not found")
  print ("   myList1:  ")
  print (myList1)

  print ("\n\n***************************************************************")
  print ("Test of copyList:")
  print ("***************************************************************")
  greekList2 = greekList.copyList()
  print ("   These should look the same:")
  print ("      greekList before delete:")
  print (greekList)
  print ("      greekList2 before delete:")
  print (greekList2)
  greekList2.delete("alpha")
  print ("   This should only change greekList2:")
  print ("      greekList after deleting 'alpha' from second list:")
  print (greekList)
  print ("      greekList2 after deleting 'alpha' from second list:")
  print (greekList2)
  greekList.delete("omega")
  print ("   This should only change greekList1:")
  print ("      greekList after deleting 'omega' from first list:")
  print (greekList)
  print ("      greekList2 after deleting 'omega' from first list:")
  print (greekList2)

  print ("\n\n***************************************************************")
  print ("Test of reverseList:  the second one should be the reverse")
  print ("***************************************************************")
  print ("   Original list:")
  print (myList1)
  print ("   Reversed list:")
  myList1Rev = myList1.reverseList()
  print (myList1Rev) 

  print ("\n\n***************************************************************")
  print ("Test of sortList:  the second list should be the first one sorted")
  print ("***************************************************************")
  planets = LinkedList()
  planets.addFirst("Mercury")
  planets.addFirst("Venus")
  planets.addFirst("Earth")
  planets.addFirst("Mars")
  planets.addFirst("Jupiter")
  planets.addFirst("Saturn")
  planets.addFirst("Uranus")
  planets.addFirst("Neptune")
  planets.addFirst("Pluto!")

  print ("   Original list:")
  print (planets)
  print ("   Sorted list:")
  sortedPlanets = planets.sortList()
  print (sortedPlanets)

  print ("\n\n***************************************************************")
  print ("Test of isSorted:  should see False, True")
  print ("***************************************************************")
  print ("   Original list:")
  print (planets)
  print ("   Sorted: ", planets.isSorted())
  sortedPlanets = planets.sortList()
  print ("   After sort:")
  print (sortedPlanets)
  print ("   Sorted: ", sortedPlanets.isSorted())

  print ("\n\n***************************************************************")
  print ("Test of isEmpty:  should see True, False")
  print ("***************************************************************")
  newList = LinkedList()
  print ("New list (currently empty):", newList.isEmpty())
  newList.addFirst("hello")
  print ("After adding one element:",newList.isEmpty())

  print ("\n\n***************************************************************")
  print ("Test of mergeList")
  print ("***************************************************************")
  list1 = LinkedList()
  list1.addLast("aardvark")
  list1.addLast("cat")
  list1.addLast("elephant")
  list1.addLast("fox")
  list1.addLast("lynx")
  print ("   first list:")
  print (list1)
  list2 = LinkedList()
  list2.addLast("bacon")
  list2.addLast("dog")
  list2.addLast("giraffe")
  list2.addLast("hippo")
  list2.addLast("wolf")
  print ("   second list:")
  print (list2)
  print ("   merged list:")
  list3 = list1.mergeList(list2)
  print (list3)

  print ("\n\n***************************************************************")
  print ("Test of isEqual:  should see True, False, True")
  print ("***************************************************************")
  print ("   First list:")
  print (planets)
  planets2 = planets.copyList()
  print ("   Second list:")
  print (planets2)
  print ("      Equal:  ",planets.isEqual(planets2))
  print (planets)
  planets2.delete("Mercury")
  print ("   Second list:")
  print (planets2)
  print ("      Equal:  ",planets.isEqual(planets2))
  print ("   Compare two empty lists:")
  emptyList1 = LinkedList()
  emptyList2 = LinkedList()
  print ("      Equal:  ",emptyList1.isEqual(emptyList2))

  print ("\n\n***************************************************************")
  print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
  print ("***************************************************************")
  dupList = LinkedList()
  print ("   removeDuplicates from an empty list shouldn't fail")
  newList = dupList.removeDuplicates()
  print ("   printing what should still be an empty list:")
  print (newList)
  dupList.addLast("giraffe")
  dupList.addLast("wolf")
  dupList.addLast("cat")
  dupList.addLast("elephant")
  dupList.addLast("bacon")
  dupList.addLast("fox")
  dupList.addLast("elephant")
  dupList.addLast("wolf")
  dupList.addLast("lynx")
  dupList.addLast("elephant")
  dupList.addLast("dog")
  dupList.addLast("hippo")
  dupList.addLast("aardvark")
  dupList.addLast("bacon")
  print ("   original list:")
  print (dupList)
  print ("   without duplicates:")
  newList = dupList.removeDuplicates()
  print (newList)

main()