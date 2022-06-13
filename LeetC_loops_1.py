# 1822. Sign of the Product of an Array

'''
There is a function signFunc(x) that returns:

    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

 

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

 

Constraints:

    1 <= nums.length <= 1000
    -100 <= nums[i] <= 100
'''

import math

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = math.prod(nums)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
    def arraySign2(self, nums: list[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
    def arraySign3(self, nums: list[int]) -> int:
        res = 1
        
        for i in nums:
            res *= i
            
        if res < 0: return -1
        elif res == 0: return 0
        else: return 1
    def arraySign4(self, nums: list[int]) -> int:
        product = 1
        for i in nums:
            if i == 0:
                return 0
            else:
                product *= i
        if product > 0:
            return 1
        else:
            return -1
    def arraySign5(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                count += 1
        return 1 if count%2 == 0 else -1

    


print(Solution().arraySign5([-1,-2,-3,-4,3,2,1]))
print(Solution().arraySign5([1,5,0,2,-3]))
print(Solution().arraySign5([-1,1,-1,1,-1]))

