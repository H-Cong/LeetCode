class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            # n & 1 determins the value of last bit
            # then move that bit to left by 31
            ret += (n & 1) << power
            # then move n to right by 1 bit
            n = n >> 1
            # then reduce the power by 1
            power -= 1
        return ret
    
    # TC: O(1)
    # Though we have a loop in the algorithm, the number of 
    # iteration is fixed regardless the input, since the integer 
    # is of fixed-size (32-bits) in our problem.
    
    # SC: O(1)
    # since the consumption of memory is constant regardless the input.

    # ref: https://leetcode.com/problems/reverse-bits/solution/
