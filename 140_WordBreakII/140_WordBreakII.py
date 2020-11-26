class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # reason for convert list to set is set is significantly faster when checking whether 
        # a element is in set vs in list
        # code can still run without this conversion
        words = set(wordDict)
        mem = {}
        def canBreak(s):
            if s in mem: return mem[s]
            ans = []
            if s in words: ans.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right not in words: continue
                ans += [w + " " + right for w in canBreak(s[:i])]
            mem[s] = ans
            return mem[s]
        return canBreak(s)
