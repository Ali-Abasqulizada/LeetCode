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