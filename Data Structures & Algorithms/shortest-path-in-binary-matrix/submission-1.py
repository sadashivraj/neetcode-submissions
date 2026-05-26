class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Initialisation
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        if N == 1:
            return 1

        ROWS , COLS = len(grid), len(grid[0])
        queue = deque()
        queue.append((0,0, 1))
        visit = set()
        visit.add((0,0))

        while queue:
            r,c, length = queue.popleft()

            if r == ROWS-1 and c == COLS -1:
                return length

            neighbours = [[0,1],[0,-1],[1,0],[-1,0],[1,1], [1,-1], [-1,1], [-1,-1]]

            for dr, dc in neighbours:
                new_x, new_y = r+dr, c+dc

                if min(new_x, new_y)< 0 or (new_x, new_y) in visit or new_x == ROWS or new_y == COLS or grid[new_x][new_y] == 1:
                    continue
                queue.append((new_x, new_y, length + 1))
                visit.add((new_x, new_y))
            
        return -1