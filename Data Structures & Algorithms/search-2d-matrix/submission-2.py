class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1
        while top <=bottom:
            mid = (top+bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid -1
            else:
                break
            if not top <= bottom:
                return False
            
        row = (top + bottom) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row][mid_col] == target:
                return True
            elif target > matrix[row][mid_col]:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return False


        
        