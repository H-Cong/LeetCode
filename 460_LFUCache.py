# Thanks to great explanation of
# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
# Read a comment said "This question should be banned from the code interview". XDDDDDDDDD

import collections

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None
        
class DLinkedList:
    """ An implementation of doubly linked list.
	
	Two APIs provided:
    
    append(node): append the node to THE HEAD of the linked list.
    pop(node=None): remove the referenced node. 
                    If None is given, remove the one from tail, which is the least recently used.
                    
    Both operation, apparently, are in O(1) complexity.
    """
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def append(self, node):
        p = self.head.next
        p.prev = node
        node.next = p
        node.prev = self.head
        self.head.next = node
        self.size += 1
    
    # you have to have =None here, otherwise the pop() function at put() will throw a error
    def pop(self, node=None):
        if self.size == 0:
            return
        
        # if None is given, remove the one from tail
        if not node:
            node = self.tail.prev
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.size -= 1
        
        return node

class LFUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        
        Three things to maintain:
        
        1. a dict, named as `self._node`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self._freq`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:
           
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
           
        """
        self.size = 0
        self.capacity = capacity
        
        self._node = {} # key:val = key:node
        self._freq = collections.defaultdict(DLinkedList) # key:value = key:DLinkedList
        self._min_freq = 0
        
    def _update(self, node):
        """ 
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minfreq is `f`,
               update self._minfreq to `f+1`
        
        All of the above opeartions took O(1) time.
        """
        freq = node.freq
        
        self._freq[freq].pop(node)
        # this if statement internally checks not self._freq[freq] by checking the length of the DLinkedList is not 0.
        if self._min_freq == freq and not self._freq[freq]:
            self._min_freq += 1
            
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)     

    def get(self, key: int) -> int:
        """
        Through checking self._node[key], we can get the node in O(1) time.
        Just performs self._update, then we can return the value of node.
        
        :type key: int
        :rtype: int
        """
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.
        
        Otherwise, the following logic will be performed
        
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self._node
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
        
        (*) How to pop the least frequently used item? Two facts:
        
        1. we maintain the self._minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)
          
        Consequence? ==> The tail of the DLinkedList with self._minfreq is the least
                         recently used one, pop it...
        
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self._freq[self._min_freq].pop()
                del self._node[node.key]
                self.size -= 1
            
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._min_freq = 1
            self.size += 1


    # TC: O(1)
    # SC: O(capacity)?? I think its this
    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
