class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix, postfix = 1,1

        for i in range(len(nums)):
            res[i] = prefix # [1, 1, 2, 8]
            prefix*=nums[i]  # prefix = 8

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res