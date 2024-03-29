'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval 
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still 
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
'''

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        ans = []
        for ele in intervals:
            if ele[1] < newInterval[0]:
                ans.append(ele)
            elif ele[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = ele
            elif ele[1] >= newInterval[1] or ele[0] <= newInterval[1]:
                newInterval[0] = min(ele[0], newInterval[0])
                newInterval[1] = max(ele[1], newInterval[1])
        ans.append(newInterval)
        return ans
    
'''
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''