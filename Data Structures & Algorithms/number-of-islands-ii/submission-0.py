class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0]*n for _ in range(m)]

        res = []
        def helper(grid):
            count = 0
            visit = set()
            def find_islands(row, col):
                if row < 0 or col < 0 or row == m or col == n or grid[row][col] == 0 or (row, col) in visit:
                    return
                
                visit.add((row, col))

                find_islands(row-1, col)
                find_islands(row, col-1)
                find_islands(row+1, col)
                find_islands(row, col+1)
            
            for i in range(m):
                for j in range(n):
                    if (i,j) not in visit and grid[i][j] == 1:
                        find_islands(i,j)
                        count += 1
            return count


        for i,j in positions:
            grid[i][j] = 1
            res.append(helper(grid))
            

        return res