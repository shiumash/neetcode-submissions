class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if  orig == color:
            return image
        
        m, n = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque([(sr, sc)])

        while q:
            image[sr][sc] = color
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == orig:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image
