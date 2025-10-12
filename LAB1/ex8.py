from itertools import combinations

def count_triangles(sides):
    count = 0
    for triplet in combinations(sides, 3):
        a, b, c = sorted(triplet)
        if a + b > c:
            count += 1
            print(f"Valid triangle: {triplet} (sides: {a}, {b}, {c})")
    return count


if __name__ == "__main__":
    test_lists = [
        [4, 6, 3],  # Valid triangle: (3, 4, 6)
        [1, 2, 3],  # Not a valid triangle (1+2 not > 3)
        [3, 4, 5, 6],  # Multiple valid triangles
        [10, 21, 22, 100, 101, 200, 300]  # More test cases
        [2] # Idiot case

    ]

    for test in test_lists:
        print(f"\nTesting list: {test}")
        result = count_triangles(test)
        print(f"Total valid triangles: {result}")

