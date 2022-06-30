# 1763. Longest Nice Substring

'''
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        #minimum length of substring is 2
        nice_string = ''                    
        if len(s) < 2:
            return nice_string
        elif len(s) == 2:
            if ord(s[0]) + 32 == ord(s[1]) or ord(s[1]) + 32 == ord(s[0]):
                nice_string = s
        else:
            print(checkNiceSubstring(s))
            

        return nice_string
    
    def longestNiceSubstring2(self, s: str) -> str:
        # First check length of string if less than 2 or 0 immediately return
        if len(s)==1 or len(s)==0:
            return "" 
        nice=""
        for window in range(2,len(s)+1):
            for i in range(len(s)-window+1):
                string=s[i:window+i]
                print(string)
                s1=set(string)
                s2=set(string.swapcase())
                s1=s1-s2
                if len(s1)==0:
                    if len(nice)<len(string):
                        nice=string
                
        return nice


print(Solution().longestNiceSubstring2("YazaAay"))