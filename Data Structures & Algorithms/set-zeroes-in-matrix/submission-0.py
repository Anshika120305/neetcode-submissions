class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # This variable tracks whether the first row needs to be zeroed out.
        # The matrix[0][0] cell is shared to track the first column.
        row_zero = False
        
        # Step 1: Mark zeroes in the first row and first column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row_zero = True
                    else:
                        matrix[r][0] = 0
                        
        # Step 2: Use the markers to set inner cells to zero
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # Step 3: Handle the first column first
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # Step 4: Handle the first row using the separate variable
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0  # wait, should be matrix[0][c] = 0
