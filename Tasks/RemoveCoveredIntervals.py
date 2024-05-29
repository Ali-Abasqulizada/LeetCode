class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        ans = [intervals[0]]
        for left, right in intervals[1:]:
            prevL, prevR = ans[-1]
            if prevL <= left and right <= prevR:
                continue
            ans.append((left, right))
        return len(ans)