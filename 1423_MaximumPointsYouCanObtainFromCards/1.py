class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints or len(cardPoints) < k: return None
        if len(cardPoints) == k: return sum(cardPoints)
        s = sum(cardPoints[:k])
        ans = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            ans = max(ans, s)
        
        return ans
    
    # TC: O(k)
    
    # SC: O(1)
    
    # NOTE the order of s += should be [-i] - [k-i]
    
    # ref: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/ 
    # read ref comment
