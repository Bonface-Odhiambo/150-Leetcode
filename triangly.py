def print_triangle(n):
    # Loop from 1 to n (inclusive)
    # i represents current row number and controls both spaces and stars
    for i in range(1, n + 1):
        
        # Calculate number of spaces for current row
        # As row number increases, number of spaces decreases
        # For n=3: Row 1 has 2 spaces, Row 2 has 1 space, Row 3 has 0 spaces
        spaces = " " * (n - i)
        
        # Calculate number of stars for current row
        # First row has 1 star, second has 3 stars, third has 5 stars, and so on
        # Formula: 2*i - 1 gives odd numbers (1, 3, 5, ...)
        stars = "*" * (2 * i - 1)
        
        # Combine spaces and stars and print the current row
        # No need for explicit newline as print() adds it automatically
        print(spaces + stars)

# Get input from user
# int() converts the string input to an integer
n = int(input("Enter the height of the triangle: "))

# Call function to print the triangle
# For n=3, output will be:
#   *    (2 spaces + 1 star)
#  ***   (1 space + 3 stars)
# *****  (0 spaces + 5 stars)
print_triangle(n)