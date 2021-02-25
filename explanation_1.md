the implementation uses Doubly linked list and dictionary

DoublyLinkedList:
    so as it can be easy to shift or delete an element in the linked list without the need to traverse the whole list

Dictionary:
    to be able to keep unique resource id's as keys and Node objects address as a value and access in a constant time
       
Complexity:
set(): overall O(1)
    checking list size -> O(1)
    deleting and dictionary element(involve shallow copy) -> O(1)
    dictionary lookup -> O(1)

get():  overall O(1)
    dictionary lookup -> O(1)
    assigning node -> O(1)
    

Space of complexity: O(n)
the LRU Cache takes 
    - linked list on n size
    - a hashmap(dict and linked-list) of specified n size
    there for the overall space complexity is O(n) 