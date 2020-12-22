class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Sliding window
        '''
        if not s: return 0
        count = collections.defaultdict(int)
        best = i = 0
        for j in range(len(s)):
            count[s[j]] += 1
            best = max(best, count[s[j]])
            if j - i + 1 > best + k:
                count[s[i]] -= 1
                i += 1
        
        return j - i + 1
    
    # TC: O(n)
    
    # SC: O(n)
    
    # Once we start to shift left boundary, end - start + 1 will always 
    # maintain the optimal result until a better result is found.     
    # Thus we can just return end - start + 1 or even len(s) - start. 
    # One thing, though, is you have to have a line to check corner case first, i.e. s = "".
