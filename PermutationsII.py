'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def count(cur, used):
            if len(cur) == len(nums):
                if cur[:] not in ans:
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

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''