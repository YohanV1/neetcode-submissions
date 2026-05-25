class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        half = sum(nums)//2

        memo = {}

        def dfs(i, curSum):
            if curSum == half:
                return True
            if curSum > half or i>= len(nums):
                return False
            if (i, curSum) in memo:
                return memo[(i, curSum)]
            found = dfs(i+1, curSum + nums[i]) or dfs(i+1, curSum)
            memo[(i, curSum)] = found
            return found

        return dfs(0,0)





        