'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above 
(there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        @cache
        def find(i):
            if i >= len(s):
                return 1
            ans = 0
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                ans += find(i + 2)
            if s[i] != "0":
                ans += find(i + 1)
            return ans 
        return find(0)

#or

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        @cache
        def find(i):
            if i < 0:
                return 1
            ans = 0
            if i > 0 and (s[i - 1] == "1" or s[i - 1] == "2" and s[i] in "0123456"):
                ans += find(i - 2)
            if s[i] != "0":
                ans += find(i - 1)
            return ans 
        return find(len(s) - 1)

#or

class Solution:
    def numDecodings(self, s: str) -> int:
        left, right = 0, 1
        for i in range(len(s)):
            ans = 0
            if i > 0 and (s[i - 1] == "1" or s[i - 1] == "2" and s[i] in "0123456"):
                ans += left
            if s[i] != "0":
                ans += right
            left, right = right, ans
        return right

'''
Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
'''