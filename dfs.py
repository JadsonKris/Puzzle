import copy
import sys
from puzzle import compare, valid, move, make_frontier, hashing


def dfs(max_level, board, p, current_level, memo={}):
    global search, k
    k += 1
    x = hashing(board)
    if memo.get(x, -1) != -1 or search == 1:
        return 0

    elif compare(board, p) == 0:
        print("DFS: ", k)
        search = 1
        return 1

    elif current_level == max_level:
        return 0

    else:
        memo[x] = 1
        frontier = make_frontier(board)
        current_level += 1

        for i in frontier:
            frontier_board = move(copy.deepcopy(board), i[0], i[1])
            dfs(max_level, frontier_board, p, current_level, memo)


def dfs_interactive(board, p):
    sys.setrecursionlimit(1000000000)
    global k, search
    k = search = max_level = 0
    while not dfs(max_level, board, p, 0):
        max_level += 1


def dfs_depth_limited(board, max_level, p):
    global k, search
    k = search = 0
    sys.setrecursionlimit(1000000000)
    dfs(max_level, board, p, 0)
