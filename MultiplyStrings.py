'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return '0'
        stack = []
        for i in range(len(num1) - 1, -1, -1):
            num = ""
            carry = 0
            ni = int(num1[i])
            for j in range(len(num2) - 1, -1, -1):
                nj = int(num2[j])
                helper = ni * nj + carry
                num += str(helper % 10)
                carry = helper // 10
            if carry:
                num += str(carry)
            stack.append(num)
        c = 1
        for i in range(1, len(stack)):
            num1 = stack[i - 1][c :]
            num2 = stack[i]
            l, r, carry = 0, 0, 0
            ans = stack[i - 1][0:c]
            while l < len(num1) or r < len(num2) or carry:
                n1 = int(num1[l]) if l < len(num1) else 0
                n2 = int(num2[r]) if r < len(num2) else 0
                total = n1 + n2 + carry
                ans += str(total % 10)
                carry = total // 10
                l += 1
                r += 1
            stack[i] = ans
            c += 1
        return stack[-1][::-1]

'''
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''