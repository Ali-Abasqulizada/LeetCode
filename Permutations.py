'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def count(cur, used):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                cur.append(nums[i])
                used[i] = True
                count(cur, used)
                cur.pop()
                used[i] = False
        count([], [False] * len(nums))
        return ans

'''
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
'''