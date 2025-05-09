# BFS Algorithm

# The algorithm works as follows:

# Start by putting any one of the graph's vertices at the back of a queue.
# Take the front item of the queue and add it to the visited list.
# Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
# Keep repeating steps 2 and 3 until the queue is empty.
# The graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the BFS algorithm on every node


graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # List to keep track of visited nodes
queue = []    # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver code
print("Following is the Breadth-First Search:")
bfs(visited, graph, '5')
