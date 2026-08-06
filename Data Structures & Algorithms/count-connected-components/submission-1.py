class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        neighbors = defaultdict(list)
        for edge in edges:
            neighbors[edge[1]].append(edge[0])
            neighbors[edge[0]].append(edge[1])
        def dfs(i):
            for nei in neighbors[i]:
                if nei in seen:
                    continue
                seen.add(nei)
                dfs(nei)
        res = 0
        for edge in edges:
            if edge[0] not in seen:
                res += 1
                dfs(edge[0])
        res += n - len(seen)
        return res