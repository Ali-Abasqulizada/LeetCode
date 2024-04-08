'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
'''

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        ans = []
        check = {}
        for n in nums:
            check[n] = check.get(n, 0) + 1
        for n in check:
            if check[n] > len(nums) // 3:
                ans.append(n)
        return ans
    
'''
Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]
'''