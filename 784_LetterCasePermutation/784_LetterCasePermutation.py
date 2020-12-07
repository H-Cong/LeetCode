class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for c in S:
            if c.isalpha():
                res = [i+j for i in res for j in [c.lower(), c.upper()]]
            else:
                res = [i+c for i in res]
        
        return res
    
    # TC: O(n*2^n)
    # if we have n letters, there are 2^n ways of permutation
    # then the for i in res loop takes O(n) each time
    
    # SC: O(n*2^n)
    # e.g. if we only have two letters, 'ab', then there are in total 4 permutations
    # that is a 2^n. Then each permutation takes n space where n is the length of the string
