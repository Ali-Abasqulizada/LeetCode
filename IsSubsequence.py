'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS, lenT = len(s), len(t)
        i = j = 0
        while i < lenS and j < lenT:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == lenS
    
#or
    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        index = 0
        for i in t:
            if s[index] == i:
                index += 1
                if index == len(s):
                    return True
        return False
    
'''
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''