# The DFS algorithm works as follows:

# Start by putting any one of the graph's vertices on top of a stack.
# Take the top item of the stack and add it to the visited list.
# Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
# Keep repeating steps 2 and 3 until the stack is empty.

# DFS Algorithm Implementation in Python using adjacency list

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver code
print("Following is the Depth-First Search:")
dfs(visited, graph, '5')
