# 1768. Merge Strings Alternately

'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        index_w1 = 0
        index_w2 = 0
        l_w1, l_w2 = len(word1), len(word2)
        iterations = l_w1 + l_w2
        if l_w1 < l_w2:
            difference = l_w2 - l_w1
            iterations += difference
            # print(iterations)
        else:
            difference = l_w1 - l_w2
            iterations += difference
            # print(iterations)

        for i in range(iterations):
            if i%2 == 0:
                if index_w1 < l_w1:
                    merged_str += word1[index_w1]
                    index_w1 +=1
            else:
                if index_w2 < l_w2:
                    merged_str += word2[index_w2]
                    index_w2 +=1
        return merged_str
    def mergeAlternately2(self, word1: str, word2: str) -> str:
        merged_str = ""
        index_w1 = 0
        index_w2 = 0
        l_w1, l_w2 = len(word1), len(word2)
        iterations = l_w1 + l_w2
        for i in range(iterations):
            if i%2 == 0 and index_w1 < l_w1:
                merged_str += word1[index_w1]
                index_w1 +=1
            elif i%2 !=0 and index_w2 < l_w2:
                merged_str += word2[index_w2]
                index_w2 +=1
            elif index_w1 == l_w1:
                merged_str += word2[index_w2:]
                break
            elif index_w2 == l_w2:
                merged_str += word1[index_w1:]
                break
        return merged_str



print(Solution().mergeAlternately2("abc", "pqr"))
print(Solution().mergeAlternately2("ab", "pqrs"))
print(Solution().mergeAlternately2("abcd", "pq"))

