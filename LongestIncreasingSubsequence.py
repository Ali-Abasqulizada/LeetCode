'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''

from functools import cache
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        @cache
        def find(i, index):
            if i >= len(nums):
                return 0
            ans = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[index]:
                    ans = max(ans, 1 + find(j + 1, j))
            return ans
        check = 0
        for i in range(len(nums)):
            check = max(check, 1 + find(i, i))
        return check

'''
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''