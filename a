import heapq

tree = {
    'A': {'d': 9, 'b': 7},
    'D': {'C': 3, 'E': 3},
    'C': {'E': 10},
    'B': {'C': 7},
    'E': {}
}

heuristics = {
    'A': 15,
    'B': 10,
    'C': 10,
    'D': 4,
    'E': 0
}

def f(current, goal, cost):
    return cost + heuristics[goal]

def a_star_search(graph, start, goal):
    frontier = [(0, start)]
    path = []
    visited = set()
    while frontier:
        cost, current = heapq.heappop(frontier)
        if current == goal:
            return path
        visited.add(current)
        for neighbor, cost2 in graph[current].items():
            if neighbor not in visited:
                total_cost = cost + cost2
                heapq.heappush(frontier, (f(neighbor, goal, total_cost), neighbor))
                path.append((current, neighbor, total_cost))
    return None

result = a_star_search(tree, 'A', 'E')
print(result)
