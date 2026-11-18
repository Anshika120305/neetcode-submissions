class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Clear the least significant bit set to 1
            count += 1
        return count
