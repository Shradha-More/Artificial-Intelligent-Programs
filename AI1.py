# Depth-First Search Implementation
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
graph = {}
n = int(input("Enter the number of nodes in the graph: "))

for _ in range(n):
    node = input("Enter the node: ")
    edges = input(f"Enter the neighbors of {node} separated by space: ").split()
    graph[node] = edges

visited = set()
start_node = input("Enter the starting node: ")

print("Following is the Depth-First Search:")
dfs(visited, graph, start_node)
