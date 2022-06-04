from collections import deque

####################### Utilities ######################################
def indexToCardinal(i, j):
    return i * 3 + (j + 1)

def cardinalToIndex(n):
    q, r = divmod(n - 1, 3)
    return (q, r)

def neighbors(i, j):
    """
    Given i, j
    Return all tiles that board[i][j] can swap with
    """
    if j > 0: yield (i, j - 1) # left
    if i > 0: yield (i - 1, j) # top
    if j < 2: yield (i, j + 1) # right
    if i < 1: yield (i + 1, j) # bottom

def current(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == 0: return [i, j]

    raise ValueError('No empty tile found in board!')
####################### Game Rep ######################################
class SlidingTileGame23:
    def __init__(self, board):
        self.board = board
        self.curr = current(board)

    def serialize(self):
        s = []
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                s.append(str(tile))
        return ''.join(s)

    @staticmethod
    def deserialize(boardStr):
        board = []
        for i in [0, 1]:
            row = []
            for j in [0, 1, 2]:
                row.append(int(boardStr[i * 3 + j]))

            board.append(row)
        return SlidingTileGame23(board)


    def cntInversions(self):
        cnt = 0
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue
                    
                for x, _r in enumerate(self.board):
                    for y, _t in enumerate(_r):
                        if indexToCardinal(x, y) < indexToCardinal(i, j) and _t > tile:
                                # assert tile == board[i][j]
                                # print(f'board[{x}][{y}](={board[x][y]}) > board[{i}][{j}](={tile})')
                                cnt += 1
        return cnt


    def canRestore(self):
        return self.cntInversions() % 2 != 1
    

    def manhattenAll(self):
        m = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        s = 0
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if tile == 0:
                    continue
                arubeki = cardinalToIndex(tile)
                s += m(arubeki, (i, j))

        return s
    
    def move(self, to):
        i_, j_ = to 
        i, j = self.curr
        self.curr = i_, j_

        self.board[i][j], self.board[i_][j_] = self.board[i_][j_], self.board[i][j]

        return self

    def isGoal(self):
        return self.manhattenAll() == 0

    def h(curr_step=0):
        return curr_step + manhattenAll()

    def __repr__(self):
        return str(self.board)

#######################3#######################3#######################3   
class Solution:
    def slidingPuzzle(self, board):
        game = SlidingTileGame23(board)
        
        if not game.canRestore():
            return -1
        else:
            # do bfs
            currLevel = [game]
            curr = game.curr
            # add initial next states to currLevel
            # for nei in neighbors(*game.curr):
            #     currLevel.append(SlidingTileGame23.deserialize(game.move(nei).serialize()))
            #     # print(game)
            #     game.move(curr) # restore curr

            
            seen = set([s.serialize() for s in currLevel])

            moves = 0
            nextLevel = []
            cnt = len(currLevel)
            while len(currLevel) != 0:
                for state in currLevel:
                    # print('Current state:')
                    # print(state)
                    if state.isGoal():
                        # print('This is the goal state')
                        # print('-------------')
                        return moves
                    else:
                        curr = state.curr 
                        # print('-------------')
                        # print('Next states:')
                        for nei in neighbors(*state.curr):
                            neiState = state.move(nei)
                            neiStateStr = neiState.serialize()
                            if neiStateStr not in seen:
                                seen.add(neiStateStr)
                                # print(neiState)
                                nextLevel.append(SlidingTileGame23.deserialize(neiStateStr))
                                cnt += 1
                                # print(f'Traversed state: {cnt}')
                                
                            state.move(curr)
                        # print('-------------')
                # print(f'Moves: {moves}')
                # print(len(nextLevel) == 0)
                moves += 1
                currLevel = nextLevel
                nextLevel = []
                # print(f'Move level: {moves}')

                

            # print([m for m in nextMoves])
