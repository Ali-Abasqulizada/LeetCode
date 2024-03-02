'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            if i in "({[":
                check.append(i)
            elif i in ")}]" and not check:
                return False
            elif i == ")" and check[-1] != "(":
                return False
            elif i == "}" and check[-1] != "{":
                return False
            elif i == "]" and check[-1] != "[":
                return False
            else:
                check.pop()
        if not check:
            return True
        return False
    
'''
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
'''