import copy
from puzzle import compare, move, make_frontier, hashing


def bfs(board, p):
    queue = [board]
    memo = {}
    k = 0
    while queue:
        current = queue.pop(0)
        x = hashing(current)
        if memo.get(x, -1) != -1:
            continue
        memo[x] = 1

        if compare(current,p) == 0:
            print("Bfs:",k)
            return current
        else:
            frontier = make_frontier(current)
            for i in frontier:
                frontier_board = move(copy.deepcopy(current), i[0], i[1])
                queue.append(frontier_board)
            k += 1
    print("BFS nao encontrou")
