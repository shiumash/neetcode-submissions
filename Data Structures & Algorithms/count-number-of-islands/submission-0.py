class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    res += 1
                    grid[row][col] = "0"
                    q.append((row, col))

                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
        
        return res

