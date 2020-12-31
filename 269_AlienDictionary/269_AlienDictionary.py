from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Topological Sorting / BFS
        '''
    
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                            
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # else will only be executed if for loop runs out without hitting break clause
                if len(second_word) < len(first_word): return ""

        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        if len(output) < len(in_degree):
            return ""
       
        return "".join(output)
    
    # TC: O(C)
    # Let C be the total length of all the words in the input list, added together.
    
    # SC: O(1) or O(U + min(U^2, N))
    # Let N be the total number of strings in the input list.
    # Let UU be the total number of unique letters in the alien alphabet. 
    
    # NOTE: for/else clause: https://book.pythontips.com/en/latest/for_-_else.html
    
    # ref: https://leetcode.com/problems/alien-dictionary/solution/
