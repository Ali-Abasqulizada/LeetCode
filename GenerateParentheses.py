'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def find(s, left, right):
            if left == 0 and right == 0:
                ans.append(s)
            if left > 0:
                find(s + "(", left - 1, right)
            if left < right and right > 0:
                find(s + ")", left, right - 1)
        find("", n, n)
        return ans
    
'''
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
'''