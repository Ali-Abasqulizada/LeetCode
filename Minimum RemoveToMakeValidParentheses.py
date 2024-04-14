'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting 
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = [i for i in s]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")":
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()
        for i in stack:
            s[i[1]] = ""
        return "".join(s)

'''
Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''