class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return []
        row_num = len(matrix)
        
        for layer in range(row_num//2):
            first, last = layer, row_num-1-layer
            for i in range(first, last):
                distance = i-first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-distance][first]
                matrix[last-distance][first] = matrix[last][last-distance]
                matrix[last][last-distance] = matrix[i][last]
                matrix[i][last] = top
                
        
