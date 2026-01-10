
# Numpy numpy.resize() - Python

import numpy as np

# Section 1: Resizing a 1D array into a 2x3 array
def resizing_1d_to_2x3():
    print("Resizing a 1D array into a 2x3 array:")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original Array:", arr)
    arr.resize((2, 3))
    print("Resized Array:\n", arr)

# Section 2: Resizing a 1D array into a 3x4 array
def resizing_1d_to_3x4():
    print("\nResizing a 1D array into a 3x4 array:")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original Array:", arr)
    arr.resize((3, 4))
    print("Resized Array:\n", arr)

# Section 3: Resizing a 1D array into a 2x2 array
def resizing_1d_to_2x2():
    print("\nResizing a 1D array into a 2x2 array:")
    arr = np.array([10, 20, 30, 40, 50])
    print("Original Array:", arr)
    arr.resize((2, 2))
    print("Resized Array:\n", arr)

# Main function
def main():
    print("Numpy numpy.resize() - Python")
    print("----------------------------")

    resizing_1d_to_2x3()
    resizing_1d_to_3x4()
    resizing_1d_to_2x2()

if __name__ == "__main__":
    main()