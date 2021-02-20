class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Hashmap
        '''
        ls, lp = len(s), len(p)
        if ls < lp:
            return None
        ds, dp = collections.Counter(), collections.Counter(p)
        ans = []
        for i in range(ls):
            ds[s[i]] += 1
            if i >= lp:
                if ds[s[i-lp]] == 1:
                    del ds[s[i-lp]]
                else:
                    ds[s[i-lp]] -= 1
            if ds == dp:
                ans.append(i-lp+1)
        
        return ans
    
    # TC: O(len(s) + len(p))
    
    # SC: O(26)
