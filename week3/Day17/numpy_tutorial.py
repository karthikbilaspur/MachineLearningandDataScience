# NumPy Tutorial

import numpy as np

# Creating NumPy Arrays
def create_arrays():
    # Converting list into numpy array
    a = [9, 3, 3, 5]
    print("Array:", np.array(a))

    # Creating numpy array
    n = np.array([9, 3, 3, 5])
    print("Array:", n)

# Basic Arithmetic Operations
def basic_arithmetic():
    n = np.array([9, 3, 3, 5])
    print("Mean:", n.mean())

# Linear Algebra with NumPy
def linear_algebra():
    A = np.array([[1, 2], [3, 4]])
    res = np.dot(A, A)  # Matrix multiplication
    print("Matrix Multiplication:\n", res)

# Random Number Generation and Statistics
def random_number_generation():
    a = np.random.normal(0, 1, 5)  # 5 values from normal distribution
    print("Data:", a)
    print("Mean:", np.mean(a))

# Advanced NumPy Operations
def advanced_operations():
    a = np.arange(5)
    r = a * 10  # Vectorized operation (fast and efficient)
    print("Vectorized Operation:", r)

# Main function
def main():
    print("NumPy Tutorial")
    print("----------------")

    print("\nCreating NumPy Arrays:")
    create_arrays()

    print("\nBasic Arithmetic Operations:")
    basic_arithmetic()

    print("\nLinear Algebra with NumPy:")
    linear_algebra()

    print("\nRandom Number Generation and Statistics:")
    random_number_generation()

    print("\nAdvanced NumPy Operations:")
    advanced_operations()

if __name__ == "__main__":
    main()