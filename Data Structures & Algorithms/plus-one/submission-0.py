class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the array from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # If all digits were 9, prepend 1 to the list
        return [1] + digits