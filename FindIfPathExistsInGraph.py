'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional 
edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
or false otherwise.
'''

from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if destination == source:
            return True
        check = {i : [] for i in range(n)}
        for s, d in edges:
            check[s].append(d)
            check[d].append(s)
        ans = deque()
        ans.append(source)
        visit = set()
        visit.add(source)
        while ans:
            sour = ans.popleft()
            for desti in check[sour]:
                if desti not in visit:
                    if desti == destination:
                        return True
                    ans.append(desti)
                    visit.add(desti)
        return False

'''
Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
'''