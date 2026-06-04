class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m*n)-1
        while left <= right:
            mid  = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_element = matrix[row][col]
            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid +1
            else:
                right = mid-1
        return False