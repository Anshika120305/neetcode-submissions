class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        # Min-heap stores tuples of (max_elevation_so_far, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            
            # Reached the bottom-right corner
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # The time to reach (nr, nc) is max(current_time, grid[nr][nc])
                    heapq.heappush(min_heap, (max(time, grid[nr][nc]), nr, nc))