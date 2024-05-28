'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ""
        index = 0
        while index < len(s):
            if s[index] == " ":
                index += 1
            elif s[index] != "+" and s[index] != "-" and s[index] != "*" and s[index] != "/":
                num += s[index]
                index += 1
            elif s[index] == "+" or s[index] == "-":
                if num:
                    stack.append(int(num))
                    num = ""
                stack.append(s[index])
                index += 1
            else:
                newNum = ""
                ope = s[index]
                index += 1
                if not num:
                    num = stack.pop()
                while index < len(s) and (s[index] != "+" and s[index] != "-" and s[index] != "*" and s[index] != "/"):
                    newNum += s[index]
                    index += 1
                if ope == "*":
                    stack.append(int(num) * int(newNum))
                else:
                    stack.append(int(num) // int(newNum))
                num = ""
        if num:
            stack.append(int(num))
        ans = stack[0]
        for i in range(1, len(stack)):
            if stack[i] == "+":
                ans += stack[i + 1]
            elif stack[i] == "-":
                ans -= stack[i + 1] 
        return ans

'''
Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''