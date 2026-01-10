
# Numpy Array Indexing

import numpy as np

# Section 1: Accessing Elements in 1D Arrays
def accessing_elements_in_1d_arrays():
    print("Accessing Elements in 1D Arrays:")
    arr = np.array([10, 20, 30, 40, 50])
    print("Array:", arr)
    print("First Element:", arr[0])
    print("Last Element:", arr[-1])

# Section 2: Accessing Elements in Multidimensional Arrays
def accessing_elements_in_multidimensional_arrays():
    print("\nAccessing Elements in Multidimensional Arrays:")
    # 2D Array
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("2D Array:\n", matrix)
    print("Element at (1, 2):", matrix[1, 2])

    # 3D Array
    cube = np.array([[[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]],
                     
                     [[10, 11, 12],
                      [13, 14, 15],
                      [16, 17, 18]]])
    print("\n3D Array:\n", cube)
    print("Element at (1, 2, 0):", cube[1, 2, 0])

# Section 3: Slicing Arrays
def slicing_arrays():
    print("\nSlicing Arrays:")
    # 1D Array
    arr = np.array([0, 1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Slice (1:4):", arr[1:4])

    # 2D Array
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\n2D Array:\n", matrix)
    print("Slice (0:2, 1:3):\n", matrix[0:2, 1:3])

# Section 4: Boolean Indexing
def boolean_indexing():
    print("\nBoolean Indexing:")
    arr = np.array([10, 15, 20, 25, 30])
    print("Array:", arr)
    print("Elements > 20:", arr[arr > 20])

# Section 5: Fancy Indexing
def fancy_indexing():
    print("\nFancy Indexing:")
    arr = np.array([10, 20, 30, 40, 50])
    indices = [0, 2, 4]
    print("Array:", arr)
    print("Elements at indices:", arr[indices])

# Section 6: Integer Array Indexing
def integer_array_indexing():
    print("\nInteger Array Indexing:")
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Elements at indices:", arr[[0, 2, 4]])

# Section 7: Ellipsis (...) in Indexing
def ellipsis_in_indexing():
    print("\nEllipsis (...) in Indexing:")
    cube = np.random.rand(4, 4, 4)
    print("Cube:\n", cube)
    print("Slice using Ellipsis:\n", cube[..., 0])

# Section 8: Using np.newaxis to Add New Dimensions
def using_np_newaxis():
    print("\nUsing np.newaxis to Add New Dimensions:")
    arr = np.array([1, 2, 3])
    print("Array:", arr)
    print("Array with new axis:\n", arr[:, np.newaxis])

# Section 9: Modifying Array Elements
def modifying_array_elements():
    print("\nModifying Array Elements:")
    arr = np.array([1, 2, 3, 4])
    print("Array:", arr)
    arr[1:3] = 99
    print("Modified Array:", arr)

# Main function
def main():
    print("Numpy Array Indexing")
    print("---------------------")

    accessing_elements_in_1d_arrays()
    accessing_elements_in_multidimensional_arrays()
    slicing_arrays()
    boolean_indexing()
    fancy_indexing()
    integer_array_indexing()
    ellipsis_in_indexing()
    using_np_newaxis()
    modifying_array_elements()

if __name__ == "__main__":
    main()