# to achieve O(1) for both get() and put(), we need two data structures: hashmap & linked list
# hashmap (or dict in Python term) is used to store the key of the node as key, and the address of the node as value
# linked list is used to store the actual key-value pair
# doubly linked list has two pointers: next and prev to point to next and previous node
# reference video: https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be&ab_channel=EvanLavizadeh

class Node:
    # initialization method
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Dict = {}
        self.head = Node(0,0) # dummy head
        self.tail = Node(0,0) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # by convention, the most recently used (MRU) node is added right before the tail node
    # Thus we always use self.tail.prev to find the node before the tail node and add the new node right after it  
    
    def _add(self, node):
        pointer = self.tail.prev
        pointer.next = node
        node.prev = pointer
        node.next = self.tail
        self.tail.prev = node
        
    # for removing a node, we use this node to find its previous node
    # and change the link edge of this previous node directly to the node after the gonna-be-deleted node
    
    def _remove(self, node):
        pointer = node.prev
        pointer.next = node.next
        node.next.prev = pointer

    def get(self, key: int) -> int:
        if key not in self.Dict:
            return -1
        node = self.Dict[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.Dict:
            self._remove(self.Dict[key]) # remember the value of the dict is the address, i.e. the actual node, thus we used the self.Dict[key]
            del self.Dict[key] # dont forget to delete the key from dict
        if len(self.Dict) == self.capacity: # if the capacity is reached
            # we find the LRU from the list and delete it
            lru_node = self.head.next
            self._remove(lru_node) # we dont need to go through the dict as we already have this node
            del self.Dict[lru_node.key]
        
        # add this node to the MRU position
        node = Node(key, value)
        self.Dict[key] = node
        self._add(node)

    # TC: O(1)
    # SC: O(capacity) 
    # since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
