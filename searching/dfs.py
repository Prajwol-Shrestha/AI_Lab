# 2.Write a program to implement DFS.

def dfs(graph, starting_vertex, visited):
    visited.add(starting_vertex)
    print(starting_vertex, end=' ')

    for neighbor in graph[starting_vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


start_vertex = 'A'
visited_vertices = set()

print("DFS Traversal:")
dfs(graph, start_vertex, visited_vertices)
print("\n")
