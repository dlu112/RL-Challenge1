# Programming Challenge
# Part 1: Algorithmic Challenge
import time
from common import binary_search

class MatrixFinder:
    """Search an m x n matrix for a specified target value.

    Each row in the target matrix is sorted in ascending order.
    The first number of each row is larger than the last number of the preceding row.
    Performs binary search to identify which row the target is in. Execution time is O(log(m)).
    Performs binary search again on the row. Execution time is O(log(n)).
    Total execution time is O(log(N)) where N = m x n.
    
    Attributes:
        matrix: A python nested list of values.
        m: An integer representing the number of rows.
        n: An integer representing the number of columns.
        x: The target value.
        exec_time: Time in ms taken for the search algorithm to complete.
        state: Boolean result of the search algorithm.
        debug: Boolean whether to print debug messages.
    """

    def __init__(self, matrix, debug=False):
        """Initialize MatrixFinder matrix input.
        
        Args:
            matrix (array[float][float]): Nested list of floats representing a 2d matrix.
            debug (boolean): Whether to output debug messages, default False.
        """

        self.matrix = matrix
        self.n = len(matrix[0])
        self.m = len(matrix)
        self.x = None
        self.exec_time_ms = 0
        self.state = False
        self.debug = debug

    def __log_time(self):
        """Log execution time to console"""

        if self.debug:
            print("Execution time =", self.exec_time_ms, "ms")

    def __select_row(self):
        """Modified binary search to select row target is in.
        
        Returns:
            The index of the row the taget is in.
            Returns -1 if the target is not the matrix.
        """

        low = 0
        high = self.m - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            if mid == high:
                return mid
            
            mid_val = self.matrix[mid][0]
     
            if mid_val < self.x:
                # check if this row contains the target
                next_val = self.matrix[mid + 1][0]

                if next_val > self.x:
                    return mid
                low = mid + 1
            
            elif mid_val > self.x:
                # check if the previous row contains the target
                prev_val = self.matrix[mid - 1][0]

                if prev_val < self.x:
                    return mid - 1
                high = mid - 1

            else:
                return mid
 
        # target is not in the matrix
        return -1

    def __find_x(self, x):
        """Find row and column of target if in matrix using binary search.
        
        Args:
            x (float): The target value.
        """

        self.x = x

        # search for containing row
        row = self.__select_row()
        if row >= 0:
            # search for containing column
            col = binary_search(self.matrix[row], self.x)
            if col >= 0:
                self.state = True
                if self.debug:
                    print("Target at [{}][{}]".format(row, col))
    
    def find(self, x, debug=False):
        """Execute search algorithm and record execution time.
        
        Args:
            x (float): Target value.
            debug (bool): Whether to output debug messages, default False.

        Returns:
            A boolean result for if the target is found or not.
        """

        self.debug = debug

        # use process time instead of performance time for accuracy
        start_time = time.process_time_ns()
        
        # catch any TypeErrors
        try:
            self.__find_x(x)
        except TypeError:
            if self.debug:
                print("Error: TypeError detected")
            self.state = False

        self.exec_time_ms = (time.process_time_ns() - start_time) // 1000
        
        if self.debug:
            self.__log_time()
            if self.state:
                print("SUCCESS!")
            else:
                print("FAILURE")

        return self.state



