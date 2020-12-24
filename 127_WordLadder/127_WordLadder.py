class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        BFS
        '''
        if not endWord or not beginWord or not wordList or endWord not in wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for w in wordList:
            for i in range(L):
                all_combo_dict[w[:i]+'*'+w[i+1:]].append(w)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            curr_w, level = queue.popleft()
            for i in range(L):
                intermidiate_w = curr_w[:i]+'*'+curr_w[i+1:]
                
                for w in all_combo_dict[intermidiate_w]:
                    if w == endWord: return level + 1
                    if w not in visited:
                        visited[w] = True
                        queue.append((w, level+1))
                all_combo_dict[intermidiate_w] = [] # optional. dont know why this line
        
        return 0
    
    # TC: O(m^2*n) where m is the length of each word and n is total number of words in wordDict
    
    # SC: O(m^2*n)
    
    # ref: https://leetcode.com/problems/word-ladder/solution/
