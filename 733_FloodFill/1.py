class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        '''
        BFS
        '''
        if not image or not image[0]: return None
        q = deque()
        r, c, v = len(image), len(image[0]), image[sr][sc]
        if v == newColor: return image
        q.append((sr, sc))
        while q:
            x, y = q.popleft()
            image[x][y] = newColor
            directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for a, b in directions:
                if 0 <= a < r and 0 <= b < c and image[a][b] == v:
                    q.append((a, b))
        
        return image
    
    # TC: O(mn)
    
    # SC: O(mn)
                    
        
        
