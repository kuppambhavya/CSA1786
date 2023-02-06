graph = {
  'A' : ['D','E','C'],
  'C' : ['B'],
  'B' : [],
  'D' : ['E'],
  'E' : []
}

visited = set() 

def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
