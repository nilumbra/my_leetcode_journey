class Solution(object):
    def rotate(self, matrix):
        L = len(matrix)
        new_coor = lambda i, j: [j, L - 1 - i]

        for i in range(L // 2):
            for j in range(i, L - 1 - i):
                x, y = i, j 
                for c in range(4):
                    nxt_x, nxt_y = new_coor(x, y) # get nxt coor
                    matrix[nxt_x][nxt_y], matrix[i][j] = matrix[i][j], matrix[nxt_x][nxt_y]

                    x, y = nxt_x, nxt_y
