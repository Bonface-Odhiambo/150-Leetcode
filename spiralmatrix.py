def spiral_order(matrix):
    """
    Returns elements of matrix in spiral order using list operations.
    
    Args:
        matrix: List[List[int]] - Input matrix
    Returns:
        List[int] - Elements in spiral order
    """
    ret = []
    while matrix:
        # 1. Go right: add first row
        ret += matrix.pop(0)
        
        # 2. Go down: add rightmost elements
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        
        # 3. Go left: add bottom row in reverse
        if matrix:
            ret += matrix.pop()[::-1]
            
        # 4. Go up: add leftmost elements, bottom to top
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
                
    return ret

# Test cases
def test_spiral_order():
    # Test 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test 1:", spiral_order([row[:] for row in matrix1]))  # Use copy to preserve original
    
    # Test 2: 3x4 matrix
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print("Test 2:", spiral_order([row[:] for row in matrix2]))
    
    # Test 3: 1x1 matrix
    print("Test 3:", spiral_order([[1]]))
    
    # Test 4: Empty matrix
    print("Test 4:", spiral_order([]))
    
    # Test 5: Single row
    print("Test 5:", spiral_order([[1, 2, 3]]))
    
    # Test 6: Single column
    print("Test 6:", spiral_order([[1], [2], [3]]))

test_spiral_order()