# A class to represent an item with weight and value
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to solve the fractional knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0  # To keep track of total value in the knapsack
    for item in items:
        if capacity >= item.weight:
            # If the knapsack can take the whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take a fraction of the item that fits into the remaining capacity
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0  # Knapsack is now full
            break

    return total_value

# Example usage
items = [
    Item(60, 10),  # value, weight
    Item(100, 20),
    Item(120, 30)
]

capacity = 50  # Knapsack capacity
max_value = fractional_knapsack(items, capacity)

print(f"Maximum value in the knapsack: {max_value}")
