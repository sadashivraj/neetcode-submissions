class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        total = 0
        min_size = float("inf")
        for R in range(0, len(nums)):
            total += nums[R]
            while total >=target:
                min_size = min(R-L+1, min_size)
                total -= nums[L]
                L+=1
        return 0 if min_size == float("inf") else min_size

