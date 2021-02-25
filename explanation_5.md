To mimic the behaviour of the actual blockchain I have used linked list concept to create the Blockchain.
The blockchain class keeps the reference of genesis and tail block. This makes easy to perform task like
adding new block to the chain which has a constant time complexity O(1) as well as constant space complexity.
to_list method has a linear time complexity O(n) as well as linear space complexity caused by iterating the
chain to create the list. Transforming the chain to the list has advantage when it comes to task like search.