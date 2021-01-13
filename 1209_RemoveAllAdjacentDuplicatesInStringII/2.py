class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        Two Stack
        '''
        ch, count = [], []
        for c in s:
            if not ch or ch[-1] != c:
                ch.append(c)
                count.append(1)
            else:
                count[-1] += 1
                if count[-1] == k:
                    ch.pop()
                    count.pop()
        
        res = [c*n for c,n in zip(ch, count)]
        
        return "".join(res)
        
    # TC: O(n)
    # where n is a string length. We process each character in the string once.
    
    # SC: O(n)
    # to store the count for each character
    
    # ref: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/
    # ref: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/628576/
