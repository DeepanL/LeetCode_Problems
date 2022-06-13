# 1790. Check if One String Swap Can Make Strings Equal

'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 

Constraints:

    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.
'''


# Hint 1: The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
# Hint 2: Check that these positions have the same set of characters.
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # according to constraints length of s1 always equal to s2
        count = 0
        swap_s1 = []
        swap_s2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                # if count = 0 then all characters are identical
                count += 1
                # store the characters that are non identical
                swap_s1.append(s1[i])
                swap_s2.append(s2[i])
        print(swap_s1, swap_s2)
        if count == 0:
            return True
            # check if the charcaters in the lists are identical
        if count == 2 and swap_s1[0] == swap_s2[1] and swap_s1[1] == swap_s2[0]:
            return True
        else:
            return False

    def areAlmostEqual2(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        a1, b1, a2, b2 = None, None, None, None
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if count == 0:
                    a1 = s1[i]
                    b1 = s2[i]
                    count += 1
                elif count == 1:
                    a2 = s1[i]
                    b2 = s2[i]
                    count += 1
                    if a1 == b2 and a2 == b1:
                        continue
                    else:
                        return False
                else:
                    return False
        return count == 2


print(Solution().areAlmostEqual2("bank", "kanb"))
print(Solution().areAlmostEqual2("attack", "defend"))  # should give false
print(Solution().areAlmostEqual2("kelb", "kelb"))
