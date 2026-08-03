class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
            
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for next_course in adj[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    
       
        return order if len(order) == numCourses else []