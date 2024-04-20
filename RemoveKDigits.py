'''
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k > 0 and stack[-1] > n:
                k -= 1
                stack.pop()
            if stack or n != "0":
                stack.append(n)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack) if stack else "0"
    
'''
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''