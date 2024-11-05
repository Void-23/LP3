import heapq
from collections import defaultdict, Counter

# Node class for Huffman Tree
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char  # Character
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child
        self.right = None  # Right child

    # Comparator for priority queue to compare based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree using a priority queue (min-heap)
def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)  # Create a min-heap from the nodes

    while len(heap) > 1:
        # Pop two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with the combined frequency
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the new node back into the heap
        heapq.heappush(heap, merged)

    return heap[0]  # The root node of the Huffman Tree

# Function to generate Huffman codes by traversing the tree
def generate_huffman_codes(root, current_code='', codes={}):
    if root is None:
        return

    # If it's a leaf node, assign the current code to the character
    if root.char is not None:
        codes[root.char] = current_code

    # Recur for left subtree with '0' and right subtree with '1'
    generate_huffman_codes(root.left, current_code + '0', codes)
    generate_huffman_codes(root.right, current_code + '1', codes)

    return codes

# Function to perform Huffman Encoding
def huffman_encoding(data):
    if not data:
        return "", {}

    # Step 1: Calculate frequency of each character
    frequency = Counter(data)

    # Step 2: Build the Huffman Tree using a greedy strategy
    root = build_huffman_tree(frequency)

    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(root)

    # Step 4: Encode the input data using the Huffman Codes
    encoded_data = ''.join([huffman_codes[char] for char in data])

    return encoded_data, huffman_codes

# Function to decode Huffman encoded data
def huffman_decoding(encoded_data, huffman_codes):
    reverse_codes = {v: k for k, v in huffman_codes.items()}

    current_code = ""
    decoded_output = []

    # Traverse the encoded data and decode it
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_output.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_output)

# Example usage
if __name__ == "__main__":
    data = "huffman encoding is a greedy algorithm"

    print(f"Original data: {data}")

    # Huffman Encoding
    encoded_data, huffman_codes = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")
    print(f"Huffman Codes: {huffman_codes}")

    # Huffman Decoding
    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print(f"Decoded data: {decoded_data}")
