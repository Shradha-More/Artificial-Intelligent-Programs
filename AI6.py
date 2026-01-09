# Minimax Algorithm with Alpha-Beta Pruning
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Driver Code
values = list(map(int, input("Enter the values for leaf nodes separated by space: ").split()))
optimal_value = minimax(0, 0, True, values, float('-inf'), float('inf'))
print(f"The optimal value is: {optimal_value}")
