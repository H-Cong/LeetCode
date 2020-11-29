class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        '''
        Merge Sort
        '''
        
        res  = [0] * len(nums)
        enum = list(enumerate(nums)) 
        
        self.mergeSort(enum, 0, len(nums) - 1, res)
        return res
    
    def mergeSort(self, enum, start, end, res):
        if start >= end: return
        
        mid = start + (end - start) // 2
        self.mergeSort(enum, start, mid, res)
        self.mergeSort(enum, mid + 1, end, res)
        self.merge(enum, start, mid, end, res)
    
    def merge(self, enum, start, mid, end, res):
        p, q = start, mid + 1
        inversion_count = 0
        
        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                res[enum[p][0]] += inversion_count
                p += 1
            else:
                inversion_count += 1
                q += 1
        
        while p <= mid:
            # res[enum[p][0]] += inversion_count
            res[enum[p][0]] += end - mid
            p += 1
        
        enum[start:end+1] = sorted(enum[start:end+1], key=lambda e:e[1])
        
    # TC: O(n(logn)^2)
    # since we used Timsort instead of the conventional O(n) merge() function in mergeSort()
    
    # SC: O(n)
    # to store the temp list

    # ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/952714/Two-solutions-based-on-MergeSort-EXPLAINED
