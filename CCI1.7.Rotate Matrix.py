class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return []
        n = len(matrix)
        for layer in xrange(n//2):
            first, last = layer, n-1-layer
            for i in xrange(first, last):
                dis = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-dis][first]
                matrix[last-dis][first] = matrix[last][last-dis]
                matrix[last][last-dis] = matrix[i][last]
                matrix[i][last] = top
#         if not matrix or not matrix[0]: return []
#         n = len(matrix)
#         for layer in range(n // 2):
#             for col in range(n):
#                 matrix[layer][col], matrix[n - 1 - layer][col] = matrix[n - 1 - layer][col], matrix[layer][col]
#         print(matrix)
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
                
            
            
        
        
