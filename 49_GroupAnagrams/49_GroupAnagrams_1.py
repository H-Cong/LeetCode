class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # len(str) is equal or longer than 1
        # len(str[i]) can be 0
        if len(strs) <= 1: return [strs]
        
        seen = {}
        
        for string in strs:
            sortStr = self.strToList(string)
            if sortStr not in seen:
                seen[sortStr] = []
            seen[sortStr].append(string)
        
        res = []
        for key in seen: # or seen.keys()
            res.append(seen[key])
        
        return res
            
    
    def strToList(self, string):
        # convert string to list of char and sort it
        charList = sorted(list(string))
        
        # or 
        # charList = list(string)
        # charList.sort()
        
        # return the sorted string
        return ''.join(charList)
    
    # TC: O(n*klogk)
    # k is ave size of string in strs, klogk is .sort() TC
    # n is the length of the strs
    
    # SC: O(n*k)
    # worst case, dict will have n entries and each entry store a size k string
    # in this problem, dict{key:string} is different from key:int
    # the former one take O(nk) where the later takes O(n)
    # another angle to consider this problem, the SC of strs is O(nk)
    # as the dict stores the same amount of information, thus the SC should be the same 
