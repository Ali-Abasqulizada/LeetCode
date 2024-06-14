class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        ans = [intervals[0]]
        for l, r in intervals[1:]:
            pl, pr = ans[-1]
            if pr < l:
                ans.append([l, r])
            elif r >= pr:
                ans[-1] = [pl, r]
        return ans