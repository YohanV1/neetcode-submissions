class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difs = {}
        for index, i in enumerate(numbers):
            dif = target - i
            if i in difs:
                return [difs[i]+1, index+1]
            else:
                difs[dif] = index            


        