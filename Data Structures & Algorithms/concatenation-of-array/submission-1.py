class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [x for x in range(2*n)]
        for i in range(len(nums)):
            ans[i]  = nums[i] 
            ans[i+n] = nums[i]
        return ans
        