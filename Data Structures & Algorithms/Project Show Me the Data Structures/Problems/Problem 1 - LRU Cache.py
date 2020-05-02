class DoubleNode(object):
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

    def set_value(self, value):
        self.value = value

class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.hashMap = HashMap()

    def prepend(self, key, value, num_elements, capacity):
        node = self.hashMap.get(key)

        if node != -1:
            self.hashMap.update(key, node, value)
            self.search(key)
            return -1

        if num_elements == capacity:
            self.hashMap.delete(self.tail.key)
            self.change_tail()
        
        node = DoubleNode(key, value)

        if self.head is not None:
            self.change_head(node)
        else:
            self.tail = node

        self.head = node

        self.hashMap.put(key, self.head)
    
    def search(self, key):
        node = self.hashMap.get(key)

        if node == -1:
            return node

        if node is not self.head:
            if node.next != None:
                node.next.previous = node.previous
                node.previous.next = node.next

            if self.head is not None:
                self.change_head(node)

            if self.tail is node:
                self.change_tail()

            self.head = node

        return node.value
        
    def change_head(self, node):
        node.next = self.head
        self.head.previous = node

    def change_tail(self):
        self.tail = self.tail.previous
        self.tail.next = None

class HashMap(object):

    def __init__(self):
        self.bucket_array = {}

    def put(self, key, node):
        self.bucket_array[key] = node

    def update(self, key, node, value):
        node.set_value(value)

        self.put(key, node)

    def get(self, key):
        node = self.bucket_array.get(key)

        if node is None:
            return -1
        
        return node

    def delete(self, key):
        self.bucket_array[key] = None

class LRU_Cache(object):

    def __init__(self, capacity):
        self.linkedList = DoublyLinkedList()
        self.num_elements = 0
        self.capacity = capacity

    def get(self, key):
        return self.linkedList.search(key)

    def set(self, key, value):
        if key != None and key != '' and value != None and value != '':
            if self.linkedList.prepend(key, value, self.num_elements, self.capacity) != -1:
                if self.num_elements < self.capacity:
                    self.num_elements += 1

# Test case 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1)) # returns 1
print(our_cache.get(2)) # returns 2
print(our_cache.get(9)) # returns -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3)) # returns -1

# Test case 2 - edge cases

edge_cache_1 = LRU_Cache(2)

edge_cache_1.set(10**10000, 1)
edge_cache_1.set(10**10000 + 1, 2)
edge_cache_1.set(10**10000 + 2, 3)

print(edge_cache_1.get(10**10000 + 2)) # returns 3
print(edge_cache_1.get(10**10000)) # returns -1
print(edge_cache_1.get(10**10000 + 1)) # returns 2

# Test case 3 - edge cases

edge_cache_2 = LRU_Cache(5)

edge_cache_2.set('', 1)
print(edge_cache_2.get('')) # returns -1 because this key is not valid

edge_cache_2.set(None, 1)
print(edge_cache_2.get(None)) # returns -1 because this key is not valid

edge_cache_2.set(1, '')
print(edge_cache_2.get(1)) # returns -1 because this value is not valid

edge_cache_2.set(1, None)
print(edge_cache_2.get(1)) # returns -1 because this value is not valid
