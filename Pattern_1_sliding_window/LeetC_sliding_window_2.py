# 643. Maximum Average Subarray I

'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

'''


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_average = -9999999
        if len(nums) == 1:
            return sum(nums)/1.00000
        for i in range(0,len(nums)-k+1):
            sub_arr = []
            for j in range(i, i+k):
                sub_arr.append(nums[j])
                # print(sub_arr)
            average_sub_arr = sum(sub_arr)/k
            if average_sub_arr > max_average:
                max_average = average_sub_arr
        return max_average
    
    def findMaxAverage2(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[0:k]) # find sum of the first window
        # print(current_sum)
        max_sum = current_sum # set the max value to the first sum
        for i in range(k,len(nums)): 
            current_sum += nums[i] - nums[i-k]
            print(current_sum)

            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum/k

print(Solution().findMaxAverage2([1,12,-5,-6,50,3], 4))
# print(Solution().findMaxAverage2([5], 1))