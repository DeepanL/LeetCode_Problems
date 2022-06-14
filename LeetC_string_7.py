# 28. Implement strStr()

'''
Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                haystack_index = i
                check = 0
                for j in range(len(needle)):
                    # print(haystack_index, j)
                    if haystack_index < len(haystack):
                        if haystack[haystack_index] == needle[j]:
                            check += 1
                        else:
                            break
                    # if haystack_index < len(haystack):
                        haystack_index += 1
                    else:
                        break
                if check == len(needle):
                    return i
                else:
                    continue
        return -1
    def strStr2(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                check_str = haystack[i:i+len(needle)]
                if check_str == needle:
                    return i
                # print(check_str)
        return -1


print(Solution().strStr2("hello", "ll"))
print(Solution().strStr("aaaaa", ""))
print(Solution().strStr2("mississippi", "issipi"))



                