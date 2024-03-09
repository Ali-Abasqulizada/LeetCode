'''
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        ia, ib = len(a) - 1, len(b) - 1
        carry = 0
        while ia >= 0 or ib >= 0 or carry:
            va = int(a[ia]) if ia >= 0 else 0
            vb = int(b[ib]) if ib >= 0 else 0
            total = va + vb + carry
            ans = str(total % 2) + ans
            carry = total // 2
            ia -= 1
            ib -= 1
        return ans

'''
Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''