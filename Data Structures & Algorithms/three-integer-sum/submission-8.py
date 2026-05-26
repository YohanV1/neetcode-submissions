class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # [-4, -1, -1, 0, 1, 2]
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                    continue
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                    continue
                while l+1 in range(len(nums)) and nums[l] == nums[l+1]:
                    l += 1
                while r-1 in range(len(nums)) and nums[r] == nums[r-1]:
                    r -= 1
                l+=1
                r-=1

        return res

