class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        we can assume we're provided a non zero grid
        multi source BFS
        -------
        init deque q
        fresh = 0
        time = 0

        iterate through the whole grid and enque the positions of containmented items, also keep track of fresh fruit

        while queue
            time += 1
            iterate through index of queue # ensures multi source
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if not valid:
                        continue
                    grid[nr][nc] = 2
                    q.append((nc, nc))
                    fresh -= 1

        return time if fresh == 0 else -1
        '''
        q = deque()
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not 0 <= nr < rows or not 0 <= nc < cols or not grid[nr][nc] == 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1

        return time if fresh == 0 else -1