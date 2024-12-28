def print_triangle(n):
    for i in range(1, n + 1):  # Loop through rows
        print(" " * (n - i) + "*" * (2 * i - 1))  # Print spaces and stars

# Input: Height of the triangle
n = int(input("Enter the height of the triangle: "))

# Print the triangle
print_triangle(n)
