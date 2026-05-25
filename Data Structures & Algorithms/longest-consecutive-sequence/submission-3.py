class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = []
        starting_points = []
        nums_set = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                starting_points.append(nums[i])
        counter = 1
        i = 0
        if len(nums)==0:
            max_counter = 0
        else:
            max_counter = 1
        print(starting_points)
        while i<len(starting_points):
            if (starting_points[i] + 1) not in nums_set:
                i+=1
                counter=1
            else:
                starting_points[i] = starting_points[i] + 1
                counter+=1
                if counter > max_counter:
                    max_counter = counter
        return max_counter
            
        


            

        




            
        
        