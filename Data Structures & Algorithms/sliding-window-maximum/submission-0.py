class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() 
        
        for i, num in enumerate(nums):
           
            while q and nums[q[-1]] < num:
                q.pop()
                
            
            q.append(i)
            
           
            if q[0] < i - k + 1:
                q.popleft()
                
           
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output