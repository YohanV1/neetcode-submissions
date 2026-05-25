import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 0
        outputs = []
        for index in range(len(nums)):
            pre, suf = 1,1
            print("---", nums[index])
            for j in nums[0:index]:
                pre *= j
            print("prefix", pre)
            for j in nums[index+1:len(nums)+1]:
                suf *= j
            print("suffix", suf)
            outputs.append(pre*suf)
        return outputs

        