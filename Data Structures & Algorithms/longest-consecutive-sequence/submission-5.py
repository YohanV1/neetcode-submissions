class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_c = 1

        for num in nums:
            if num - 1 not in nums_set:
                cur = num
                counter = 1
                while cur + 1 in nums_set:
                    counter += 1
                    cur += 1
                max_c = max(max_c, counter)
        
        return max_c