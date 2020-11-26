class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {}
        for i, ch in enumerate(S):
            last_index[ch] = i
        
        start = end = 0
        ans = []
        for i, ch in enumerate(S):
            end = max(end, last_index[ch])
            if i == end:
                ans.append(end-start+1)
                start = end + 1
        
        return ans
    
    # TC: O(n)
    # n is the length of S
    
    # SC: O(1)
    # to keep the data structure of last_index of no more than 26 characters
