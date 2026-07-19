
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, current_subset):
            if i == len(nums):
                res.append(current_subset.copy())
                return
            current_subset.append(nums[i])        
            backtrack(i+1, current_subset)
            current_subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, current_subset)
        backtrack(0, [])
        return res