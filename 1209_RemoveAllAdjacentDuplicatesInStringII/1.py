class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        Memoise Count
        '''
        ans = list(s)
        count = [0]*len(s)
        i = 0
        while i < len(ans):
            if i == 0 or ans[i] != ans[i-1]:
                count[i] = 1
            else:
                count[i] = count[i - 1] + 1
                if count[i] == k:
                    del ans[i-k+1:i+1]
                    i -= k
            i += 1
        
        return "".join(ans)
    
    # TC: O(n^2)
    # where n is a string length. We process each character in the string once. And slicing takes O(n)???
    
    # SC: O(n)
    # to store the count for each character
    
    # ref: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solution/
    # ref: https://stackoverflow.com/questions/11905606/changing-the-number-of-iterations-in-a-for-loop


