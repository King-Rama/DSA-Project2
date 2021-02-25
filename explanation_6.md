using the provided code for constructing a linked list
adding a function to convert the LinkedList to normal list and then to set
applying set methods (union, intersection) to the to set objects 
then convert back linked list

Time complexity of union(): -> overall  O(n) 
    assigning and looping -> O(n)
    instantiation -> O(1)
    looping -> O(n)
    python union -> O(n+n) -> O(n)


Time Complexity of intersection(): -> overall 
    converting a linked list of n-nodes to list of n-elements and to set of n-elements:  O(2n) -> O(n)
    perform python set intersection : O(len(set1) * len(set2)) -> O(n*n)

the overall time complexity is O(n*n)
the overall space complexity is O(n)