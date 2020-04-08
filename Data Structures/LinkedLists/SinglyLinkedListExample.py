from LinkedList import LinkedList


myList = LinkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.swap_adjacent_nodes()
myList2 = LinkedList()
myList2.append(8)
myList2.append(4) 
myList2.append(2)
myList.sum_of_two_lists(myList2)
myList.move_tail_to_head()
myList.printList()
