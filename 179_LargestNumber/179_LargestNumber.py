class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Sort
        '''
        str_nums = sorted(map(str, nums), reverse = True)
        swap = False
        while not swap:
            swap = True
            i = 0
            while i < len(nums) - 1:
                if str_nums[i] + str_nums[i+1] < str_nums[i+1] + str_nums[i]:
                    str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                    swap = False
                i += 1
        
        ans = ''.join(str_nums)
        if ans[0] == '0': return '0' # if first char in ans is 0, then all following char are '0' for sure
        
        return ans
    
    # TC: O(nlogn)
    # Although we are doing extra work in our comparator, it is only by a constant factor. 
    # Therefore, the overall runtime is dominated by the complexity of sort, which is O(nlgn).
    
    # SC: O(n)
    
    # 1st line of code equals the following
    #   str_nums = []
    #   for num in nums:
    #       str_nums.append(str(num))
    #   str_nums.sort(reverse=True)
    
    # ref: https://leetcode.com/problems/largest-number/discuss/863449/Python-super-simple-explained-solution-O(nlogn)
