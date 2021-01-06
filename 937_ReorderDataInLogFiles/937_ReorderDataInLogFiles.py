class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        Sorting by Keys
        '''
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        def weirdOrder(log):
            all_parts = log.split()
            key, rest = all_parts[0], all_parts[1:]
            return ' '.join(rest) + ' ' + key
        letter_logs.sort(key=weirdOrder)
        return letter_logs + digit_logs
    
    # TC: O(m*n*logn). n is the number of logs in the list. m is the maximum length of a single log
    # sort() takes O(nlogn), the comparison of two logs takes up to O(m) time.
    
    
    # SC: O(m*n)
    # First, we need O(m⋅n) space to keep the keys for the log.
    # In addition, the worst space complexity of the Timsort algorithm is O(N), 
    # assuming that the space for each element is O(1). Hence we would need O(M⋅N) 
    # space to hold the intermediate values for sorting.
    
    # ref: https://leetcode.com/problems/reorder-data-in-log-files/solution/
