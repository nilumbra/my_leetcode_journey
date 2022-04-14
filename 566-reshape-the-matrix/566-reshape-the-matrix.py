class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c: return mat
        
        
        new_matrix = [[0] * c for i in range(r)]
        flat = [c for row in mat for c in row]
        
        for rnum in range(r):
            for cnum in range(c):
                
                new_matrix[rnum][cnum] = flat[rnum*c + cnum]
                
        return new_matrix
        