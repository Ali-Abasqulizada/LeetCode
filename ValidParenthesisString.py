'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if not stack:
                    if count <= 0:
                        return False
                    count -= 1
                else:
                    stack.pop()
            else:
                count += 1
                star.append(i)
        while star and stack:
            if stack[-1] < star[-1]:
                star.pop()
                stack.pop()
            else:
                break
        return len(stack) == 0

#or

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for i in s:
            if i == "(":
                leftMin += 1
                leftMax += 1
            elif i == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            elif leftMin < 0:
                leftMin = 0
        return leftMin == 0

'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
'''