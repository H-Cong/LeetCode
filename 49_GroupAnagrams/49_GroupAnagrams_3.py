from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        # ans = {}
        
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            # if tuple(count) not in ans:
            #     ans[tuple(count)] = []
            ans[tuple(count)].append(string) 
        
        return ans.values()
            
    
    # TC: O(n*k)
    # where n is the length of strs, and k is the maximum length of a string in strs.
    # Counting each string is linear in the size of the string, and we count every string.
    
    # SC: O(n*k)
    # worst case, dict will have n entries and each entry store a size k string
    # in this problem, dict{key:string} is different from key:int
    # the former one take O(nk) where the later takes O(n)
    # another angle to consider this problem, the SC of strs is O(nk)
    # as the dict stores the same amount of information, thus the SC should be the same
    
    # NOTE: We have to use tuple as key but not list
    # The issue is that tuples are immutable, and lists are not
    
    # NOTE2: O(nk) is not necessary faster than O(nklogk) in practice
    # https://stackoverflow.com/questions/27932832/on-algorithm-slower-than-on-logn-algorithm
    
    
