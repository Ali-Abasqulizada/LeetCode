'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= ans[-1][0] and intervals[i][0] <= ans[-1][1] and intervals[i][1] >= ans[-1][1]:
                ele = ans.pop()
                ele[1] = intervals[i][1]
                ans.append(ele)
            elif intervals[i][0] >= ans[-1][0] and intervals[i][0] <= ans[-1][1] and intervals[i][1] < ans[-1][1]:
                continue
            elif ans[-1][0] >= intervals[i][0] and ans[-1][0] <= intervals[i][1] and ans[-1][1] >= intervals[i][1]:
                ele = ans.pop()
                ele[0] = intervals[i][0]
                ans.append(ele)
            elif ans[-1][0] >= intervals[i][0] and ans[-1][0] <= intervals[i][1] and ans[-1][1] < intervals[i][1]: 
                ans.pop()
                ans.append(intervals[i])
            else:
                ans.append(intervals[i])
        return ans

#or

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]
        for l, r in intervals[1:]:
            pl, pr = ans[-1]
            if l <= pr and r <= pr:
                continue
            elif l <= pr:
                ans.pop()
                ans.append([pl, r])
            else:
                ans.append([l, r])
        return ans

#or

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        def find(i, ans):
            if i >= len(intervals):
                return ans
            l, r = intervals[i]
            pl, pr = ans[-1]
            if pr < l:
                ans.append([l, r])
            elif pr <= r:
                ans.pop()
                ans.append([pl, r])
            return find(i + 1, ans)
        return find(1, [intervals[0]])

'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''