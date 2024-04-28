'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        def find(cur, start):
            ans.add(tuple(sorted(cur[:])))
            for i in range(start, len(nums)):
                cur.append(nums[i])
                find(cur, i + 1)
                cur.pop()
        find([], 0)
        return list(ans)
    
'''
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
'''