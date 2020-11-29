class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        Merge Sort
        '''
        if not nums or len(nums) < 2: return 0
        
        return self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, nums, start, end):
        if start >= end: return 0
        
        mid = start + (end - start) // 2
        
        count = self.mergeSort(nums, start, mid) + self.mergeSort(nums, mid + 1, end)
        
        p, q = start, mid + 1
        
        while p <= mid and q <= end:
            if nums[p] > 2 * nums[q]:
                count += mid - p + 1
                q += 1
            else:
                p += 1
        
        nums[start:end+1] = sorted(nums[start:end+1])
        # nums[start:end+1].sort() # this does not work
        
        return count
    
    # TC: O(n*(logn)^2)
    # if a conventional merge(), which is a O(n) sort function is implemented
    # the overall TC will be O(n*logn). But as we used Timsort, which is a O(nlogn)
    # thus the overall TC is O(n*(logn)^2)
    
    # SC: O(n)
    # Additional space for storing L and R arrays, used in sorted()
    
    # NOTE:
    # 1. "For those who're experiencing TLE: I implemented merge-sort on my own, 
    # thinking that custom merge-sort is O(n) while the built-in sorted is O(n logn), 
    # only to fail with TLE over and over. After a search, I learnt that Python's built-in 
    # sorted is much more efficient, as it's internally implemented in hand-optimized C.
    # 2. Why we use sorted() to sort from start to end:
    # When the while loop in mergeSort() function is executed, it requires both left of mid 
    # and right of mid arrays to be already sorted. Thus this sorted() function is to make sure 
    # of that in the prior recursive call of the current while loop. Otherwise the line of 
    # count += mid - left + 1 wont work. 
    # 3. O(n^2) vs O (n(logn)^2):
    # https://stackoverflow.com/questions/13710629/on2-vs-o-nlogn2/13710732
    # 4. This prob takes me quite some time to figure out...
    
    # ref:
    # https://stackoverflow.com/questions/10948920/what-algorithm-does-pythons-sorted-use
    # https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/
    # Qing Yun Youtube: https://www.youtube.com/watch?v=j68OXAMlTM4
    # https://www.youtube.com/watch?v=tmzg_XGg5dw
    
