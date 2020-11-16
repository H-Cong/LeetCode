from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # three ways to build a dict where the key is the word and value is the count of that word
        # 1.
        count = {}
        for word in words:
            if word in count: count[word] += 1
            else: count[word] = 1
        
        
        # 2. Use defaultdict
        # count = defaultdict(lambda:0) # this set the default val of the dict to be always 0
        #                              # count = defautdict(int) will do the same thing
        # for word in words:
        #     count[word] += 1
        # print(count)
        
        
        # 3. Use Counter
        # count = Counter(words)  # this will automatically generate a dict with key as word and val as count
        
        """
        Next we sort the key based on the value. We can do this in two ways. One is we generate a list with only
        keys (i.e. word) in it. Or we can generate a list of tuples to contain a (key, val) tuple as the list item
        """
        
        # 1. List of key
        candidates = list(count.keys()) # list(count) will do the same
        
        # then we sort this list based on the corresponding val of the dict
        # this is done using the inline lambda function
        # x is the value that the sort is based on. minus sign indicates the reverse order
        # so it will first sort candidates based on the corresponding dict value in reverse order
        # then it will sort the item in candidates in alphabetical order
        candidates.sort(key = lambda x:(-count[x], x))
        
        # then we return top k element of this candidates list
        return candidates[:k]
        
        # 2. List of key:val pairs
        # candidates = list(count.items()) # if you dont use .items() it will generate a list of keys
        
        # candidates.sort(key = lambda x:(-x[1], x[0])) # x[1] stands for the val, and x[0] is the key
        
        # return [item[0] for item in candidates[:k]]
        
        
        # TC: O(nlogn)
        # .sort() is a O(nlogn) operation. All other steps is O(n) I believe
        
        # SC: O(n)
        # this is for the dict space consuming
        
        
        """
        NOTE: The follwoing works in Python but not Python3
        
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
        """
        
