class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row0, col0 = [], []
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j]==0:
                    col0.append(i)
                    row0.append(j)
        for col in col0:
            for j in xrange(n):
                matrix[col][j]=0
        for i in xrange(m):
            for row in row0:
                matrix[i][row]=0

        

                    
        
                    
                
        
