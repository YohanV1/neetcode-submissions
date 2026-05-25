import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        copy = nums.copy()
        for index, i in enumerate(copy):
            copy[index] = 1
            l.append(copy)
            print(l)
            copy=nums.copy()
        res = []
        for numbers in l:
            res.append(math.prod(numbers))
        return res


        