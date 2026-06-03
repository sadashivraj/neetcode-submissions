class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <=1:
            return len(nums)

        nums = sorted(list(set(nums)))
        max_len = 0
        ptr = 1
        curr = 0
        while ptr < len(nums):
            if nums[ptr] - nums[ptr-1] == 1:
                pass
            else:
                max_len = max(max_len, (ptr-curr))
                curr = ptr
            ptr+=1
        max_len = max(max_len, (ptr-curr))
        return max_len
