import functools
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])
        
        res = []
        compressed1 = self.compress_zeros(mat1) 
        compressed2 = self.compress_zeros(mat2)
        for i in range(m):
            res.append(self.row_comb_sparse(mat1[i], mat2, compressed1[i], compressed2))
        
        return res
                              
    def row_comb_sparse(self, row, mat2, comp_row, comp2):
        pos = {}
        for i in comp_row:
            for j in comp2[i]:
                if j not in pos:
                    pos[j] = [i]
                else:
                    pos[j].append(i)

        resrow = [0] * len(mat2[0])
        for j in pos:
            s = 0 
            for i in pos[j]:
                s += row[i] * mat2[i][j]
            resrow[j] = s

        return resrow
                              
    def compress_zeros(self, mat):
        """
        Example:
        7 0 0              [[0],
        0 0 0   returns     [],
        0 0 1              [2]]
        """
        return [[idx for idx, e in enumerate(row) if e != 0] for row in mat]  