'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = [0] * 26
        for i in magazine:
            check[ord(i) - ord("a")] += 1
        for i in ransomNote:
            if check[ord(i) - ord("a")] == 0:
                return False
            else:
                check[ord(i) - ord("a")] -= 1
        return True

#or
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
    
'''
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''