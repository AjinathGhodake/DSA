# 1.	Squares of numbers from 1 to 10:
# Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(
    "Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]>>>",
    [i**2 for i in range(1, 11)],
)

# 2.Filter multiples of 3 from 0 to 20:
# Expected output: [0, 3, 6, 9, 12, 15, 18]
print(
    "Expected output: [0, 3, 6, 9, 12, 15, 18]>>>",
    [i for i in range(0, 20) if i % 3 == 0],
)

# 3. Convert a list of names to lowercase:
# List: ["Alice", "Bob", "Charlie"]
# Expected output: ["alice", "bob", "charlie"]
words = ["Alice", "Bob", "Charlie"]
print(
    'Expected output: ["alice", "bob", "charlie"]>>>',
    [word.lower() for word in words],
)

# 4.Create a list of (x, y) pairs where x is from 1 to 3 and y is from 1 to 2:
# Expected output: [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
print(
    "Expected output: [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]>>>",
    [(x, y) for x in range(1, 4) for y in range(1, 3)],
)
