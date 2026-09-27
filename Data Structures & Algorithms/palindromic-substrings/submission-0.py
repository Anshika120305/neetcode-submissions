class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            res += self.countPalindrome(s, i, i)
            
            # Even length palindromes (two character center)
            res += self.countPalindrome(s, i, i + 1)
            
        return res

    def countPalindrome(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count