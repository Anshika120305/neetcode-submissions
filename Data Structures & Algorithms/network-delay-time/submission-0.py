
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Step 2: Min-heap initialized with (cost=0, starting_node=k)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0
        
        # Step 3: Dijkstra's shortest path search
        while min_heap:
            w1, u = heapq.heappop(min_heap)
            
            if u in visited:
                continue
            
            visited.add(u)
            max_time = w1
            
            # Stop early if all nodes are visited
            if len(visited) == n:
                return max_time
                
            for v, w2 in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w1 + w2, v))
                    
        return max_time if len(visited) == n else -1