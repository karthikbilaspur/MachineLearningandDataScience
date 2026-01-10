# NumPy Array Broadcasting

import numpy as np

# Section 1: Broadcasting a Scalar to a 1D Array
def broadcasting_scalar_to_1d_array():
    print("Broadcasting a Scalar to a 1D Array:")
    arr = np.array([1, 2, 3])
    print("Original Array:", arr)
    res = arr + 1
    print("Result:", res)

# Section 2: Broadcasting a 1D Array to a 2D Array
def broadcasting_1d_array_to_2d_array():
    print("\nBroadcasting a 1D Array to a 2D Array:")
    a = np.array([2, 4, 6])
    b = np.array([[1, 3, 5], [7, 9, 11]])
    print("Array a:", a)
    print("Array b:\n, b)
    res = a + b
    print("Result:\n", res)

# Section 3: Broadcasting in Conditional Operations
def broadcasting_in_conditional_operations():
    print("\nBroadcasting in Conditional Operations:")
    a = np.array([12, 24, 35, 45, 60, 72])
    b = np.array(["Adult", "Minor"])
    print("Array a:", a)
    res = np.where(a > 18, b[0], b[1])
    print("Result:", res)

# Section 4: Using Broadcasting for Matrix Multiplication
def broadcasting_for_matrix_multiplication():
    print("\nUsing Broadcasting for Matrix Multiplication:")
    m = np.array([[1, 2], [3, 4]])
    v = np.array([10, 20])
    print("Matrix m:\n", m)
    print("Vector v:", v)
    res = m * v
    print("Result:\n", res)

# Section 5: Scaling Data with Broadcasting
def scaling_data_with_broadcasting():
    print("\nScaling Data with Broadcasting:")
    fd = np.array([[0.8, 2.9, 3.9], [52.4, 23.6, 36.5], [55.2, 31.7, 23.9], [14.4, 11.0, 4.9]])
    cpg = np.array([9, 4, 4])
    print("Food Data:\n", fd)
    print("Calories per Gram:", cpg)
    res = fd * cpg
    print("Result:\n", res)

# Section 6: Adjusting Temperature Data Across Multiple Locations
def adjusting_temperature_data():
    print("\nAdjusting Temperature Data Across Multiple Locations:")
    temp = np.array([[30, 32, 34, 33, 31], [25, 27, 29, 28, 26], [20, 22, 24, 23, 21]])
    corr = np.array([1.5, -0.5, 2.0])
    print("Temperature Data:\n", temp)
    print("Correction Factors:", corr)
    res = temp + corr[:, None]
    print("Result:\n", res)

# Section 7: Normalizing Image Data
def normalizing_image_data():
    print("\nNormalizing Image Data:")
    img = np.array([[100, 120, 130], [90, 110, 140], [80, 100, 120]])
    print("Image Data:\n", img)
    m = img.mean(axis=0)
    s = img.std(axis=0)
    res = (img - m) / s
    print("Result:\n", res)

# Section 8: Centering Data in Machine Learning
def centering_data_in_machine_learning():
    print("\nCentering Data in Machine Learning:")
    data = np.array([[10, 20], [15, 25], [20, 30]])
    print("Data:\n", data)
    m = data.mean(axis=0)
    res = data - m
    print("Result:\n", res)

# Main function
def main():
    print("NumPy Array Broadcasting")
    print("------------------------")

    broadcasting_scalar_to_1d_array()
    broadcasting_1d_array_to_2d_array()
    broadcasting_in_conditional_operations()
    broadcasting_for_matrix_multiplication()
    scaling_data_with_broadcasting()
    adjusting_temperature_data()
    normalizing_image_data()
    centering_data_in_machine_learning()

if __name__ == "__main__":
    main()