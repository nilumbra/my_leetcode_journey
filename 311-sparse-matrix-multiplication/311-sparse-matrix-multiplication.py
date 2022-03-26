import functools
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [0] * len(mat1) 
        for idx, row in enumerate(mat1):
            res[idx] = self.row_comb(row, mat2)
        
        return res
        
    def row_comb(self, row, mat):
        """
        Assumes row is a row vector and mat2 is a matrix where len(row) == len(mat2)
        Returns the linear combination of mat2's rows weighted by row
        """
        return functools.reduce(lambda a, b: [x + y for x, y in zip(a, b)], 
                                [self.scale(f, r) for f, r in zip(row, mat)])
            
    def scale(self, s, v):
        """
        Returns the result of multiply vector v by scalar s
        """
        return list(map(lambda e: e * s ,v))