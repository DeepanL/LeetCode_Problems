# 976. Largest Perimeter Triangle

'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

Input: nums = [2,1,2]
Output: 5

Example 2:

Input: nums = [1,2,1]
Output: 0

 

Constraints:

    3 <= nums.length <= 104
    1 <= nums[i] <= 106

'''

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        '''
        The three edges of triangle need to satisfy the following rules:
        1. the sum of any two of them is larger than the 3rd edge -> shortest edge + mid edge > longest edge
        2. the subtraction of any two of them is smaller than the 3rd edge  -> (longest edge - shortest edge) < mid edge
        '''
        sorted_sides = sorted(nums, reverse = True)
        # print(nums[0] + nums[1])
        # print(nums[0] + nums[2])
        perimeter = 0
        for i in range(len(nums)-2):
            side_1 = sorted_sides[i]
            side_2 = sorted_sides[i+1]
            side_3 = sorted_sides[i+2]
            if side_3 + side_2 > side_1 and side_1 - side_3 < side_2:
                perimeter = side_1 + side_2 + side_3

        return perimeter

    def largestPerimeter(self, nums: list[int]) -> int:  
        nums_sorted = sorted(nums,reverse=True)
        perimeter = 0
        for i in range(len(nums_sorted)-2):
            longest_edge = nums_sorted[i]
            mid_edge = nums_sorted[i+1]
            shortest_edge = nums_sorted[i+2]
            if mid_edge+shortest_edge>longest_edge and longest_edge-shortest_edge<mid_edge:
                perimeter = longest_edge + mid_edge + shortest_edge
                break
            
        return perimeter

    def largestPerimeter2(self, nums: list[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)-1,1,-1):
        #     if nums[i-1]+nums[i-2]>nums[i] and nums[i] - nums[i-2]<nums[i-1]:
        #         return nums[i] + nums[i-1] + nums[i-2]
        # return 0
        # sorted_nums = sorted(nums, reverse=True)
        # for i in range(len(nums)-2):
        #     if sorted_nums[i+1]+sorted_nums[i+2]>sorted_nums[i] and sorted_nums[i] - sorted_nums[i+2]<sorted_nums[i+1]:
        #         return sorted_nums[i] + sorted_nums[i+1] + sorted_nums[i+2]
        # return 0
        #Fastest solution
        sorted_nums = sorted(nums)
        for i in range(len(nums)-1,1,-1):
            if sorted_nums[i-1]+sorted_nums[i-2]>sorted_nums[i] and sorted_nums[i] - sorted_nums[i-2]<sorted_nums[i-1]:
                return sorted_nums[i] + sorted_nums[i-1] + sorted_nums[i-2]
        return 0


print(Solution().largestPerimeter2([2,1,2]))
print(Solution().largestPerimeter2([1,2,1]))
