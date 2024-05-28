from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def find(i, j, k):
            if i >= len(s1) and j >= len(s2) and k >= len(s3):
                return True
            if i < len(s1) and s1[i] == s3[k]:
                if find(i + 1, j, k + 1):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if find(i, j + 1, k + 1):
                    return True
            return False
        return find(0, 0, 0)
    
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        check = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        check[-1][-1] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and check[i + 1][j]:
                    check[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and check[i][j + 1]:
                    check[i][j] = True
        return check[0][0]