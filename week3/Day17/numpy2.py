# Reshape NumPy Array - Python

import numpy as np

# Section 1: Reshaping a 1-D array into a 2-D array
def reshaping_1d_to_2d():
    print("Reshaping a 1-D array into a 2-D array:")
    a = np.array([1, 2, 3, 4, 5, 6])
    print("Original Array:", a)
    r = a.reshape(2, 3)
    print("Reshaped Array:\n", r)

# Section 2: Reshaping a 1-D array into a 3-D array
def reshaping_1d_to_3d():
    print("\nReshaping a 1-D array into a 3-D array:")
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original Array:", a)
    r = a.reshape(2, 2, 2)
    print("Reshaped Array:\n", r)

# Section 3: Using -1 to auto-calculate the missing dimension
def using_minus_one():
    print("\nUsing -1 to auto-calculate the missing dimension:")
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print("Original Array:", a)
    r = a.reshape(3, -1)
    print("Reshaped Array:\n", r)

# Main function
def main():
    print("Reshape NumPy Array - Python")
    print("-----------------------------")

    reshaping_1d_to_2d()
    reshaping_1d_to_3d()
    using_minus_one()

if __name__ == "__main__":
    main()