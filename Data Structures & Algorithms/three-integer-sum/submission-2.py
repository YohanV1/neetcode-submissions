class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for index, num in enumerate(nums):
            l = index+1
            r = len(nums)-1
            
            while l<r:
                cur_sum = num + nums[l] + nums[r]
                if cur_sum > 0:
                    r-=1
                elif cur_sum < 0:
                    l+=1
                else:
                    if [num, nums[l], nums[r]] not in res:
                        res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
        return res
                    
                    


        