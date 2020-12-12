class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Sliding Window
        '''
        start, count = 0, 0
        mapT = collections.Counter(t)
        mapS = {c:0 for c in s}
        result = ""
        
        for i, c in enumerate(s):
            if mapT[c] > 0:
                mapS[c] += 1
                if mapT[c] >= mapS[c]:
                    count += 1
            if count == len(t):
                while mapS[s[start]] == 0 or mapT[s[start]] < mapS[s[start]]:
                    if mapT[s[start]] < mapS[s[start]]:
                        mapS[s[start]] -= 1
                    start += 1
                if result == "" or i - start + 1 < len(result):
                    result = s[start:i+1]
        
        return result
    
    # TC: O(n + m) where n is the length of s
    # we put n + m here because m can be close to n. And if we only iterate s once, 
    # n and m gives similar contibution to the TC
    # mapT: O(m), mapS: O(n). m is len(t)
    # for loop in worst case we iterate s twice, one for start index, one for i, thats a O(2n)
    
    # SC: O(n + m)
    # two dictionaries.
    
    # IDEA: two pointers to form sliding window.
    # we first move the end pointer, i.e. i
    # once we find a valid substring 
    # AND we found a second s[start] in this substring
    # we enter the second if loop
    # and start to move the start pointer. 
    
    # ref: https://www.youtube.com/watch?v=IzynHx-O4lE
