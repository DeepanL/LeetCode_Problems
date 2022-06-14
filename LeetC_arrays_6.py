# 896. Monotonic Array

'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:

Input: nums = [1,2,2,3]
Output: true

Example 2:

Input: nums = [6,5,4,4]
Output: true

Example 3:

Input: nums = [1,3,2]
Output: false

'''

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        flag_increasing = True
        flag_decreasing = True

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                # flag_increasing = True
                flag_decreasing = False
                # print(flag_increasing, flag_decreasing)
            if nums[i] > nums[i+1]:
                # flag_increasing = False
                flag_increasing = False
                # print(flag_increasing, flag_decreasing)
        # print(flag_increasing, flag_decreasing)
        if flag_increasing == True and flag_decreasing == False:
            return True
        elif flag_increasing == False and flag_decreasing == True:
            return True
        elif flag_increasing == True and flag_decreasing == True:
            return True
        else:
            return False
    def isMonotonic2(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        d = nums[0] - nums[n-1]

        if d > 0:
            for i in range(n-1):
                if nums[i] < nums[i+1]:
                    return False
        elif d < 0:
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(n-1):
                if nums[i] != nums[i+1]:
                    return False

        return True


print(Solution().isMonotonic([1,2,2,3]))
print(Solution().isMonotonic([6,5,4,4]))
print(Solution().isMonotonic([1,3,2]))
print(Solution().isMonotonic([1,1,1]))
print(Solution().isMonotonic2([1,2,4,5]))





