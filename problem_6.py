class Node(object):
    """
	implementation of a signle linked-list
	"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """
	this is a basic linked list
	with some addition to display the list with some intuitive way
	"""

    def __init__(self):
        self.head = None

    def __str__(self):
        # method of displaying the linked list
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        # this method append an element to the tail of linked list
        # and the new element become the tail
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        # return the size of linked list to reduce lookup-time
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def to_list(linked_list):
    # this func is for converting the linked-list to a set()
    my_new_list = set()
    my_head = linked_list.head
    while my_head:
        my_new_list.add(my_head.value)
        my_head = my_head.next
    return my_new_list


def back_to_linked_list(incoming_set):
    # helper func to convert set to linked-list, return a linked-list
    new_linked_list = LinkedList()
    for x in incoming_set:
        new_linked_list.append(x)
    return new_linked_list


def union(llist_1, llist_2):
    # perform set union to our two sets
    my_set1 = set(to_list(llist_1))
    my_set2 = set(to_list(llist_2))

    return back_to_linked_list((my_set1.union(my_set2)))


def intersection(l_list_1, l_list_2):
    # perform set intersection to our two sets and return a new linked list
    #  with the help of back_to_linked_list()
    my_set1 = set(to_list(l_list_1))
    my_set2 = set(to_list(l_list_2))

    return back_to_linked_list((my_set1.intersection(my_set2)))


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 21 -> 6 ->


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
#


# Test case 3
# Empty element lists

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("\nUnion of the linked lists: ", union(linked_list_5, linked_list_6))
print("Intersection of the linked lists: ",intersection(linked_list_5, linked_list_6))
# Union of the linked lists:
# Intersection of the linked lists:



# Test case 4
# Empty element 1 list

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [3, 2, 4, 35, 6, 8, 10, 6, 4, 3, 23]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("\nUnion of the linked lists: ", union(linked_list_7, linked_list_8))
print("Intersection of the linked lists: ",intersection(linked_list_7, linked_list_8))
# Union of the linked lists:  2 -> 35 -> 3 -> 4 -> 6 -> 8 -> 10 -> 23 ->
# Intersection of the linked lists:





# Test case 5
# Using similar lists

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [5, 6, 8, 10, 6, 4, 3, 23, 9, 200, 50, 51, 48, 25, 97, 100055853, 58933018000, 4556, 52, 73, 34, 21,23, 2444, 34, 788, 567, 789, 193193913, 39394449, 382148284, 91381, 1763474, 3171371,138381393, 3813813, 318381 ,13384848]
element_2 = [5, 6, 8, 10, 6, 4, 3, 23, 9, 200, 50, 51, 48, 25, 97, 100055853, 58933018000, 4556, 52, 73, 34, 21,23, 2444, 34, 788, 567, 789, 193193913, 39394449, 382148284, 91381, 1763474, 3171371,138381393, 3813813, 318381 ,13384848]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print("\nUnion of the linked lists: ", union(linked_list_9, linked_list_10))
print("Intersection of the linked lists: ",intersection(linked_list_9, linked_list_10))
# Union of the linked lists:  3 -> 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> 2444 -> 58933018000 -> 39394449 -> 1763474 -> 13384848 -> 788 -> 21 -> 789 -> 23 -> 25 -> 34 -> 3171371 -> 100055853 -> 318381 -> 48 -> 50 -> 51 -> 52 -> 3813813 -> 567 -> 193193913 -> 382148284 -> 200 -> 73 -> 4556 -> 138381393 -> 97 -> 91381 ->
# Intersection of the linked lists:  3 -> 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> 2444 -> 58933018000 -> 39394449 -> 1763474 -> 13384848 -> 788 -> 21 -> 789 -> 23 -> 25 -> 34 -> 3171371 -> 100055853 -> 318381 -> 48 -> 50 -> 51 -> 52 -> 3813813 -> 567 -> 193193913 -> 382148284 -> 200 -> 73 -> 4556 -> 138381393 -> 97 -> 91381 ->





# Test case 6
# Including a None value in element 2

linked_list_11 = LinkedList()
linked_list_12 = LinkedList()

element_1 = [5, 6, 8, 10, 6, 4, 3, 23, 9, 200, 50, 51, 48, 25, 97, 100055853, 58933018000, 4556, 52, 73]
element_2 = [5, 6, 8, None, 5030, 34, 55, 41, 14, 45,25, 97, 73]

for i in element_1:
    linked_list_11.append(i)

for i in element_2:
    linked_list_12.append(i)

print("\nUnion of the linked lists: ", union(linked_list_11, linked_list_12))
print("Intersection of the linked lists: ",intersection(linked_list_11, linked_list_12))
# Union of the linked lists:  3 -> 4 -> 5 -> 6 -> 8 -> 9 -> 10 -> 200 -> 73 -> 4556 -> None -> 14 -> 58933018000 -> 23 -> 25 -> 97 -> 34 -> 5030 -> 41 -> 100055853 -> 45 -> 48 -> 50 -> 51 -> 52 -> 55 ->
# Intersection of the linked lists:  97 -> 5 -> 6 -> 8 -> 73 -> 25 ->