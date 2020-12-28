class Trie:
    '''
    Hashtable in Hashtable
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['#'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.find(word)
        return p is not None and '#' in p

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return True if self.find(prefix) else False
    
    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]
        
        return p


    # TC: O(l) where l is the length of the word
    
    # SC: O(n*l_ave) 
    # worst case there are n words with average length l_ave without sharing any prefix
    
    # ref: http://zxi.mytechroad.com/blog/data-structure/leetcode-208-implement-trie-prefix-tree/
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
