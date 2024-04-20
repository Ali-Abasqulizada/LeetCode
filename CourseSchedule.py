'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        allCourse = {i : [] for i in range(numCourses)}
        for cor, pcor in prerequisites:
            allCourse[cor].append(pcor)
        visit = set()
        def find(cor):
            if cor in visit:
                return False
            elif allCourse[cor] == []:
                return True
            visit.add(cor)
            for pcor in allCourse[cor]:
                if not find(pcor): 
                    return False
            visit.remove(cor)
            allCourse[cor] = []
            return True
        for cor in range(numCourses):
            if not find(cor):
                return False
        return True

#or

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        check = [[] for _ in range(numCourses)]
        course = [0] * numCourses
        ans = []
        for cor, pcor in prerequisites:
            check[pcor].append(cor)
            course[cor] += 1
        solve = deque()
        for pcor in range(numCourses):
            if course[pcor] == 0:
                solve.append(pcor)
        while solve:
            pcor = solve.popleft()
            ans.append(pcor)
            for cor in check[pcor]:
                course[cor] -= 1
                if course[cor] == 0:
                    solve.append(cor)
        return len(ans) == numCourses

'''
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''