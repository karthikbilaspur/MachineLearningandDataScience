# Splitting Arrays in NumPy

import numpy as np

# Section 1: Splitting Arrays Into Equal Parts using numpy.split()
def splitting_arrays_into_equal_parts():
    print("Splitting Arrays Into Equal Parts using numpy.split():")
    arr = np.arange(6)
    print("Original Array:", arr)
    result = np.split(arr, 2)
    print("Split Array:\n", result)

# Section 2: Unequal Splitting of Arrays using numpy.array_split()
def unequal_splitting_of_arrays():
    print("\nUnequal Splitting of Arrays using numpy.array_split():")
    arr = np.arange(13)
    print("Original Array:", arr)
    result = np.array_split(arr, 4)
    print("Split Array:\n", result)

# Section 3: Splitting NumPy 2D Arrays
def splitting_numpy_2d_arrays():
    print("\nSplitting NumPy 2D Arrays:")
    arr = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
    print("Original 2D Array:\n", arr)
    result = np.split(arr, 3, axis=1)
    print("Split Array:\n", result)

# Section 4: Vertical Splitting of Arrays using numpy.vsplit()
def vertical_splitting_of_arrays():
    print("\nVertical Splitting of Arrays using numpy.vsplit():")
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print("Original Matrix:\n", matrix)
    result = np.vsplit(matrix, 2)
    print("Split Matrix:\n", result)

# Section 5: Horizontal Splitting of Arrays using numpy.hsplit()
def horizontal_splitting_of_arrays():
    print("\nHorizontal Splitting of Arrays using numpy.hsplit():")
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print("Original 2D Array:\n", arr)
    result = np.hsplit(arr, 2)
    print("Split Array:\n", result)

# Section 6: Splitting Arrays Along the Third Axis using numpy.dsplit()
def splitting_arrays_along_third_axis():
    print("\nSplitting Arrays Along the Third Axis using numpy.dsplit():")
    original_3d_array = np.arange(24).reshape((2, 3, 4))
    print("Original 3D Array:\n", original_3d_array)
    result = np.dsplit(original_3d_array, 2)
    print("Split Array:\n", result)

# Main function
def main():
    print("Splitting Arrays in NumPy")
    print("-------------------------")

    splitting_arrays_into_equal_parts()
    unequal_splitting_of_arrays()
    splitting_numpy_2d_arrays()
    vertical_splitting_of_arrays()
    horizontal_splitting_of_arrays()
    splitting_arrays_along_third_axis()

if __name__ == "__main__":
    main()
    