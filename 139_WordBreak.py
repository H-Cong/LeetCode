"""
m is a dict to store whether any substring can be broke by the words in wordDict
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def canBreak(s, m, wordDict):
            # this if should return m[s] instad of return True
            # if s in m: return True
            if s in m: return m[s]
            
            if s in wordDict:
                m[s] = True
                return True
            """
            this for start at 1 instead of 0 
            Because the previous if loop has checked the s as a whole word
            You can set range starting from 0 but its just unnecessary
            """
            """
            HOWEVER, even if you set range from 0, you still have to have
            the if s in wordDict statement otherwise a wrong answer will be outputted
            This is because, when you set range starting from 0
            a empty string "" will be checked sooner or later
            As the len of the empty string is 0, this gives a range(0, 0) in
            the for loop, thus the loop will be iterated 0 time and directly 
            jumps to m[""]=False, which will lead to the final answer be always False
            PLUS the description said wordDict contains non-empty words
            """
            for i in range(1, len(s)):
                r = s[i:]
                l = s[:i]
                if r in wordDict and canBreak(l, m, wordDict):
                    m[s] = True
                    return True
            
            m[s] = False
            return False
        
        return canBreak(s, {}, wordDict)
    
    # TC: O(n*m*k) ~ O(n^3) or maybe between O(N^2) and O(N^3)
    # [length of s]*[size of dict]*[avg length of words in dict]
    # SC: O(n)
    # n for the length hashtable m that stores the substring:True/False 
