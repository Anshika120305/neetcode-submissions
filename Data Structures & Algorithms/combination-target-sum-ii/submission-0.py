class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, current_combo, current_sum):
            if current_sum ==  target:
                res.append(list(current_combo))
                return
            if current_sum > target or i >= len(candidates):
                return
            current_combo.append(candidates[i])
            backtrack(i+1, current_combo, current_sum + candidates[i])
            current_combo.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, current_combo, current_sum)
        backtrack(0,[], 0)
        return res