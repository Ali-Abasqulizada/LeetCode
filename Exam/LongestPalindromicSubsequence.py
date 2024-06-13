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