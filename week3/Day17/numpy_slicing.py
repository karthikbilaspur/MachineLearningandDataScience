# How to Access Different Rows of a Multidimensional NumPy Array

import numpy as np

# Section 1: Accessing Rows in 2D Arrays
def accessing_rows_in_2d_arrays():
    print("Accessing Rows in 2D Arrays:")
    # Example 1: Accessing the First and Last row of a 2D NumPy array
    arr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
    print("Array:")
    print(arr)
    res = arr[[0, 2]]
    print("Accessed Rows:")
    print(res)

    # Example 2: Accessing the Middle row of 2D NumPy array
    arr = np.array([[101, 20, 3, 10], [40, 5, 66, 7], [70, 88, 9, 141]])
    print("\nArray:")
    print(arr)
    res_arr = arr[1]
    print("Accessed Row:")
    print(res_arr)

# Section 2: Accessing Rows in 3D Arrays
def accessing_rows_in_3d_arrays():
    print("\nAccessing Rows in 3D Arrays:")
    # Example 1: Accessing the Middle rows of 3D NumPy array
    n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], [[50, 65, 8], [70, 85, 10], [11, 22, 33]]])
    print("Array:")
    print(n_arr)
    res_arr = n_arr[:, [1]]
    print("Accessed Rows:")
    print(res_arr)

    # Example 2: Accessing the First and Last rows of 3D NumPy array
    n_arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], 
                     [[50, 65, 8], [70, 85, 10], [11, 22, 33]],
                     [[19, 69, 36], [1, 5, 24], [4, 20, 96]]])
    print("\nArray:")
    print(n_arr)
    res_arr = n_arr[:, [0, 2]]
    print("Accessed Rows:")
    print(res_arr)

# Main function
def main():
    print("How to Access Different Rows of a Multidimensional NumPy Array")
    print("-----------------------------------------------------------------")

    accessing_rows_in_2d_arrays()
    accessing_rows_in_3d_arrays()

if __name__ == "__main__":
    main()