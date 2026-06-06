class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1

        if len(nums) == 1 and nums[0]==target:
            return 0
        elif len(nums) == 1 and nums[0]!=target:
            return -1
        
        
        while L<=R:
            mid = (L+R)//2
            if nums[mid] == target:
                return mid
            
            # Identify which side is sorted
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1