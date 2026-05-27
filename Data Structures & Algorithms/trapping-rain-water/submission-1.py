class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        L, R = 0, len(height) - 1
        leftmax, rightmax = height[L], height[R]

        res = 0

        while L < R:
            if leftmax < rightmax:
                L += 1
                leftmax = max(leftmax, height[L])
                res += leftmax - height[L]
            else:
                R -= 1
                rightmax = max(rightmax, height[R])
                res += rightmax - height[R]
        return res