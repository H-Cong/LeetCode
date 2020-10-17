class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # create a empty dict
        s_dict = {}
        
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        counter = 0
        for key in s_dict:
            counter += s_dict[key] % 2
            if counter <= 1:
                continue
        
        return counter <= 1
    
        # TC: O(N)
        # This O(N) comes from the first for loop
        # Second for loop has TC of O(1) as the length of the dict wont be longer than 128
        # SC: O(1)
        # This is because the max length of the dict is 128. Its a constant number
        
        # NOTE: "key in dict" is the same as "key in dict.keys()"
        # And the in operation on a dict, or the dict_keys object you get back from calling keys() on it (in 3.x), is not O(N), it's O(1).
        
        # This is because The "in" operator, like most other operators, is just a call to a __contains__ method 
        # (or the equivalent for a C/Java/.NET/RPython builtin). list implements it by iterating the list and comparing each element; 
        # dict implements it by hashing the value and looking up the hash, thus O(1)
        
        # Even in 3.x, you don't want to call keys, because there's no need to. Iterating a dict, checking its __contains__, 
        # and in general treating it like a sequence is always equivalent to doing the same thing to its keys, so why bother?
        
        # More info at https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
