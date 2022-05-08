import bisect
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        insert_pos = bisect.bisect_left([*reversed(grid[0])], 0)
        i_0, j_0 = 0, n - 1 - insert_pos
        
        if j_0 == -1: return m * n
        neg_count = 0
        
        while j_0 >= 0 and i_0 < m:
            neg_count += n - 1 - j_0
            while i_0 + 1 < m and grid[i_0 + 1][j_0] < 0: # while bottom cell is negtive
                # go left on this row
                j_0 -= 1
                if j_0 < 0: break # notice we need to maintain the loop invariant
            
            # Having found the first(cell) j_0 on <i_0> row from right s.t. the bottom cell is positive
            i_0 += 1
        
        # all row(if any) below i_0 is of full negative numbers
        
        if i_0 < m:
            neg_count += (m - i_0) * n # by the structure of last while loop i_0 will be incremented before exiting, hence here it is i_0, instead of m - 1 - i_0
        
        return neg_count