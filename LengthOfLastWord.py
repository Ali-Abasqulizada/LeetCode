'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])
    
#or
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            ans += 1
            i -= 1
        return ans 
    
#or

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reach = False
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and not reach:
                continue
            elif s[i] != " ":
                count += 1
                reach = True
            else:
                break
        return count

'''
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''