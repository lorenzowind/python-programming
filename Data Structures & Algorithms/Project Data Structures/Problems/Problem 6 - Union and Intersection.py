class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_llist = LinkedList()

    elements_set = set()

    current_llist_1 = llist_1.head
    current_llist_2 = llist_2.head
    
    while current_llist_1 or current_llist_2:
        value = None

        if current_llist_1 is not None:
            value = current_llist_1.value
            
            if not value in elements_set:
                elements_set.add(value)
                union_llist.append(value)
            
            current_llist_1 = current_llist_1.next
        
        if current_llist_2 is not None: 
            value = current_llist_2.value
            
            if not value in elements_set:
                elements_set.add(value)
                union_llist.append(value)
            
            current_llist_2 = current_llist_2.next

    return union_llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection_llist = LinkedList()

    elements = {}

    current = llist_1.head

    while current:
        elements[current.value] = 1
        current = current.next
    
    current = llist_2.head

    while current:
        if current.value in elements:
            
            if elements[current.value] is not None:
                intersection_llist.append(current.value)
            
            elements[current.value] = None
        
        current = current.next
    
    return intersection_llist

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # returns 3 -> 6 -> 2 -> 32 -> 4 -> 35 -> 9 -> 65 -> 1 -> 11 -> 21 -> 
print (intersection(linked_list_1,linked_list_2)) # returns 6 -> 4 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # returns 3 -> 1 -> 2 -> 7 -> 4 -> 8 -> 35 -> 9 -> 6 -> 11 -> 65 -> 21 -> 23 ->
print (intersection(linked_list_3,linked_list_4)) # returns nothing because doesn't exist elements that are in both A and B

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,1,2,2,3,3,4,5,6,7,8,9]
element_2 = [4,4,5,5,6,6,7,7,10,11,12]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6)) # returns 1 -> 4 -> 2 -> 5 -> 3 -> 6 -> 7 -> 10 -> 11 -> 8 -> 12 -> 9 ->
print (intersection(linked_list_5,linked_list_6)) # returns 4 -> 5 -> 6 -> 7 ->

## Test case 4 - edge cases

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [10**1000, 10**1000 + 1, 10**1000 + 2, 10**1000 + 2, 10**1000 + 3]
element_2 = [10**1000 + 2, 10**1000 + 3, 10**1000 + 1]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8)) # returns 10**1000 -> 10**1000 + 2 -> 10**1000 + 1 -> 10**1000 + 3
print (intersection(linked_list_7,linked_list_8)) # returns 10**1000 + 2 -> 10**1000 + 3 -> 10**1000 + 1
