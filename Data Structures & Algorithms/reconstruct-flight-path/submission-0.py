from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list
        adj = defaultdict(list)
        
        # Sort tickets in reverse lexical order so pop() gets the smallest element in O(1)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        res = []
        
        def dfs(airport: str):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            # Post-order placement
            res.append(airport)
            
        dfs("JFK")
        
        # Reverse post-order traversal to get the valid itinerary
        return res[::-1]
