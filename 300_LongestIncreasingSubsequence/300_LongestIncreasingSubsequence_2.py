class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Binary Search. Similar: 334
        '''
        sub = []
        for val in nums:
            idx = self.BS(val, sub)
            if idx == len(sub):
                sub.append(val)
            else:
                sub[idx] = val
        
        return len(sub)
    
    def BS(self, val, sub):
        l, r = 0, len(sub)
        while l < r:
            m = l + (r-l) // 2
            if val < sub[m]:
                r = m
            elif val > sub[m]:
                l = m + 1
            else:
                return m
        return l
    
    # TC: (nlogn)
    
    # SC: O(n)
    
    # if using l < r, then it is the range of [l,r), meaning r = len(sub) instead of len(sub) - 1
    # why return l:
    # sub = [1, 3, 4, 7]
    # val = 2
    # l = 0, r = 4
    # m = 2
    # val < 4 = sub[2]
    # r = 2
    # m = 1
    # val < 3 = sub[1]
    # r = 1
    # m = 0
    # val > 1 = sub[0]
    # l = 1
    
    # essentially, when we move l pointer for the last time, it means that val > sub[m], and val < sub[m+1]
    # and val < each elements in sub[m+1:r]
    # thus we return l as sub[l] is the closest one that sub[l] > val
    
    # ref: https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step
