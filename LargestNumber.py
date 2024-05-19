'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def find(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        ans = sorted(nums, key = cmp_to_key(find))
        if ans[0] == "0":
            return "0"
        return "".join(ans)

'''
Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
'''