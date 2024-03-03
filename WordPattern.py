'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(set(s)) != len(set(pattern)) or len(s) != len(pattern):
            return False
        check = {}
        for i in range(len(pattern)):
            if pattern[i] in check and check[pattern[i]] != s[i]:
                return False
            else:
                check[pattern[i]] = s[i]
        return True

'''
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''