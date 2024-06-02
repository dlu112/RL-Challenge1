# RL-Challenge1

## Objective
Develop an algorithm, accompanied by unit tests, that is capable of searching a matrix of dimensions m x n for a specified number in logarithmic or better time complexity.

Each row within the matrix is sorted in ascending order, and the first number of each row is larger than the last number of the preceding row.

## Implementation
The implemented algorithm first performs a modified binary search to on the first element of each row to find the row containing the target value, where the first value of the selected row is less than or equal to the target and the first value of the next row is greater than the target. The algorithm will also select the last row if the first value of the last row in the matrix is less than or equal to the target. This is performed in O(log(m)) where m is the number of rows.

The algorithm next performs standard binary search on the selected row to find the target. This is performed in O(log(n)), where n is the number of columns, or elements in the row.

Overall time complexity is O(log(N)), where N is the total number of elements in the matrix.

The implementation MatrixFinder class assumes that the matrix will be input as a nested python list of floats or integers, or as a numpy matrix. This class also logs to the console the time taken in ms to execute the search function using time.process_time_ns() instead of time.perf_time_ns() for more accurate time measurement. In order to see the output time, initiate a MatrixFinder instance with debug=True.

A `common.py` file is provided which contains an iterative implementation of binary search in python.

## Running the code
The implementation is coded in python3.10.5 and requires no building. To create a MatrixFinder instance, first create a matrix and then create a MatrixFinder as MatrixFinder(matrix, bool(optional)), with an optional boolean parameter for debug and timing statements. To search the matrix for a value, call MatrixFinder.find(target).

## Unit tests
A sample test suite is provided using unittest. Unittest is used for ease of install and lack of external libraries required. The test suite implements 18 standard test cases using 6 sample matrices of various configurations. Debug statements are set True for the test suite which may clutter the output log slightly. 