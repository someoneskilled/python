# MiniMax Algorithm Works as Follows:

# Start from the root node (usually at depth 0), assuming it's the maximizing player's turn.
# Recursively move down the tree until the target depth (leaf nodes) is reached.
# At the leaf nodes, return the score (or utility value).
# While returning back up the tree:
    # If it's the maximizing player's turn, select the maximum value among the child nodes.
    # If it's the minimizing player's turn, select the minimum value among the child nodes.
# Repeat this process until the root node receives the optimal value.
# The final value at the root is the best score the maximizing player can guarantee with optimal play.

import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: target depth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

# Driver code
scores = []

x = int(input("Enter the number of values (should be power of 2): "))
for i in range(x):
    y = int(input(f"Enter value {i + 1}: "))
    scores.append(y)

treeDepth = int(math.log2(len(scores)))

print("The optimal value is:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))
