class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        maximum = 0

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            stack = []
            for i in range(cols + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    maximum = max(maximum, h * width)
                stack.append(i)

        return maximum