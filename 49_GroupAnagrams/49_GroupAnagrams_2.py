class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # A simplified version of my last submission
        if len(strs) <= 1: return [strs]
        
        seen = {}
        
        for string in strs:
            sortStr = ''.join(sorted(string))
            if sortStr not in seen:
                seen[sortStr] = []
            seen[sortStr].append(string)
        
        return seen.values()
            
    
    # TC: O(n*klogk)
    # k is ave size of string in strs, klogk is .sort() TC
    # n is the length of the strs
    
    # SC: O(n*k)
    # worst case, dict will have n entries and each entry store a size k string
    # in this problem, dict{key:string} is different from key:int
    # the former one take O(nk) where the later takes O(n)
    # another angle to consider this problem, the SC of strs is O(nk)
    # as the dict stores the same amount of information, thus the SC should be the same 
