# 1502. Can Make Arithmetic Progression From Sequence

'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:

    2 <= arr.length <= 1000
    -106 <= arr[i] <= 106


'''


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr_ascending = sorted(arr)
        arr_descending = sorted(arr, reverse=True)
        diff_ascending = arr_ascending[1] - arr_ascending[0]
        diff_descending = arr_descending[1] - arr_descending[0]
        arr_length = len(arr)
        flag = 0
        for i in range(arr_length-1):
            if (arr_ascending[i+1] - arr_ascending[i]) != diff_ascending:
                flag = 1
                break
            if (arr_descending[i+1] - arr_descending[i]) != diff_descending:
                flag = 1
                break
        if flag == 1:
            return False
        else:
            return True
    def canMakeArithmeticProgression2(self, arr: list[int]) -> bool:
        arr_sorted = sorted(arr)
        for i in range(len(arr) - 1):
            # we check the absolute difference between consecutive elements and compare with the difference 
            # of the first two elements
            # because if we sort ascending or descending the absolute difference will remain the same so we need to check only one way
            if abs(arr_sorted[i+1] - arr_sorted[i]) != abs(arr_sorted[1] - arr_sorted[0]):
                return False
        return True




print(Solution().canMakeArithmeticProgression2([3,5,1]))
print(Solution().canMakeArithmeticProgression2([1,2,4]))

        

