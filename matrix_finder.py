import time
import logging
from common import binary_search
logger = logging.getLogger(__name__)

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
        state: Boolean result of the search algorithm.
    """

    def __init__(self, matrix):
        """Initialize MatrixFinder matrix input.
        
        Args:
            matrix (array[float][float]): 
                Nested list of floats representing a 2d matrix.
        """

        self._matrix = matrix
        self._m = len(matrix)
        self._n = len(matrix[0])
        self.x = None
        self.state = False

    def _select_row(self):
        """Modified binary search to select row target is in.
        
        Returns:
            The index of the row the taget is in.
            Returns -1 if the target is not the matrix.
        """

        low = 0
        high = self._m - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2

            if mid == high:
                return mid
            
            mid_val = self._matrix[mid][0]
     
            if mid_val < self.x:
                # check if this row contains the target
                next_val = self._matrix[mid + 1][0]

                if next_val > self.x:
                    return mid
                low = mid + 1
            
            elif mid_val > self.x:
                # check if the previous row contains the target
                prev_val = self._matrix[mid - 1][0]

                if prev_val < self.x:
                    return mid - 1
                high = mid - 1

            else:
                return mid
 
        # target is not in the matrix
        return -1

    def _find_x(self, x):
        """Find row and column of target if in matrix using binary search.
        
        Args:
            x (float): The target value.
        """

        self.x = x

        # search for containing row
        row = self._select_row()
        if row >= 0:
            # search for containing column
            col = binary_search(self._matrix[row], self.x)
            if col >= 0:
                self.state = True
                logger.info("Target at [{}][{}]".format(row, col))

    def find(self, x):
        """Execute search algorithm and record execution time.
        
        Args:
            x (float): Target value.

        Returns:
            A boolean result for if the target is found or not.
        """

        # use process time instead of performance time for accuracy
        start_time = time.process_time_ns()
        
        # catch any TypeErrors
        try:
            self._find_x(x)
        except TypeError:
            logger.error("TypeError detected")
            self.state = False

        exec_time_ms = (time.process_time_ns() - start_time) // 1000
        logger.info("Execution time = {} ms".format(exec_time_ms))
        
        if self.state:
            logger.info("Success!")
        else:
            logger.info("Failure!")

        return self.state



