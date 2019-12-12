import copy

from heapq import heappop, heappush

from dfs import valid, move
from puzzle import make_frontier, compare, hashing, heuristic


def a_star_search(board, p):
    queue = []
    heappush(queue, (0, board))
    k = 0
    memo = {}
    while queue:
        current = heappop(queue)
        current_price = current[0];current_state = current[1]
        x = hashing(current_state)
        if memo.get(x, -1) != -1:
            continue
        memo[x] = 1
        if len(queue) > 65:
            queue = queue[:65]

        if compare(current_state, p) == 0:
            print("Busca com heuristica:",k)
            return current_state
        else:
            frontier = make_frontier(current_state)
            for i in frontier:
                frontier_board = move(copy.deepcopy(current_state), i[0], i[1])
                heappush(queue,(current_price+heuristic(frontier_board,p),frontier_board))
            k += 1

    return None