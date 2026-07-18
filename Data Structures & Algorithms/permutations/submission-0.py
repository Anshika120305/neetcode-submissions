class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in nums:
                if num in perm:
                    continue
                perm.append(num)
                backtack(perm)
                perm.pop()
        backtack([])
        return res