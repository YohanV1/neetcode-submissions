class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_counter = 1

        for num in nums:
            if num - 1 not in nums_set:  # start of a sequence
                cur = num
                counter = 1
                while cur + 1 in nums_set:
                    cur += 1
                    counter += 1
                max_counter = max(max_counter, counter)

        return max_counter
