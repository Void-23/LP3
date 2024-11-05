def knapsack_dynamic(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP array to store the maximum value for each item and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Take the maximum value of either including or excluding the current item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack_dynamic(weights, values, capacity)
print(f"Maximum value in the knapsack: {max_value}")
