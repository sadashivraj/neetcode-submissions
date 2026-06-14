from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0           
        
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                delta = [(-1,0), (1,0), (0, -1), (0,1)]
                for dr, dc in delta:
                    if r+dr < 0 or c+dc <0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc]!=1:
                        continue
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    q.append((r+dr, c+dc))
            minutes += 1

        return minutes if fresh == 0 else -1