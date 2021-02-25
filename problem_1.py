class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LRU_Cache(object):
    """
    this is an implementation of LRU_Cache
    tail -> will indicate the most recently used value
    head -> will indicate the least recently used value
    """
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.my_dict = dict()
        self.tail = None
        self.head = None

    def remove_head(self, node):
        # removing the head node if the cache capacity is reached
        node.next = self.head.next
        node.previous = None
        self.head = node.next
        self.size -= 1

    def remove_node(self, node):
        # removing the middle node if its requested
        back_node = node.next
        front_node = node.previous
        front_node.next = back_node
        back_node.previous = front_node
        self.size -= 1

    def append(self, node):
        # append the most recently requested resource
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        self.size += 1

    def get(self, key):
        # getting element in the cache
        if key not in self.my_dict:
            return -1
        else:
            node = self.my_dict[key]
            if self.head is not node and self.tail is not node:
                self.remove_node(node)
                self.append(node)
                return node.value
            else:
                return node.value

    def set(self, key, value):
        # putting/ adding requested resources to the cache
        if self.capacity > 0:
            if self.size == self.capacity:
                self.my_dict.pop(self.head.value)
                self.remove_head(self.head)
            if key in self.my_dict:
                if key != value:
                    node = Node(value)
                    self.my_dict.pop(key)
                    self.my_dict[key] = node
                    self.append(node)
                else:
                    node = self.my_dict[key]
                    self.remove_node(node)
                    self.append(node)
            else:
                new_node = Node(value)
                self.my_dict[key] = new_node
                self.append(new_node)
        else:
            return -1


# Test 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)


print(our_cache.get(3))       # return 3
our_cache.set(5, 5)
print(our_cache.get(4))       # return 4
print(our_cache.get(5))       # return 5
print(our_cache.get(1))       # return -1

print("""\n
    end of test 1
    \n
""")

# Test 2
new_cache = LRU_Cache(0)

new_cache.set(100, 100)
print(new_cache.get(100))     # return -1
new_cache.set(2, 2)
print(new_cache.get(0))       # return -1
new_cache.set(17, 17)
print(new_cache.get(17))      # return -1

print("""\n
    end of test 2
    \n
""")

# Test 3
test_cache = LRU_Cache(1)

test_cache.set(1, 1)
test_cache.set(20, 20)
print(test_cache.get(1))      # return -1
print(test_cache.get(20))     # return 20
test_cache.set(13, 13)
print(test_cache.get(20))     # return -1


print("""\n
    end of test 3
    \n
""")


# Test 4
our_cache1 = LRU_Cache(3)
our_cache1.set(1, 1)
our_cache1.set(2, 2)
our_cache1.set(3, 3)
our_cache1.set(4, 4)
print(our_cache1.get(4))   # Expected Value = 4
print(our_cache1.get(1))   # Expected Value = -1
our_cache1.set(2, 4)
print(our_cache1.get(2))   # Expected Value = 4
our_cache1.set(5, 5)
print(our_cache1.get(3))   # Expected Value = -1
print(our_cache1.get(5))  # Expected Value = 5
our_cache1.set(2, 6)

print(our_cache1.get(2))   # Expected Value = 6