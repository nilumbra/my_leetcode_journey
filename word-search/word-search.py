class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        w, h = len(board[0]), len(board)
        
        def search(G, pos, s):
            # Recursive method to determine whether <s> is constructible 
            # at a given position pos
            if not s: return True
            i, j = pos[0], pos[1]
            # print(G[i][j], pos[0], pos[1])
            if G[i][j] != s[0]: 
                return False
            else:
                if len(s) == 1: return True

                parent.add(pos)
                res = False
                if j + 1 < w and (i, j+1) not in parent:
                    res = res or search(G, (i, j+1), s[1:])
                if j - 1 >= 0 and (i, j-1) not in parent:
                    res = res or search(G, (i, j-1), s[1:])
                if i + 1 < h and (i+1, j) not in parent:
                    res = res or search(G, (i+1, j), s[1:])
                if i - 1 >= 0 and (i-1, j) not in parent:
                    res = res or search(G, (i-1, j), s[1:])
                parent.remove(pos)
                return res
        for i in range(h):
            for j in range(w):
                parent = set()
                if search(board, (i, j), word): return True
        
        return False