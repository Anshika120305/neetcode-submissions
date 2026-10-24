class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        
        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            else:  # char == '*'
                left_min -= 1  # '*' acts as ')'
                left_max += 1  # '*' acts as '('
                
            if left_max < 0:
                return False
            if left_min < 0:
                left_min = 0  # Cannot have negative open brackets
                
        return left_min == 0