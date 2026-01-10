# matrix_operations.py

import numpy as np

def create_matrix(rows, cols):
    """
    Create a matrix with given number of rows and columns.

    Parameters:
    rows (int): Number of rows
    cols (int): Number of columns

    Returns:
    np.ndarray: A matrix with given number of rows and columns
    """
    matrix = np.random.randint(0, 10, size=(rows, cols))
    return matrix

def add_matrices(A, B):
    """
    Add two matrices.

    Parameters:
    A (np.ndarray): First matrix
    B (np.ndarray): Second matrix

    Returns:
    np.ndarray: Sum of A and B
    """
    return A + B

def multiply_matrices(A, B):
    """
    Multiply two matrices.

    Parameters:
    A (np.ndarray): First matrix
    B (np.ndarray): Second matrix

    Returns:
    np.ndarray: Product of A and B
    """
    return np.dot(A, B)

def transpose_matrix(A):
    """
    Transpose a matrix.

    Parameters:
    A (np.ndarray): Matrix to transpose

    Returns:
    np.ndarray: Transpose of A
    """
    return A.T

def determinant_matrix(A):
    """
    Calculate the determinant of a matrix.

    Parameters:
    A (np.ndarray): Matrix

    Returns:
    float: Determinant of A
    """
    return np.linalg.det(A)

def inverse_matrix(A):
    """
    Calculate the inverse of a matrix.

    Parameters:
    A (np.ndarray): Matrix

    Returns:
    np.ndarray: Inverse of A
    """
    return np.linalg.inv(A)

def main():
    # Create two 2x2 matrices
    A = create_matrix(2, 2)
    B = create_matrix(2, 2)

    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    # Add matrices
    print("\nA + B:")
    print(add_matrices(A, B))

    # Multiply matrices
    print("\nA * B:")
    print(multiply_matrices(A, B))

    # Transpose matrix A
    print("\nA^T:")
    print(transpose_matrix(A))

    # Calculate determinant of A
    print("\ndet(A):")
    print(determinant_matrix(A))

    # Calculate inverse of A
    try:
        print("\nA^-1:")
        print(inverse_matrix(A))
    except np.linalg.LinAlgError:
        print("\nA is not invertible.")

if __name__ == "__main__":
    main()