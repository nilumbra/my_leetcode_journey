import functools
class Solution:
    def multiply(self, mat1, mat2):
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])
        
        res = []
        compressed1 = self.compress_zeros(mat1) 
        compressed2 = self.compress_zeros(mat2)
        for i in range(m):
            res.append(self.row_comb_sparse(mat1[i], mat2, compressed1[i], compressed2))

        return res


        
    def row_comb(self, row, mat):
        """
        Assumes row is a row vector and mat2 is a matrix where len(row) == len(mat2)
        Returns the linear combination of mat2's rows weighted by row
        """
        return functools.reduce(lambda a, b: [x + y for x, y in zip(a, b)], 
                                [self.scale(f, r) for f, r in zip(row, mat)])
        

    def row_comb_sparse(self, row, mat2, comp_row, comp2):
        """
        e.g.
        row = [1, 0, 2, 0],  mat2 = [[3, 0, 1, 0],
                                     [2, 3, 0, 0],
                                     [0, 1, 2, 0],
                                     [7, 0, 0, 0],] 

        comp_row = [0, 2], comp2 = [[0, 2],
                                    [0, 1],
                                    [1, 2],
                                    [0],]

        Intermediate:
            pos = { 0: [0, 2],
                    1: [2],
                    2: [2], }

            row = [3, 2, 5, 0]


        """
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




    def scale(self, s, v):
        """
        Returns the result of multiply vector v by scalar s
        """
        return list(map(lambda e: e * s ,v))
    
    def scale_sparse(self, mat, s, i, js):
        row = [0] * len(mat[0])
        for j in js:
	        row[j] = mat[i][j] * s 
        return row
                              
    def compress_zeros(self, mat):
        """
        Example:
        7 0 0              [[0],
        0 0 0   returns     [],
        0 0 1              [2]]
        """
        return [[idx for idx, e in enumerate(row) if e != 0] for row in mat]  

if __name__ == '__main__':
    row = [1, 0, 2, 0]
    mat2 = [[3, 0, 1, 0],
            [2, 3, 0, 0],
            [0, 1, 2, 0],
            [7, 0, 0, 0],] 

    comp_row = [0, 2]
    comp2 = [[0, 2],
             [0, 1],
             [1, 2],
             [0],]
    

    solution = Solution()
    print(solution.row_comb_sparse(row, mat2, comp_row, comp2))
    