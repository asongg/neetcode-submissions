class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = defaultdict(list)
        for src, dst in prerequisites:
            indegree[src] += 1
            neighbors[dst].append(src)
        start = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                start.append(i)
        q = deque(start)
        res = []
        while q:
            curr = q.popleft()
            for neighbor in neighbors[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            res.append(curr)
        return (len(res) == numCourses)