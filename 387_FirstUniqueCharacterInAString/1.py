class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        q = []
        seen = set()
        for i,c in enumerate(s):
            if c not in seen:
                q.append(c)
                seen.add(c)
            elif c in seen and not q:
                continue
            elif c in q:
                q.remove(c)    
        
        return s.find(q[0]) if q else -1
    
    # TC: O(n^2)
    
    # SC: O(n)
