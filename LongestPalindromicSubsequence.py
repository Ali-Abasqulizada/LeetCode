'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence 
by deleting some or no elements without changing the order of the remaining elements.
'''

from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def find(i, j):
            if j < i:
                return 0
            elif i == j:
                return 1
            elif s[i] == s[j]:
                return 2 + find(i + 1, j - 1)
            return max(find(i + 1, j - 1), find(i + 1, j), find(i, j - 1))
        return find(0, len(s) - 1)

#or

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        check = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i - 1] == t[j - 1]:
                    check[i][j] = 1 + check[i - 1][j - 1]
                else:
                    check[i][j] = max(check[i][j - 1], check[i - 1][j], check[i - 1][j - 1])
        return check[-1][-1]

#or

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        check = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s), 0, -1):
            for j in range(len(s), 0, -1):
                if s[i - 1] == t[j - 1]:
                    check[i - 1][j - 1] = 1 + check[i][j]
                else:
                    check[i - 1][j - 1] = max(check[i - 1][j], check[i][j - 1], check[i][j])
        return check[0][0]

'''
Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''