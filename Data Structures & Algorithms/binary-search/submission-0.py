class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                high -= 1
            elif nums[mid] < target:
                low += 1
            else:
                return mid
        return -1