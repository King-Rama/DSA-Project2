The problem that was being tackled was to find all occurences of the characters in the
message "The bird is the word" and other test case messages which are "sabnahisdn#njk", "kjlvsdr01?!osmimfs", "aa",
"aaa", "aaaa", "aaaaa", "aaaaaa" to create an efficient way to encode and decode the message.
The reason i decided to use heapq as a python module to solve the huffman module as reccomended by most of the literatures.
Since the heap is used, the weight of each tree is stored successfully. Every loop in the program required a time of O(logn)
to loop through out the program and to place the characters in the priority queue. Each of the character has O(n) loops/iterations.

Technically while passing through the code the complexity was obtained after examining our code functions and summing them together to 
get O(1) + O(n) + O(n) +O(1) + O(logn) + O(logn) + O(1) + O(1) + O(1) + O(nlogn) + O(logn) since there was
an if statement inside a for loop in the huffman decoding function + O(n) for the for and while loops 
test cases. So from that assesment I concluded that the time complexity of the solution is
O(nlogn).

The space complexity will be that of traversing through the tree via the
nodes which is O(the number of characters in the string)