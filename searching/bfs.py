# 1.Write a program to implement BFS.
from collections import deque


def bfs(graph, starting_node):
    visited = set()
    queue = deque([starting_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(current_node, end=' ')
            visited.add(current_node)
            queue.extend(neighbor for neighbor in graph[current_node] if neighbor not in visited)


graph2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'C'],
    'C': ['A', 'D', 'B'],
    'D': ['B', 'C']
}

start_node = 'A'

print("BFS Traversal:")
bfs(graph2, start_node)
print("\n")
