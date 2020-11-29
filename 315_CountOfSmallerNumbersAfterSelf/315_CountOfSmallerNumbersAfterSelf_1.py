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
        temp = []
        
        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                temp.append(enum[p])
                res[enum[p][0]] += inversion_count
                p += 1
            else:
                temp.append(enum[q])
                inversion_count += 1
                q += 1
        
        # if p <= mid:
        #     temp += enum[p:]  # probabaly should be enum[p:mid+1]
        #     res[enum[p][0]:] += inversion_count # this does not work for list, it only works for nparray
        
        while p <= mid:
            temp.append(enum[p])
            res[enum[p][0]] += inversion_count
            p += 1
            
        if q <= end:
            temp += enum[q:end + 1]  # TLE happens if use enum[q:] instead of enum[q:end+1]
        
        # while q <= end:          # this works as well
        #     temp.append(enum[q])
        #     q += 1
        
        enum[start:end+1] = temp
        
    # TC: O(nlogn)
    
    # SC: O(n)
    # to store the temp list

    # ref: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/952714/Two-solutions-based-on-MergeSort-EXPLAINED
