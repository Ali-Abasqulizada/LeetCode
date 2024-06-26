'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        ans = 0
        left, right = 0, 0
        while right < len(nums) - 1:
            longest = 0
            for i in range(left, right + 1):
                longest = max(i + nums[i], longest)
            left, right = right + 1, longest
            ans += 1
        return ans
    
#or

from functools import cache
class Solution:
    def jump(self, nums: list[int]) -> int:
        @cache
        def find(i):
            if i >= len(nums) - 1:
                return 0
            ans = float("inf")
            for j in range(i, i + nums[i]):
                ans = min(ans, 1 + find(j + 1))
            return ans
        return find(0)

'''
Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''