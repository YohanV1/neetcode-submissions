class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            if index>0 and num==nums[index-1]:
                continue
            l = index+1
            r = len(nums)-1
            
            while l<r:
                cur_sum = num + nums[l] + nums[r]
                if cur_sum > 0:
                    r-=1
                elif cur_sum < 0:
                    l+=1
                else:
                    res.append([num, nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res
                    
                    


        