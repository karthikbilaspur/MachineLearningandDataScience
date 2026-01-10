
# NumPy Tutorial

# Section 1: Introduction to NumPy
def intro_to_numpy():
    print("NumPy (Numerical Python) is a library for working with arrays and mathematical operations in Python.")
    print("It is a core library for scientific computing and is widely used in various fields such as physics, engineering, signal processing, and data analysis.")

# Section 2: History of NumPy
def history_of_numpy():
    print("NumPy was created by Travis Oliphant in 2005 as a combination of two earlier libraries: Numeric and Numarray.")
    print("The goal was to create a single, unified library for numerical computing in Python.")

# Section 3: Key Features of NumPy
def key_features_of_numpy():
    print("Key Features of NumPy:")
    print("*   Multi-dimensional arrays: NumPy provides support for large, multi-dimensional arrays and matrices.")
    print("*   Vectorized operations: NumPy allows you to perform operations on entire arrays at once, making it much faster than working with Python lists.")
    print("*   Linear algebra support: NumPy provides an extensive range of linear algebra functions, including matrix multiplication, eigenvalue decomposition, and singular value decomposition.")
    print("*   Random number generation: NumPy provides a wide range of random number generators for various distributions.")

# Section 4: Why Use NumPy?
def why_use_numpy():
    print("Why Use NumPy?")
    print("*   Speed: NumPy is much faster than Python lists for numerical operations.")
    print("*   Memory efficiency: NumPy arrays are more memory-efficient than Python lists.")
    print("*   Convenience: NumPy provides a wide range of functions for performing common mathematical operations.")

# Section 5: Getting Started with NumPy
def getting_started_with_numpy():
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Array * 2:", arr * 2)

# Main function
def main():
    print("NumPy Tutorial")
    print("----------------")

    print("\nIntroduction to NumPy:")
    intro_to_numpy()

    print("\nHistory of NumPy:")
    history_of_numpy()

    print("\nKey Features of NumPy:")
    key_features_of_numpy()

    print("\nWhy Use NumPy?")
    why_use_numpy()

    print("\nGetting Started with NumPy:")
    getting_started_with_numpy()

if __name__ == "__main__":
    main()
