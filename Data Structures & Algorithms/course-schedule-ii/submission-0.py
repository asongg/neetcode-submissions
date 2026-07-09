class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses # A -> B
        graph = defaultdict(list) # node -> [neighbors]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            in_degree[prereq] += 1
        queue = deque([])
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        order = [] # reverse order, will be sliced later
        while queue:
            curr = queue.popleft()
            order.append(curr) # any popped node has indegree 0
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        order = order[::-1]
        if len(order) == len(graph): return order
        else: return []