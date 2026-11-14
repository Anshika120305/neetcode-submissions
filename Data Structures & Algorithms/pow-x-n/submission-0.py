class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base cases
        if x == 0:
            return 0.0
        if n == 0:
            return 1.0

        # Helper function for recursive binary exponentiation
        def helper(base: float, power: int) -> float:
            if power == 0:
                return 1.0
            
            res = helper(base, power // 2)
            res = res * res
            
            return base * res if power % 2 != 0 else res

        # Handle negative exponents
        ans = helper(x, abs(n))
        return ans if n >= 0 else 1 / ans