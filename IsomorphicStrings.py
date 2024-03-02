'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check1 = {}
        check2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in check1:
                check1[s[i]] += i
            else:
                check1[s[i]] = i
            if t[i] in check2:
                check2[t[i]] += i
            else:
                check2[t[i]] = i
        for i in range(len(s)):
            if check1[s[i]] != check2[t[i]]:
                return False
        return True
    
#or
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

'''
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
'''