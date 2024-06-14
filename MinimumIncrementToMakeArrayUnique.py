'''
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i] += 1
                ans += 1
            elif nums[i - 1] > nums[i]:
                ans += (nums[i - 1] - nums[i] + 1)
                nums[i] += (nums[i - 1] - nums[i] + 1)
        return ans

'''
Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
'''