# Basics of NumPy Arrays

import numpy as np

# Section 1: Types of Arrays
def types_of_arrays():
    print("Types of Arrays:")
    print("*   One Dimensional Array: A one-dimensional array is a type of linear array.")
    print("*   Multi-Dimensional Array: A Multi-Dimensional Array is an array that can store data in more than one dimension such as rows and columns.")

# Section 2: One Dimensional Array
def one_dimensional_array():
    a = [1, 2, 3, 4]
    arr = np.array(a)
    print("List in python:", a)
    print("Numpy Array in python:", arr)

# Section 3: Multi-Dimensional Array
def multi_dimensional_array():
    list_1 = [1, 2, 3, 4]
    list_2 = [5, 6, 7, 8]
    list_3 = [9, 10, 11, 12]
    sample_array = np.array([list_1, list_2, list_3])
    print("Numpy multi dimensional array in python\n", sample_array)

# Section 4: Parameters of a Numpy Array
def parameters_of_numpy_array():
    print("Parameters of a Numpy Array:")
    print("*   Axis: Axis of an array describes the order of the indexing into the array.")
    print("*   Shape: Number of elements along with each axis and is returned as a tuple.")
    print("*   Rank: Rank of an array is simply the number of axes or dimensions it has.")
    print("*   Data type objects (dtype): Data type objects (dtype) is an example of numpy.dtype class.")

# Section 5: Different Ways of Creating Numpy Array
def different_ways_of_creating_numpy_array():
    print("Different Ways of Creating Numpy Array:")
    print("*   numpy.array(): Numpy array object in Numpy is called ndarray.")
    print("*   numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object.")
    print("*   numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.")
    print("*   numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits.")
    print("*   numpy.empty(): This function create a new array of given shape and type without initializing value.")
    print("*   numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1).")
    print("*   numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0).")

# Section 6: Examples of Creating Numpy Array
def examples_of_creating_numpy_array():
    # numpy.array()
    arr = np.array([3, 4, 5, 5])
    print("Array:", arr)

    # numpy.fromiter()
    var = "Geekforgeeks"
    arr = np.fromiter(var, dtype='U2')
    print("fromiter() array:", arr)

    # numpy.arange()
    arr = np.arange(1, 20, 2, dtype=np.float32)
    print("arange() array:", arr)

    # numpy.linspace()
    arr = np.linspace(3.5, 10, 3, dtype=np.int32)
    print("linspace() array:", arr)

    # numpy.empty()
    arr = np.empty([4, 3], dtype=np.int32, order='f')
    print("empty() array:\n", arr)

    # numpy.ones()
    arr = np.ones([4, 3], dtype=np.int32, order='f')
    print("ones() array:\n", arr)

    # numpy.zeros()
    arr = np.zeros([4, 3], dtype=np.int32, order='f')
    print("zeros() array:\n", arr)

# Main function
def main():
    print("Basics of NumPy Arrays")
    print("------------------------")

    print("\nTypes of Arrays:")
    types_of_arrays()

    print("\nOne Dimensional Array:")
    one_dimensional_array()

    print("\nMulti-Dimensional Array:")
    multi_dimensional_array()

    print("\nParameters of a Numpy Array:")
    parameters_of_numpy_array()

    print("\nDifferent Ways of Creating Numpy Array:")
    different_ways_of_creating_numpy_array()

    print("\nExamples of Creating Numpy Array:")
    examples_of_creating_numpy_array()

if __name__ == "__main__":
    main()