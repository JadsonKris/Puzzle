def start(p):
    if p == 8:
        return [[1, 3, 6],
                [5, 2, 4],
                [7, 8, 0]]

    elif p == 16:
        return [[15, 10, 0, 13], [11,4, 1, 12], [3, 7, 9,8], [2,14, 6, 5]]

    else:
        return "Invalid input"


def compare(board, p, final_board=[]):
    if p == 8:
        if final_board:
            return compare8(board, final_board)
        else:
            return compare8(board)

    elif p == 16:
        if final_board:
            return compare16(board, final_board)
        else:
            return compare16(board)

    else:
        return "Invalid size of board"


def compare8(board, final_board=[[1, 2, 3], [4, 5, 6], [7, 8, 0]]):
    h = 0
    for i in range(len(final_board)):
        for j in range(len(final_board[i])):
            if board[i][j] != final_board[i][j]: h += 1

    return h


def compare16(board, final_board=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]):
    h = 0
    for i in range(len(final_board)):
        for j in range(len(final_board[i])):
            if board[i][j] != final_board[i][j]: h += 1

    return h


def hashing(board):
    return tuple(tuple(i) for i in board)


def valid(board, x, y):
    if x - 1 >= 0:
        if board[x - 1][y] == 0:
            return True
    if x + 1 < len(board):
        if board[x + 1][y] == 0:
            return True

    if y + 1 < len(board):
        if board[x][y + 1] == 0:
            return True

    if y - 1 >= 0:
        if board[x][y - 1] == 0:
            return True

    return False


def move(board, x, y):
    if x - 1 >= 0:
        if board[x - 1][y] == 0:
            board[x - 1][y] = board[x][y]
            board[x][y] = 0
            return board

    if x + 1 < len(board):
        if board[x + 1][y] == 0:
            board[x + 1][y] = board[x][y]
            board[x][y] = 0
            return board

    if y + 1 < len(board):
        if board[x][y + 1] == 0:
            board[x][y + 1] = board[x][y]
            board[x][y] = 0
            return board

    if y - 1 >= 0:
        if board[x][y - 1] == 0:
            board[x][y - 1] = board[x][y]
            board[x][y] = 0
            return board

    else:
        return False


def make_frontier(board):
    result = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if valid(board, i, j):
                result.append((i, j))
    return result


def dist(xy1, xy2):
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def heuristic_aux(valor, i, j , p):
    if p == 8: pos = [(2,2), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1)]

    else: pos = [(3,3), (0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3),
                 (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2)]
    return dist((i,j), pos[valor])

def heuristic(board, p):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                zero = (i,j)

    for i in range(len(board)):
        for j in range(len(board[i])):
            sum += heuristic_aux(board[i][j], i, j, p) * dist((i,j), zero)

    return sum

