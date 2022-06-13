# 953. Verifying an Alien Dictionary

'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.



'''
# worldabcefghijkmnpqstuvxyz

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        for i in range(len(words)-1):
            word1=words[i]
            j=len(word1)
            word2=words[i+1]
            k=len(word2)
            l=min(j,k)
            n=0
            
            while n<l:
                if order.index(word1[n])>order.index(word2[n]):
                    return False
                elif order.index(word1[n])<order.index(word2[n]):
                    break
                else:
                    n+=1
                if j>k and n==l:
                    return False
        return True


print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))