class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        if len(edges) == 0:
            return True
        neighbors = defaultdict(list)
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        q = deque([[edges[0][0], -1]])
        seen.add(edges[0][0])
        while q:
            curr = q.popleft()
            for nei in neighbors[curr[0]]:
                if curr[1] == nei:
                    continue
                elif nei in seen:
                    return False
                else:
                    q.append([nei, curr[0]])
                    seen.add(nei)
        return len(seen) == n