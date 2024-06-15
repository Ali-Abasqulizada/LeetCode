class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        check = {cor : [] for cor in range(numCourses)}
        for cor, pre in prerequisites:
            check[cor].append(pre)
        ans, visit, cycle = [], set(), set()
        def find(cor):
            if cor in cycle:
                return False
            elif cor in visit:
                return True
            cycle.add(cor)
            for pre in check[cor]:
                if find(pre) == False:
                    return False
            cycle.remove(cor)
            visit.add(cor)
            ans.append(cor)
        for cor in range(numCourses):
            if find(cor) == False:
                return []
        return ans  