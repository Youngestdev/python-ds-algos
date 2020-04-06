from LinkedList import *


myList = LinkedList()
myList.append(5)
myList.append(6)
myList.append(3)

myList2 = LinkedList()
myList2.append(8)
myList2.append(4) 
myList2.append(2)
myList.sum_of_two_lists(myList2)
myList.move_tail_to_head()
myList.printList()