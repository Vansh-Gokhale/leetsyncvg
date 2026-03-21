class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        rows_to_zero = [False] * num_rows
        cols_to_zero = [False] * num_cols
        
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if matrix[row_idx][col_idx] == 0:
                    rows_to_zero[row_idx] = True
                    cols_to_zero[col_idx] = True
        
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if rows_to_zero[row_idx] or cols_to_zero[col_idx]:
                    matrix[row_idx][col_idx] = 0