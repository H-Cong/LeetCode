class Solution:
    def reorganizeString(self, S: str) -> str:
        res = []
        c = collections.Counter(S)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        prev_count, prev_char = 0, ''
        while pq:
            count, char = heapq.heappop(pq)
            res += [char]
            if prev_count < 0:
                heapq.heappush(pq, (prev_count, prev_char))
            count += 1
            prev_count, prev_char = count, char
        res = ''.join(res)
        if len(res) != len(S): return ""
        return res    
    
    # TC: O(nlogk)
    # n is the length of S. k is the size of the alphabet. If we take k as 26, then TC is O(n)
    
    # SC: O(n)
    
    
    # ref: https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue
