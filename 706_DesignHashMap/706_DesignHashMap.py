class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 2069
        self.hash_table = self.create_buckets()
    
    def create_buckets(self):
        return [[] for _ in range(self.size)] 

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = hash(key) % self.size 
          
        # Get the bucket corresponding to index 
        bucket = self.hash_table[hashed_key] 
  
        found_key = False
        for index, record in enumerate(bucket): 
            record_key, record_val = record 
              
            # check if the bucket has same key as 
            # the key to be inserted 
            if record_key == key: 
                found_key = True
                break
  
        # If the bucket has same key as the key to be inserted, 
        # Update the key value 
        # Otherwise append the new key-value pair to the bucket 
        if found_key: 
            bucket[index] = (key, value) 
        else: 
            bucket.append((key, value)) 
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        # Get the index from the key using 
        # hash function 
        hashed_key = hash(key) % self.size 
          
        # Get the bucket corresponding to index 
        bucket = self.hash_table[hashed_key] 
  
        found_key = False
        for index, record in enumerate(bucket): 
            record_key, record_val = record 
              
            # check if the bucket has same key as  
            # the key being searched 
            if record_key == key: 
                found_key = True
                break
  
        # If the bucket has same key as the key being searched, 
        # Return the value found 
        # Otherwise indicate there was no record found 
        if found_key: 
            return record_val 
        else: 
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        # Get the index from the key using 
        # hash function 
        hashed_key = hash(key) % self.size 
          
        # Get the bucket corresponding to index 
        bucket = self.hash_table[hashed_key] 
  
        found_key = False
        for index, record in enumerate(bucket): 
            record_key, record_val = record 
              
            # check if the bucket has same key as 
            # the key to be deleted 
            if record_key == key: 
                found_key = True
                break
        if found_key: 
            bucket.pop(index) 
        return

    # TC:
    
    # SC:
    
    # ref: https://www.geeksforgeeks.org/hash-map-in-python/
    # ref: https://leetcode.com/problems/design-hashmap/solution/


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
