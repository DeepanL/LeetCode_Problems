# 2269. Find the K-Beauty of a Number

'''
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.
 

Constraints:

1 <= num <= 109
1 <= k <= num.length (taking num as a string)
'''

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_string = str(num)
        k_beauty = 0
        for i in range(len(num_string)):
            if i+k > len(num_string):
                return k_beauty
            else:
                sub_string = int(num_string[i:i+k])
                # print(sub_string)
                if sub_string == 0:
                    continue
                elif num % sub_string == 0:
                    k_beauty += 1
        return k_beauty

print(Solution().divisorSubstrings(30003,3))
print(Solution().divisorSubstrings(240,2))
print(Solution().divisorSubstrings(430043,2))