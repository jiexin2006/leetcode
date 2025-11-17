import numpy as np

class Solution:
    def rangeAddQueries(self, n: int, queries):
        if n == 0:
            return []
        mat = np.array([[0 for _ in range(n)] for _ in range(n)])
        for query in queries:
            mat[query[0]:query[2] + 1, query[1]: query[3] + 1] += 1
        return mat.tolist()

print(Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))


# class Solution:
#     def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
#         grid = [[0] * (n + 1) for _ in range(n + 1)]
#
#         for start_x, start_y, end_x, end_y in queries:
#             grid[start_x][start_y] += 1
#             if end_y + 1 < n:
#                 grid[start_x][end_y + 1] -= 1
#
#             if end_x + 1 < n:
#                 grid[end_x + 1][start_y] -= 1
#
#             if end_x + 1 < n and end_y + 1 < n:
#                 grid[end_x + 1][end_y + 1] += 1
#
#         for row in range(n):
#             for col in range(n):
#                 if row > 0:
#                     grid[row][col] += grid[row - 1][col]
#
#                 if col > 0:
#                     grid[row][col] += grid[row][col - 1]
#
#                 if row > 0 and col > 0:
#                     grid[row][col] -= grid[row - 1][col - 1]
#
#         print(grid)
#         result = [row[:n] for row in grid[:n]]
#         return result