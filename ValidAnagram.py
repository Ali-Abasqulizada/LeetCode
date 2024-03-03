'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = [0] * 26
        for i in s:
            ans[ord(i) - ord("a")] += 1
        for j in t:
            if ans[ord(j) - ord("a")] == 0:
                return False
            ans[ord(j) - ord("a")] -= 1
        return True
    
#or
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t

'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
'''