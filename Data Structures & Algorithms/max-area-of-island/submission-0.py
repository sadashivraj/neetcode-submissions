class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        visit = set()
        max_area = 0

        def dfs(row, col):
            if min(row, col)<0 or row==ROWS or col == COLS or (row,col) in visit or grid[row][col]==0:
                return 0
            
            visit.add((row,col))
            area = 1
            area+=dfs(row + 1, col)
            area+=dfs(row - 1, col)
            area+=dfs(row, col + 1)
            area+=dfs(row, col - 1)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    max_area = max(max_area,area)
        
        return max_area

