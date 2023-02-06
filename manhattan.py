import heapq
import copy

def manhattan_distance(board, goal):
    """Calculate the Manhattan distance between the current board and the goal board."""
    distance = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                x, y = divmod(goal.index(board[i][j]), 3)
                distance += abs(i - x) + abs(j - y)
    return distance

def bfs(board, goal):
    """Breadth-first search algorithm to find the optimal solution to the 8 puzzle problem."""
    heap = [(manhattan_distance(board, goal), 0, board)]
    visited = set()
    while heap:
        _, cost, current = heapq.heappop(heap)
        if current == goal:
            return cost
        if str(current) in visited:
            continue
        visited.add(str(current))
        i, j = divmod(current.index(0), 3)
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < 3 and 0 <= y < 3:
                new_board = copy.deepcopy(current)
                new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
                heapq.heappush(heap, (manhattan_distance(new_board, goal) + cost + 1, cost + 1, new_board))

board = [[1, 5, 3], [0,4,2], [7, 8, 6]]
goal = [[1, 2, 3], [4,5, 6], [7, 8, 0]]
print("Optimal solution:", bfs(board, goal)):
