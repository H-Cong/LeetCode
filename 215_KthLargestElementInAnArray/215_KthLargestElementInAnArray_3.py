class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Quick Select
        '''
        low = 0
        high = len(nums) - 1
        # Shuffle to avoid the worst case
        random.shuffle(nums)
        while low <= high:
            pIndex = self.partition(nums, low, high)
            if k < pIndex + 1:
                high = pIndex - 1
            elif k > pIndex + 1:
                low = pIndex + 1
            else:
                return nums[pIndex]

    def partition(self, nums, start, end):
        pIndex = start
        pivot = nums[end]
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex += 1
        nums[pIndex], nums[end] = nums[end], nums[pIndex]
        return pIndex
    
    # TC: O(n) on average, O(n^2) worst
    
    # SC: O(1)
