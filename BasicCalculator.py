'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''

class Solution:
    def calculate(self, s: str) -> int:
        def find(index):
            stack = []
            num = 0
            sign = 1
            while index < len(s):
                digit = s[index]
                if digit.isdigit():
                    num = num * 10 + int(digit)
                elif digit == "+":
                    stack.append(sign * num)
                    num = 0
                    sign = 1
                elif digit == "-":
                    stack.append(sign * num)
                    num = 0
                    sign = -1
                elif digit == "(":
                    num, index = find(index + 1)
                    num *= sign
                    sign = 1
                elif digit == ")":
                    stack.append(sign * num)
                    return sum(stack), index
                index += 1
            stack.append(sign * num)
            return sum(stack), index
        return find(0)[0]

'''
Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''