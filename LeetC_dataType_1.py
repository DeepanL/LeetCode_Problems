#1523. Count Odd Numbers in an Interval Range
'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
    0 <= low <= high <= 10^9
'''




class Solution:
    # Solution @1
    def countOdds(self, low: int, high: int) -> int:
        count_odd_num = 0
        range = high - low + 1
        if range%2 == 0:
            count_odd_num = range //2
        elif high%2 == 0:
            count_odd_num = range//2
        else:
            count_odd_num = range//2 +1
        return count_odd_num
    # Solution @2
    def countOdds2(self, low: int, high: int) -> int:
        if low%2==0:
            low+=1
        return int((high-low)/2+1)

print(Solution().countOdds(3, 7))
print(Solution().countOdds2(8,10))
