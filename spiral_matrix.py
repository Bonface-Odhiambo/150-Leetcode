from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    # Handle empty matrix
    if not matrix:
        return []
    
    result = []
    m, n = len(matrix), len(matrix[0])
    
    # Initialize boundaries
    top = 0
    bottom = m - 1  # last row
    left = 0
    right = n - 1   # last column
    
    while top <= bottom and left <= right:
        # Traverse right: fixed row (top), varying column
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down: varying row, fixed column (right)
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Check if still have rows to traverse
        if top <= bottom:
            # Traverse left: fixed row (bottom), varying column backwards
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Check if still have columns to traverse
        if left <= right:
            # Traverse up: varying row backwards, fixed column (left)
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Test cases
def test_spiral_matrix():
    # Test case 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test 1:", spiral_matrix(matrix1))  # Expected: [1,2,3,6,9,8,7,4,5]
    
    # Test case 2: 3x4 matrix
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print("Test 2:", spiral_matrix(matrix2))  # Expected: [1,2,3,4,8,12,11,10,9,5,6,7]
    
    # Test case 3: 1x1 matrix
    matrix3 = [[1]]
    print("Test 3:", spiral_matrix(matrix3))  # Expected: [1]
    
    # Test case 4: Single row matrix
    matrix4 = [[1, 2, 3]]
    print("Test 4:", spiral_matrix(matrix4))  # Expected: [1,2,3]
    
    # Test case 5: Single column matrix
    matrix5 = [[1], [2], [3]]
    print("Test 5:", spiral_matrix(matrix5))  # Expected: [1,2,3]

# Run tests
if __name__ == "__main__":
    test_spiral_matrix()