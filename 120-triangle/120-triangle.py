class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        The minimum path from top to bottom in the triangle specified by the problem has the optimal substructure as follows:
        hummmmmm what? I don't actually know what's the optimal substructure ヽ(ヽﾟﾛﾟ)
        """
        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][-1] += triangle[i - 1][-1]
            for j in range(1, i):
                print(i,j)
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
                
        # print(triangle)
        
        
        
        return min(*triangle[-1])
                
                