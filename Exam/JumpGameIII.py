class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visit = set()
        def find(i):
            if i >= len(arr) or i < 0:
                return False
            if i in visit:
                return False
            visit.add(i)
            if arr[i] == 0:
                return True
            return find(i + arr[i]) or find(i - arr[i])
        return find(start)