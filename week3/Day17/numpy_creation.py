
# Numpy - Array Creation

import numpy as np

# Section 1: Creating Arrays
def creating_arrays():
    print("Creating Arrays:")
    # One-dimensional array
    arr1 = np.array([1, 2, 3, 4, 5])
    print("One-dimensional array:", arr1)

    # Two-dimensional array
    arr2 = np.array([[1, 2], [3, 4]])
    print("Two-dimensional array:\n", arr2)

# Section 2: Creating Arrays with Specific Values
def creating_arrays_with_specific_values():
    print("\nCreating Arrays with Specific Values:")
    # Zeros Array
    arr_zero = np.zeros((3, 4))
    print("Zeros Array:\n", arr_zero)

    # Ones Array
    arr_one = np.ones((2, 3))
    print("Ones Array:\n", arr_one)

    # Full Array
    arr_full = np.full((2, 2), 7)
    print("Full Array:\n", arr_full)

# Section 3: Creating Arrays with Random Values
def creating_arrays_with_random_values():
    print("\nCreating Arrays with Random Values:")
    # Random Float Array
    arr_rand = np.random.rand(2, 3)
    print("Random Float Array:\n", arr_rand)

    # Random Integers
    arr_int = np.random.randint(1, 10, size=(3, 3))
    print("Random Integers:\n", arr_int)

# Section 4: Creating Arrays with a Range of Values
def creating_arrays_with_range_of_values():
    print("\nCreating Arrays with a Range of Values:")
    # Using np.arange()
    arr_range = np.arange(0, 10, 2)
    print("Array using np.arange():", arr_range)

    # Using np.linspace()
    arr_linspace = np.linspace(0, 1, 5)
    print("Array using np.linspace():", arr_linspace)

# Section 5: Identity and Diagonal Matrices
def identity_and_diagonal_matrices():
    print("\nIdentity and Diagonal Matrices:")
    # Identity Matrix
    identity_matrix = np.eye(3)
    print("Identity Matrix:\n", identity_matrix)

    # Diagonal Matrix
    diag_matrix = np.diag([1, 2, 3])
    print("Diagonal Matrix:\n", diag_matrix)

# Main function
def main():
    print("Numpy - Array Creation")
    print("------------------------")

    creating_arrays()
    creating_arrays_with_specific_values()
    creating_arrays_with_random_values()
    creating_arrays_with_range_of_values()
    identity_and_diagonal_matrices()

if __name__ == "__main__":
    main()