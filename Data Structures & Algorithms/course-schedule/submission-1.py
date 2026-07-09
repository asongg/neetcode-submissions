class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            in_degree[prereq] += 1
            graph[course].append(prereq)
        queue = deque([])
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        top_sort = []
        while queue:
            curr = queue.popleft()
            top_sort.append(curr)
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(top_sort) == len(graph):
            return True
        else:
            return False

        