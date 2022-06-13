# 1281. Subtract the Product and Sum of Digits of an Integer

'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

 

Constraints:

    1 <= n <= 10^5

'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit = 0
        product_of_digits = 1
        sum_of_digits = 0
        while n>0:
            digit = n%10
            product_of_digits *= digit
            sum_of_digits += digit
            n //= 10
        return (product_of_digits - sum_of_digits)

    def subtractProductAndSum2(self, n: int) -> int:
        # convert integer to string, because in python strings are iterable
        num = str(n)
        product_of_digits = 1
        sum_of_digits = 0
        for i in num:
            product_of_digits *= int(i)
            sum_of_digits += int(i)
        return (product_of_digits - sum_of_digits)

print(Solution().subtractProductAndSum2(234))
print(Solution().subtractProductAndSum2(4421))