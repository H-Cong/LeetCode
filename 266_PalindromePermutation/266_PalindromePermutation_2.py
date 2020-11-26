class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # collections.defaultdict(int) sets up a empty dict with value being 0 for each key
        s_dict = collections.defaultdict(int)
        for char in s:
            s_dict[char] += 1
        
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
