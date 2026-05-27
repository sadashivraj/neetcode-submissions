class Solution:
    def removeDuplicates(self, nums: List[int]) -> int: 
        l = 1  # position to place next unique element
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l