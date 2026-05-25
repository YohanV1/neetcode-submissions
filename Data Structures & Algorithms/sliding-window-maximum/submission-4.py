class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k>len(nums):
            return []
        if k==len(nums):
            return [max(nums)]
        res = []
        for i in range(len(nums)):
            if i + k - 1 < len(nums):
                res.append(max(nums[i:i+k]))
        return res
        