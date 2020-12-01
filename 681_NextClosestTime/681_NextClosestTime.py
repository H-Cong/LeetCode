class Solution:
    def nextClosestTime(self, time: str) -> str:
        '''
        
        '''
        hour, minute = time.split(":")  # generate two strings
        
        digit = sorted(set(hour + minute)) # set(string) => set('char', 'char', ...)
        
        num = [a + b for a in digit for b in digit]
        
        i = num.index(minute)
        
        if len(num) > i + 1 and minute < num[i+1] < "60":
            return hour + ":" + num[i+1]
        
        j = num.index(hour)
        
        if len(num) > j + 1 and hour < num[j+1] < "24":
            return num[j+1] + ":" + num[0]
        
        return num[0] + ":" + num[0]
    
    # TC: O(1)
    # there are maximum 16 numbers in num. sort() takes maximum O(4log4).
    
    # SC: O(1)
    
    # ref: https://leetcode.com/problems/next-closest-time/discuss/190816/Python-simple-20ms-solution
