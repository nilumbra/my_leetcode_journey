class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for rowLen in range(1, numRows+1):
            row = [1] * rowLen
            for i in range(1, rowLen - 1):
                # print(ans, rowLen)
                row[i] = ans[rowLen - 2][i - 1] + ans[rowLen - 2][i]
            row[rowLen - 1] = 1
            ans.append(row)
        
        return ans
                