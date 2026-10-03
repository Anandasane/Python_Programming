def dfs(matrix, start_node):
    n = len(matrix)
    visited = []
    stack = [start_node]
    seen = set()
    
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            visited.append(node)
            for neighbor in range(n):
                if matrix[node][neighbor] == 1 and neighbor not in seen:
                    stack.append(neighbor)
    
    return visited   

print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
