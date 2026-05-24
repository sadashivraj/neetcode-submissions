class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = 0
        for i in range(0, len(arr)):
            if i == 0:
                cur_max = arr[len(arr)-1-i]
                arr[len(arr)-1-i] = -1
            else:
                temp = cur_max
                cur_max = max(cur_max, arr[len(arr)-1-i])
                arr[len(arr)-1-i] = temp
        return arr
        