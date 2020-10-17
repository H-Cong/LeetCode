class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # palindrome: A string that read the same forwards or backwards.
        dist_char = []
        l = len(s)
        
        for i in s:
            if i in dist_char:
                # list.remove(x) deletes the first occurrence of element x from the list.
                # list.remove() has TC of O(N), SC of O(1)
                dist_char.remove(i)
            else:
                # list.append() has TC and SC both as O(1)
                dist_char.append(i)
                
        l_d = len(dist_char)
                
        return l_d <= 1
    
        # TC: O(N) 
        # The for loop has O(len(s)) where essentially is O(N) as len(s) grows
        # The list.remove() has O(N) TC BUT, as there are only 128 distinct ASCII char exists, thus the len(dist_char) will not 
        # exceed 128. Thus this is actually O(1) in this problem. 
        # Thus the TC is O(N).
        # IF, there can be unlimited number of distict char exists, then the TC will be O(N^2)
        
        
        # SC: O(1)
        # The SC comes from the dist_char list as well. Similarly, as the len(dist_char) will not be longer than 128, thus its O(1).
