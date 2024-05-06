'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        check = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            check[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            check[len(word1)][j] = len(word2) - j
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    check[i][j] = check[i + 1][j + 1]
                else:
                    check[i][j] = 1 + min(check[i + 1][j + 1], check[i + 1][j], check[i][j + 1])
        return check[0][0]
    
'''
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''