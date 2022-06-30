# 219. Contains Duplicate II

'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # check if there are duplicates in the list at all
        if len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False
    
    def containsNearbyDuplicate2(self, nums: list[int], k: int) -> bool:
        # check if there are duplicates in the list at all
        if len(set(nums)) == len(nums):
            return False
        
        window = {} # create a dictionary
        for i in range(len(nums)):
            #check if value is not in dictionary
            if nums[i] not in window:
                # create a key using the value nums[i] and set the value of the key to index i
                window[nums[i]] = i
                print(window)
            else:
                # if value is in dictionary subtract the current index with the value of key and check condition
                if abs(i - window[nums[i]]) <= k:
                    return True
                # keep creating key value pairs as iterating through nums
                window[nums[i]] = i
        return False

    def containsNearbyDuplicate3(self, nums: list[int], k: int) -> bool:
        # check if there are duplicates in the list at all
        if len(set(nums)) == len(nums):
            return False
        
        window = {} # create a dictionary
        for i in range(len(nums)):
            #check if value is not in dictionary
            if nums[i] in window and abs(i - window[nums[i]]) <= k:
                return True
            window[nums[i]] = i
            #     # create a key using the value nums[i] and set the value of the key to index i
            #     window[nums[i]] = i
            #     print(window)
            # else:
            #     # if value is in dictionary subtract the current index with the value of key and check condition
            #     if abs(i - window[nums[i]]) <= k:
            #         return True
            #     # keep creating key value pairs as iterating through nums
            #     window[nums[i]] = i
        return False


print(Solution().containsNearbyDuplicate3([1,2,3,1], 3))
print(Solution().containsNearbyDuplicate3([1,0,1,1], 1))
print(Solution().containsNearbyDuplicate3([1,2,3,1,2,3], 2))




