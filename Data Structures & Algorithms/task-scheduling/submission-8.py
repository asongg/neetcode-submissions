class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freq = [-cnt for cnt in count.values()]
        heapq.heapify(freq)
        time = 0
        q = deque()
        while q or freq:
            time += 1
            if not freq:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(freq)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(freq, q.popleft()[0])
            
        return time