# numpy.stack() in Python

import numpy as np

# Section 1: Stacking two 1D arrays
def stacking_two_1d_arrays():
    print("Stacking two 1D arrays:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Array a:", a)
    print("Array b:", b)
    c = np.stack((a, b), axis=0)
    print("Stacked array (axis=0):\n", c)
    c = np.stack((a, b), axis=1)
    print("Stacked array (axis=1):\n", c)

# Section 2: Stacking two 2D arrays
def stacking_two_2d_arrays():
    print("\nStacking two 2D arrays:")
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[7, 8, 9], [10, 11, 12]])
    print("Array x:\n", x)
    print("Array y:\n", y)
    c = np.stack((x, y), axis=0)
    print("Stacked array (axis=0):\n", c)
    c = np.stack((x, y), axis=1)
    print("Stacked array (axis=1):\n", c)
    c = np.stack((x, y), axis=2)
    print("Stacked array (axis=2):\n", c)

# Section 3: Stacking more than two 2D arrays
def stacking_more_than_two_2d_arrays():
    print("\nStacking more than two 2D arrays:")
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[7, 8, 9], [10, 11, 12]])
    z = np.array([[13, 14, 15], [16, 17, 18]])
    print("Array x:\n", x)
    print("Array y:\n", y)
    print("Array z:\n", z)
    c = np.stack((x, y, z), axis=0)
    print("Stacked array (axis=0):\n", c)
    c = np.stack((x, y, z), axis=1)
    print("Stacked array (axis=1):\n", c)
    c = np.stack((x, y, z), axis=2)
    print("Stacked array (axis=2):\n", c)

# Section 4: Stacking two 3D arrays
def stacking_two_3d_arrays():
    print("\nStacking two 3D arrays:")
    m = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
    n = np.array([[[51, 52, 53], [54, 55, 56], [57, 58, 59]],
                  [[110, 111, 112], [113, 114, 115], [116, 117, 118]]])
    print("Array m:\n", m)
    print("Array n:\n", n)
    c = np.stack((m, n), axis=0)
    print("Stacked array (axis=0):\n", c)
    c = np.stack((m, n), axis=1)
    print("Stacked array (axis=1):\n", c)
    c = np.stack((m, n), axis=2)
    print("Stacked array (axis=2):\n", c)
    c = np.stack((m, n), axis=3)
    print("Stacked array (axis=3):\n", c)

# Main function
def main():
    print("numpy.stack() in Python")
    print("------------------------")

    stacking_two_1d_arrays()
    stacking_two_2d_arrays()
    stacking_more_than_two_2d_arrays()
    stacking_two_3d_arrays()

if __name__ == "__main__":
    main()
    