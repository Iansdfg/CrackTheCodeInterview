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
                offset = i - first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = top
        
                
                
            
            
        
        
