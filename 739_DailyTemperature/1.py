class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        Stack
        '''
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                curr = stack.pop()
                ans[curr] = i - curr
            stack.append(i)
        
        return ans
    
    # TC: O(n)
    
    # SC: O(n)
