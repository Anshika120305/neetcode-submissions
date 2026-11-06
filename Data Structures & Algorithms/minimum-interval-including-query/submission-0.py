class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        
        # Sort queries while keeping track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        min_heap = []
        res = {}
        i = 0
        n = len(intervals)
        
        for q_idx, q_val in sorted_queries:
            # Add all intervals that start before or at the current query
            while i < n and intervals[i][0] <= q_val:
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1
            
            # Remove intervals that end before the current query (expired intervals)
            while min_heap and min_heap[0][1] < q_val:
                heapq.heappop(min_heap)
            
            # The top of the heap is the smallest valid interval, if any exists
            res[q_idx] = min_heap[0][0] if min_heap else -1
            
        # Return the results in the original query order
        return [res[j] for j in range(len(queries))]