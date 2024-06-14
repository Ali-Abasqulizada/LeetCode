'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.
'''

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        ans = 0
        for i in range(mid):
            ans += nums[mid] - nums[i]
        for i in range(mid + 1, len(nums)):
            ans += nums[i] - nums[mid]
        return ans

'''
Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16
'''